import os
import openai
from dotenv import load_dotenv

load_dotenv()

def chat_with_gpt(prompt):
    openai.api_key = os.getenv('OPENAI_API_KEY')

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # ou outro modelo
        messages=[
            {"role": "system", "content": "Você é um generalista"},
            {"role": "user", "content": prompt},
        ]
    )

    return response.choices[0].message['content']

# Solicita ao usuário que insira a pergunta
user_prompt = input("Digite sua pergunta: ")

# Chama a função chat_with_gpt com a pergunta do usuário
print(chat_with_gpt(user_prompt))
