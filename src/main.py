import os
from speech_handler import SpeechHandler
from ollama_client import OllamaClient

def main():
    speech_handler = SpeechHandler()
    ollama_client = OllamaClient()
    
    print("음성 인터페이스가 준비되었습니다. 말씀해주세요...")
    
    while True:
        try:
            # 음성 입력 받기
            print("\n듣고 있습니다...")
            user_input = speech_handler.listen()
            
            if not user_input:
                print("음성을 인식하지 못했습니다. 다시 말씀해주세요.")
                continue
                
            print(f"입력: {user_input}")
            
            # Ollama AI에 질문하기
            response = ollama_client.ask(user_input)
            print(f"\nAI 응답: {response}")
            
            # 음성으로 응답 출력
            speech_handler.speak(response)
            
        except KeyboardInterrupt:
            print("\n프로그램을 종료합니다.")
            break
        except Exception as e:
            print(f"오류가 발생했습니다: {str(e)}")
            continue

if __name__ == "__main__":
    main()