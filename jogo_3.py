from time import sleep as tempo_de_pausa
from cores import * 
from random import randint

def jogo_terceira_fase():

    # APRESENTAÇÃO DAS REGRAS

    print(rosa_barbie()+'Bem vindo a sua terceira fase do jogo!\n')

    print('Esta fase se trata de um questionário de python!\n')  

    print('Serão perguntas objetivas, enumeradas em "A","B","C","D",sendo apenas uma alternativa correta.\n')

    print('Serão ao todo 5 perguntas.\n') 

    # LISTA COM AS TUPLAS AS QUAIS ESTÃO INCLUÍDAS AS PERGUNTAS 

    perguntas=[
    ("Qual é a função para imprimir algo na tela em Python?",
     "a) echo()", "b) print()", "c) printf()", "d) println()"),

    ("Qual das seguintes opções é uma estrutura de dados imutável?",
     "a) lista", "b) conjunto", "c) dicionário", "d) tupla"),

    ("Qual dos seguintes é um loop em Python?",
     "a) for", "b) loop", "c) repeat", "d) iterate"),

    ("Como você cria um comentário em uma linha em Python?",
     "a) //", "b) <!--", "c) #", "d) %"),

    ("Qual é a extensão de arquivo padrão para scripts Python?",
     "a) .pyt", "b) .py", "c) .pt", "d) .pyth"),

    ("Qual a palavra-chave usada para definir uma função em Python?",
     "a) func", "b) define", "c) def", "d) function"),

    ("Como você obtém a entrada do usuário em Python 3?",
     "a) input()", "b) raw_input()", "c) scan()", "d) get()"),

    ("Qual das seguintes opções cria uma lista?",
     "a) {}", "b) []", "c) ()", "d) <>"),

    ("Qual a palavra-chave usada para verificar se uma condição é verdadeira?",
     "a) for", "b) if", "c) while", "d) switch"),

    ("Qual é a palavra-chave usada para importar um módulo em Python?",
     "a) include", "b) import", "c) using", "d) require")
    ]


    # GABARITO DAS RESPOSTAS
    resposta_correta=['b','d','a','c','b','c','a','b','b','b']

    # FUNÇÃO QUE VAI GARANTIR QUE AS PERGUNTAS NÃO SE REPITAM
    posicoes_jogadas=set()


    # JOGO EM SI
    while len(posicoes_jogadas)<5:
        posicao=randint(0,(len(perguntas)-1))

        while posicao in posicoes_jogadas:
            posicao=randint(0,(len(perguntas)-1))


        posicoes_jogadas.add(posicao)

        print(perguntas[posicao])

        resposta=input('A resposta correta é?\n[A]\n[B]\n[c]\n[D]\n').lower().strip()

        while resposta not in 'a,b,c,d':
            resposta=input('ERRO! VALOR INVÁLIDO! A resposta correta é?\n[A]\n[B]\n[c]\n[D]\n').lower().strip()


        # VERIFICAR SE A RESPOSTA ESTÁ CORRETA
        if resposta==resposta_correta[posicao]:
            print('RESPOSTA CORRETA!')
            tempo_de_pausa(1)

        else:
            while resposta!=resposta_correta[posicao]:
                resposta=input('ERRO! RESPOSTA INCORRETA. A resposta correta é?\n[A]\n[B]\n[c]\n[D]\n').lower().strip()
                if resposta==resposta_correta[posicao]:
                    print('RESPOSTA CORRETA!')
                    tempo_de_pausa(1)

    tempo_de_pausa(1)

    print(apaga()+verde()+'PARABÉNS! VOCÊ PASSOU ESTE NÍVEL.'+apaga())

