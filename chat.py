import openai

# Defina sua chave de API da OpenAI
api_key = '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'

# Configuração da API
openai.api_key = api_key

# Função para interagir com o modelo GPT-3 (ChatGPT)
def ask_chatbot(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Você pode alterar o modelo conforme sua assinatura na OpenAI
        messages=[
            {"role": "system", "content": prompt},
        ],
    )
    return response.choices[0].message['content']

# Exemplo de interação com o chatbot
user_input = input("Você: ")

while user_input.lower() != 'exit':
    response = ask_chatbot(user_input)
    print("Chatbot:", response)
    user_input = input("Você: ")