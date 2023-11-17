import re

#Dict com os pontos de interesse
point_dict = {
    "prego": "armazém",
    "parafuso": "depósito",
    "fita": "caixa de ferramentas",
    "trena": "sala de medições",
    "porca": "gaveta de ferragens",
    "martelo": "prateleira"
}



def go_to(point): #Função que recebe o ponto de interesse e imprime a localização
    if point in point_dict: #Verifica se o ponto de interesse está no dict
        print(f"Vamo la para '{point}': {point_dict[point]}") #Imprime a localização
    else:
        print(f"Vish, vou ficar devendo  esse item aqui oh",{point},"Foi mal, não sei onde fica.")#Caso não esteja,
        #imprime essa mensagem

#Dict com as intenções e suas respectivas funções
intent_dict = {
    r"\b[Vv][áa](?:\spara)?\s?[oa]?\s(.+)": go_to, # "Va para o ..."
    #Seguindo essa logica, a primeira parte possiblita o uso de "Vá para o ..." e "Va para o ...", sendo ele maiusculo ou minusculo
    #A segunda parte possiblita o uso de do pronome adequado como [a] ou [o]

    r"\b(?:[Vv]a)(?:\spara)?(?:\so)?\s(?:objeto)?\s(.+)": go_to, # Va para o obejto ...
    #Podemos dizer que essa parte segue a logia da primeira mas apenas com o uso de "Va para o objeto ..."

    r"\b(?:[Qq]uero)(?:\sum[a])?\s(.+)": go_to # "Quero o ..."
    #Para diferenciar um pouco, mas bem pouco, Botei um "\sum[a]" para que o usuario possa usar "Quero um..." ou "Quero uma...

}

def main(): #Função principal
    command = input("O que queres hoje? ") #Recebe o comando do pronpt
    for key, function in intent_dict.items(): #Percorre o dict de intenções
        pattern = re.compile(key) #Compila a expressão regular
        point = pattern.findall(command) #Procura a expressão regular no comando
        if point:
            print("ShowVe, calma ai")#Caso encontre, imprime essa mensagem
            function(point[0])#Chama a função com o ponto de interesse
            break#Para o loop
    else:
        print("Não entendi o que você quis dizer.")#Caso não encontre, imprime essa mensagem

if __name__ == "__main__":
    main()
