from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import base64
import tempfile
import logging
from ollama_client import OllamaClient
from speech_handler import SpeechHandler

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# 현재 파일의 디렉토리 경로를 가져옵니다
current_dir = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(os.path.dirname(current_dir), 'static')

app = Flask(__name__, static_folder=static_dir)
CORS(app)

ollama_client = OllamaClient()
speech_handler = SpeechHandler()

@app.route('/')
def index():
    return send_from_directory(static_dir, 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory(static_dir, path)

@app.route('/process-audio', methods=['POST'])
def process_audio():
    temp_file_path = None
    try:
        # 음성 데이터 받기
        audio_data = request.json.get('audio')
        if not audio_data:
            logging.error('No audio data received')
            return jsonify({'error': '음성 데이터가 없습니다.'}), 400

        logging.debug('Received audio data length: %d', len(audio_data))

        try:
            # Base64 디코딩
            audio_data_split = audio_data.split(',')
            # Get the content type from the data URL
            content_type = audio_data_split[0].split(';')[0].split(':')[1]
            logging.debug('Audio content type: %s', content_type)
            
            audio_binary = base64.b64decode(audio_data_split[1])
            logging.debug('Successfully decoded base64 audio data, length: %d', len(audio_binary))
        except Exception as e:
            logging.error('Failed to decode base64 audio data: %s', str(e))
            return jsonify({'error': 'Invalid audio data format'}), 400
        
        # 임시 파일로 저장
        try:
            # Determine file extension based on content type
            if 'webm' in content_type.lower():
                suffix = '.webm'
            else:
                suffix = '.wav'
            
            with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as temp_file:
                temp_file.write(audio_binary)
                temp_file_path = temp_file.name
            logging.debug('Saved audio data to temporary file: %s', temp_file_path)
        except Exception as e:
            logging.error('Failed to save audio data to temporary file: %s', str(e))
            return jsonify({'error': 'Failed to save audio data'}), 500

        try:
            # 음성을 텍스트로 변환
            text = speech_handler.transcribe_file(temp_file_path)
            if not text:
                logging.error('Speech recognition failed')
                return jsonify({'error': '음성을 인식하지 못했습니다.'}), 400
            logging.debug('Transcribed text: %s', text)

            # Ollama AI에 질문
            response = ollama_client.ask(text)
            logging.debug('AI response: %s', response)

            # 음성 응답 생성
            audio_response = speech_handler.generate_speech(response)
            if not audio_response:
                logging.error('Failed to generate speech response')
                return jsonify({'error': '음성 응답을 생성하지 못했습니다.'}), 500
            logging.debug('Generated speech response')

            return jsonify({
                'text': text,
                'response': response,
                'audio': audio_response
            })

        except Exception as e:
            logging.error('Error during processing: %s', str(e))
            return jsonify({'error': str(e)}), 500

    except Exception as e:
        logging.error('Unexpected error: %s', str(e))
        return jsonify({'error': str(e)}), 500

    finally:
        # 임시 파일 삭제
        if temp_file_path and os.path.exists(temp_file_path):
            try:
                os.unlink(temp_file_path)
                logging.debug('Deleted temporary file: %s', temp_file_path)
            except Exception as e:
                logging.error('Failed to delete temporary file: %s, error: %s', temp_file_path, str(e))

if __name__ == '__main__':
    os.makedirs(static_dir, exist_ok=True)
    project_root = os.path.dirname(current_dir)
    ssl_context = (
        os.path.join(project_root, 'ssl/cert.pem'),
        os.path.join(project_root, 'ssl/key.pem')
    )
    print(f"Static directory: {static_dir}")
    print(f"SSL certificate: {ssl_context[0]}")
    print(f"SSL key: {ssl_context[1]}")
    app.run(debug=True, ssl_context=ssl_context, host='0.0.0.0', port=8443)