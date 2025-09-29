import requests

class OllamaClient:
    def __init__(self, model="gemma3:12b", base_url="http://localhost:11434"):
        self.model = model
        self.base_url = base_url
    
    def ask(self, prompt):
        """Ollama API에 질문을 보내고 응답을 받습니다."""
        try:
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False
                }
            )
            response.raise_for_status()
            return response.json()["response"]
        except requests.exceptions.RequestException as e:
            print(f"Ollama API 오류: {str(e)}")
            return "죄송합니다. 현재 AI 서비스에 연결할 수 없습니다."