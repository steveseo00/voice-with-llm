import speech_recognition as sr
from gtts import gTTS
import os
import tempfile
import sounddevice as sd
import soundfile as sf
import base64
from pydub import AudioSegment
import io

class SpeechHandler:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.temp_dir = tempfile.gettempdir()
    
    def transcribe_file(self, audio_file_path):
        """오디오 파일을 텍스트로 변환합니다."""
        try:
            print(f"오디오 파일 변환 시작: {audio_file_path}")
            
            # WebM에서 WAV로 변환
            try:
                # Explicitly specify the codec for WebM
                audio = AudioSegment.from_file(audio_file_path, format="webm", codec="opus")
            except Exception as e:
                print(f"WebM 형식 로드 실패, 일반 형식으로 시도: {str(e)}")
                audio = AudioSegment.from_file(audio_file_path)
            
            wav_io = io.BytesIO()
            audio.export(wav_io, format="wav", parameters=["-ac", "1", "-ar", "16000"])
            wav_io.seek(0)
            print("WAV 형식으로 변환 성공")

            # WAV 파일 처리
            with sr.AudioFile(wav_io) as source:
                print("음성 데이터 읽기 시작")
                audio_data = self.recognizer.record(source)
                print("음성 데이터 읽기 성공")
                text = self.recognizer.recognize_google(audio_data, language='ko-KR')
                print(f"음성 인식 결과: {text}")
                return text

        except sr.UnknownValueError as e:
            print(f"음성 인식 실패: 음성을 인식할 수 없음")
            return None
        except sr.RequestError as e:
            print(f"음성 인식 서비스 오류: {str(e)}")
            return None
        except Exception as e:
            print(f"예상치 못한 오류 발생: {str(e)}")
            raise

    def generate_speech(self, text):
        """텍스트를 Base64로 인코딩된 음성 데이터로 변환합니다."""
        try:
            # 임시 파일에 음성 저장
            temp_file = os.path.join(self.temp_dir, 'temp_speech.mp3')
            tts = gTTS(text=text, lang='ko')
            tts.save(temp_file)
            
            # 파일을 Base64로 인코딩
            with open(temp_file, 'rb') as audio_file:
                audio_data = audio_file.read()
                audio_base64 = base64.b64encode(audio_data).decode('utf-8')
            
            # 임시 파일 삭제
            os.remove(temp_file)
            
            return f"data:audio/mp3;base64,{audio_base64}"
        except Exception as e:
            print(f"음성 생성 오류: {str(e)}")
            return None
    
    def listen(self):
        """음성을 텍스트로 변환합니다."""
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
            
        try:
            text = self.recognizer.recognize_google(audio, language='ko-KR')
            return text
        except sr.UnknownValueError:
            return None
        except sr.RequestError as e:
            print(f"음성 인식 서비스 오류: {str(e)}")
            return None
    
    def speak(self, text):
        """텍스트를 음성으로 변환하여 재생합니다."""
        try:
            # 임시 파일에 음성 저장
            tts = gTTS(text=text, lang='ko')
            temp_file = os.path.join(self.temp_dir, 'temp_speech.mp3')
            tts.save(temp_file)
            
            # 음성 재생
            data, samplerate = sf.read(temp_file)
            sd.play(data, samplerate)
            sd.wait()
            
            # 임시 파일 삭제
            os.remove(temp_file)
        except Exception as e:
            print(f"음성 출력 오류: {str(e)}")