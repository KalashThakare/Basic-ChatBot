import requests
import os
from dotenv import load_dotenv

load_dotenv()



API_KEY = os.getenv("API_KEY")

MODEL = "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free"

API_URL = "https://api.together.xyz/v1/chat/completions"

def chat():
    print("Chatbot: Hello! Type 'exit' to quit.\n")
    
    messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        messages.append({"role": "user", "content": user_input})

        payload = {
            "model": MODEL,
            "messages": messages,
            "temperature": 0.7
        }

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        response = requests.post(API_URL, headers=headers, json=payload)

        if response.status_code == 200:
            reply = response.json()["choices"][0]["message"]["content"]
            print("Chatbot:", reply.strip())
            messages.append({"role": "assistant", "content": reply.strip()})
        else:
            print("Error:", response.status_code, response.text)
            break

if __name__ == "__main__":
    chat()
