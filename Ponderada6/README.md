# Ponderada 6

## O que é um percptron

Um Perceptron é um bloco fundamental em redes neurais artificiais, representando um neurônio artificial que recebe entradas, aplica pesos a essas entradas, soma esses valores ponderados, adiciona um viés e, em seguida, passa por uma função de ativação para produzir uma saída. O objetivo principal é aprender a classificar corretamente dados linearmente separáveis, ajustando iterativamente seus pesos e viés com base nos erros de previsão durante o treinamento. Entretanto, é importante notar que um único Perceptron é capaz de aprender apenas padrões linearmente separáveis, sendo redes mais complexas, como as multi-camadas, necessárias para lidar com problemas mais complicados e não-linearmente separáveis.

O Perceptron, proposto por Frank Rosenblatt em 1957, desempenha um papel crucial na compreensão dos fundamentos das redes neurais. É a unidade básica de processamento em modelos de aprendizado de máquina e serve como ponto de partida para explorar arquiteturas mais avançadas de redes neurais profundas.

## Sobre o codigo 

O código implementa um modelo de neurônio artificial chamado Perceptron. Esse "neurônio" é treinado para imitar o comportamento de portas lógicas simples, como AND, OR, NAND e XOR. Ele aprende ajustando pesos e um viés para produzir saídas com base em entradas fornecidas. No exemplo dado, ele tenta reproduzir o comportamento da porta XOR, mas devido à sua estrutura simples, o Perceptron tem dificuldade em representar corretamente essa porta lógica.

## SObre a porta XOR

 A porta lógica XOR é um problema que não pode ser resolvido por um unico Perceptron devido a sua natureza não linear. O Perceptron, por sua estrutura linear, não consegue separar corretamente os padrões para a porta XOR, já que ela não pode ser representada por uma única linha reta no espaço de entrada.

O XOR tem um padrão que não pode ser separado linearmente (0 XOR 1 = 1 e 1 XOR 0 = 1, enquanto 0 XOR 0 = 0 e 1 XOR 1 = 0). Para lidar com esse tipo de problema, é necessário um modelo mais complexo, como uma rede neural com camadas ocultas (hidden layers).

Ao adicionar uma camada oculta entre a entrada e a saída, a rede neural seria capaz de aprender e representar relações não lineares entre as entradas e saídas, permitindo assim que o modelo aprenda com mais precisão o comportamento da porta XOR. Além disso, a substituição da função de ativação linear por uma função sigmoide na camada oculta ajuda na representação de relações não lineares, permitindo que o modelo capture esses padrões mais complexos.





