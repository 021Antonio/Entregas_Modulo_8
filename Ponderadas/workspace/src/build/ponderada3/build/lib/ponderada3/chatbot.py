import re

# Dicionário de intenções e ações
intencoes_acoes = {
    r'.*Vá para a (\w+).*': 'Mover para a {0}',
    r'.*Dirija-se ao (\w+).*': 'Mover para o {0}',
    r'.*Me leve para a (\w+).*': 'Mover para a {0}'
}

# Função para processar o comando do usuário
def processar_comando(comando):
    for padrao, acao in intencoes_acoes.items():
        correspondencia = re.match(padrao, comando, re.IGNORECASE)
        if correspondencia:
            destino = correspondencia.group(1)
            acao_formatada = acao.format(destino)
            return acao_formatada
    return "Desculpe, não entendi o comando."

# Função principal
def main():
    while True:
        entrada_usuario = input("Usuário: ")
        if entrada_usuario.lower() == 'sair':
            break
        resposta = processar_comando(entrada_usuario)
        print("Chatbot: " + resposta)

if __name__ == "__main__":
    main()
