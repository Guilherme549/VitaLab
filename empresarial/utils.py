import string
from random import choice, shuffle


def gerar_senha_aleatoria(tamanho):
    caracteres_especiais = string.punctuation
    caracteres = string.ascii_letters
    numeros_list = string.digits

    sobra = 0
    qtd = tamanho // 3
    if not tamanho % 3 == 0:
        sobra = tamanho - (qtd * 3)

    letras = ""

    for i in range(0, qtd + sobra):
        letras += choice(caracteres)

    numeros = ""

    for i in range(0, qtd):
        numeros += choice(numeros_list)

    especias = ""

    for i in range(0, qtd):
        especias += choice(caracteres_especiais)

    senha = list(letras + numeros + especias)
    shuffle(senha)


    return ''.join(senha) # retorna a lista em forma de string