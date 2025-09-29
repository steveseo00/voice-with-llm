# Voice Chat with AI 🎙️💬

음성으로 AI와 실시간 대화할 수 있는 웹 기반 인터페이스입니다. 브라우저에서 음성으로 질문하면 AI가 답변을 생성하고 음성으로 응답합니다.

## 주요 기능 ✨

- 실시간 음성 녹음 및 변환 (WebM/Opus 지원)
- AI와의 자연스러운 대화
- 음성 합성을 통한 AI 응답
- 모던한 채팅 인터페이스
- 처리 상태 실시간 표시
- HTTPS를 통한 보안 연결

## 시작하기 🚀

### 필수 요구사항

- Python 3.8 이상
- [FFmpeg](https://ffmpeg.org/download.html)
- [Ollama](https://ollama.ai) (로컬 AI 모델 서버)

### 설치 방법

1. 저장소 클론
```bash
git clone https://github.com/yourusername/voice-with-ai.git
cd voice-with-ai
```

2. 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 또는
.\venv\Scripts\activate  # Windows
```

3. 의존성 패키지 설치
```bash
pip install -r requirements.txt
```

4. SSL 인증서 생성 (로컬 HTTPS를 위해 필요)
```bash
mkdir ssl
openssl req -x509 -newkey rsa:4096 -nodes -out ssl/cert.pem -keyout ssl/key.pem -days 365 -subj "/CN=localhost"
```

5. Ollama 설치 및 모델 다운로드
```bash
# Ollama 설치 (https://ollama.ai 참조)
ollama pull gemma  # 기본 AI 모델 다운로드
```

### 실행 방법

1. Ollama 서버 시작
```bash
ollama serve
```

2. 웹 서버 실행
```bash
python src/web_server.py
```

3. 브라우저에서 접속
- https://localhost:8443 으로 접속
- 브라우저의 보안 경고는 "고급" > "안전하지 않은 사이트로 이동" 선택

## 사용 방법 📝

1. 브라우저에서 마이크 권한 요청 시 "허용" 선택
2. "녹음하기" 버튼을 클릭하여 녹음 시작
3. 말하기가 끝나면 다시 버튼을 클릭하여 녹음 종료
4. AI의 음성 응답 대기
5. 대화 기록은 채팅창에 자동으로 표시됨

## 기술 스택 🛠️

- **Backend**
  - Flask (웹 서버)
  - SpeechRecognition (음성 인식)
  - gTTS (텍스트-음성 변환)
  - pydub (오디오 처리)
  - Ollama (로컬 AI 모델)

- **Frontend**
  - HTML5
  - CSS3
  - JavaScript (MediaRecorder API)

## 프로젝트 구조 📁

```
voice-with-ai/
├── README.md
├── requirements.txt
├── ssl/
│   ├── cert.pem
│   └── key.pem
├── src/
│   ├── web_server.py      # 메인 웹 서버
│   ├── speech_handler.py  # 음성 처리 로직
│   └── ollama_client.py   # AI 모델 클라이언트
└── static/
    └── index.html         # 웹 인터페이스
```

## 주요 기능 설명 🔍

### 음성 처리 파이프라인

1. **음성 녹음**
   - 브라우저의 MediaRecorder API 사용
   - WebM 형식으로 녹음 (Opus 코덱)

2. **음성 변환**
   - WebM -> WAV 변환 (FFmpeg 사용)
   - 샘플레이트 및 채널 정규화

3. **음성 인식**
   - Google Speech Recognition 사용
   - 한국어 음성 인식 지원

4. **AI 처리**
   - Ollama API를 통한 응답 생성
   - 컨텍스트 기반 자연스러운 대화

5. **음성 합성**
   - Google TTS를 통한 음성 변환
   - 자연스러운 한국어 음성 출력

## 보안 고려사항 🔒

- HTTPS 사용으로 안전한 통신
- 로컬에서 실행되는 AI 모델로 데이터 프라이버시 보장
- 음성 데이터는 임시 파일로만 저장되며 처리 후 즉시 삭제

## 문제 해결 💡

### 일반적인 문제

1. **마이크가 인식되지 않는 경우**
   - 브라우저 설정에서 마이크 권한 확인
   - HTTPS 연결 확인

2. **음성이 인식되지 않는 경우**
   - 마이크 볼륨 확인
   - 주변 소음 확인
   - 인터넷 연결 상태 확인

3. **AI 응답이 없는 경우**
   - Ollama 서버 실행 상태 확인
   - 모델 다운로드 상태 확인

### 에러 메시지 해석

- "음성을 인식할 수 없습니다" - 음성이 명확하지 않거나 배경 소음이 많은 경우
- "서버 연결 오류" - Ollama 서버 연결 확인 필요
- "마이크 접근 오류" - 브라우저 권한 설정 확인 필요

## 라이선스 📄

이 프로젝트는 MIT 라이선스에 따라 배포됩니다.

## 기여하기 🤝

프로젝트 개선을 위한 제안이나 버그 리포트는 언제나 환영합니다.
이슈를 생성하거나 풀 리퀘스트를 보내주세요.

## 감사의 글 🙏

이 프로젝트는 다음 오픈소스 프로젝트들의 도움을 받았습니다:

- [Flask](https://flask.palletsprojects.com/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [gTTS](https://pypi.org/project/gTTS/)
- [Ollama](https://ollama.ai)

---
마지막 업데이트: 2025년 9월 29일