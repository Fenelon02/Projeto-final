from random import randint
from cores import *
from time import sleep as tempo_de_espera

def jogo_quinta_fase():
    palavras=["data","result","value","item","index","count","temp","name","while","elif"]
    lista_palavras_selecionadas=[]
    
    enforcado=[
        """
           -----
           |   |
               |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ---------
        """
    ]

    for item in range(5):
        palavras_selecionadas=randint(0,len(palavras))
        lista_palavras_selecionadas.append(palavras[palavras_selecionadas-1])
        palavras.pop(palavras_selecionadas-1)

    palavra=''
    for item in lista_palavras_selecionadas:
        print(guarana()+'JOGO DA FORCA!\n')

        # tempo_de_espera(1)

        print('O algorítimo irá sortear 5 palavras, as quais, você tem que acertar ao menos uma.\n')

        # tempo_de_espera(1)

        print('Você terá 7 chances de completar a palavra corretamentet, sem erros.\n')

        # tempo_de_espera(1)

        print('Dando palpites de possíveis letras presentes na palavra.\n'+apaga())
        jogadas=[]
        contador=0
        while True:
            palavra=item
            palavra=palavra.split()

            print(palavra)
            print(f'{enforcado[0]}')

            tamanho=("_"*len(palavra[0]))
            tamanho_printável=tamanho.center(20)
            print(tamanho_printável)

            palpite=input('\nQual letra você deseja jogar? ')

            if palpite in palavra[0]:
                tempo_de_espera(1)
                local=palavra[0].index(f"{palpite}")

            letras_faltando=tamanho[:local]+palpite+tamanho[local+1:]
            jogadas.append(letras_faltando)
            print(jogadas[contador])
            contador+=1
                
                


            


            

            
        break

        

        

        


jogo_quinta_fase()
