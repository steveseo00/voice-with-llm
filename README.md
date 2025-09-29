# Voice Chat with AI 🎙️💬

A web-based interface for real-time voice conversations with AI. Simply speak your questions through the browser, and the AI will generate responses and speak them back to you.

## Key Features ✨

- Real-time voice recording and conversion (WebM/Opus support)
- Natural conversation with AI
- AI responses through speech synthesis
- Modern chat interface
- Real-time processing status display
- Secure connection via HTTPS

## Getting Started 🚀

### Prerequisites

- > Python 3.8 
- [FFmpeg](https://ffmpeg.org/download.html)
- [Ollama](https://ollama.ai)

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/voice-with-ai.git
cd voice-with-ai
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Generate SSL certificate (required for local HTTPS)
```bash
mkdir ssl
openssl req -x509 -newkey rsa:4096 -nodes -out ssl/cert.pem -keyout ssl/key.pem -days 365 -subj "/CN=localhost"
```

5. Install Ollama and download model
```bash
# Install Ollama (refer to https://ollama.ai)
ollama pull gemma  # Download default AI model
```

### Running the Application

1. Start Ollama server
```bash
ollama serve
```

2. Run web server
```bash
python src/web_server.py
```

3. Access in browser
- Navigate to https://localhost:8443
- For security warning, click "Advanced" > "Proceed to unsafe site"

## How to Use 📝

1. Allow microphone access when prompted by the browser
2. Click the "Record" button to start recording
3. Click the button again to stop recording when finished speaking
4. Wait for AI's voice response
5. Conversation history is automatically displayed in the chat window

## Technology Stack 🛠️

- **Backend**
  - Flask (Web Server)
  - SpeechRecognition
  - gTTS (TTS)
  - pydub
  - Ollama
  
- **Frontend**
  - HTML5
  - CSS3
  - JavaScript (MediaRecorder API)

## Project Structure 📁

```
voice-with-ai/
├── README.md
├── requirements.txt
├── ssl/
│   ├── cert.pem
│   └── key.pem
├── src/
│   ├── web_server.py      # Main web server
│   ├── speech_handler.py  # Speech processing logic
│   └── ollama_client.py   # AI model client
└── static/
    └── index.html         # Web interface
```

## Core Features Explained 🔍

### Voice Processing Pipeline

1. **Voice Recording**
   - Uses browser's MediaRecorder API
   - Records in WebM format (Opus codec)

2. **Audio Conversion**
   - WebM to WAV conversion (using FFmpeg)
   - Sample rate and channel normalization

3. **Speech Recognition**
   - Utilizes Google Speech Recognition
   - Supports multiple languages

4. **AI Processing**
   - Response generation through Ollama API
   - Context-aware natural conversation

5. **Speech Synthesis**
   - Voice conversion using Google TTS
   - Natural voice output in multiple languages

## Security Considerations 🔒

- Secure communication via HTTPS
- Data privacy ensured through locally running AI model
- Voice data stored only as temporary files and deleted immediately after processing

## Troubleshooting 💡

### Common Issues

1. **Microphone Not Detected**
   - Check microphone permissions in browser settings
   - Verify HTTPS connection

2. **Speech Not Recognized**
   - Check microphone volume
   - Minimize background noise
   - Verify internet connection

3. **No AI Response**
   - Check Ollama server status
   - Verify model download status

### Error Message Interpretation

- "Speech could not be recognized" - Unclear speech or high background noise
- "Server connection error" - Check Ollama server connection
- "Microphone access error" - Check browser permissions

## License 📄

This project is distributed under the MIT License.

## Contributing 🤝

Suggestions and bug reports for project improvement are always welcome.
Feel free to create an issue or submit a pull request.

## Acknowledgments 🙏

This project was made possible thanks to these open-source projects:

- [Flask](https://flask.palletsprojects.com/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [gTTS](https://pypi.org/project/gTTS/)
- [Ollama](https://ollama.ai)

---
Last updated: September 29, 2025