from cores import *
from time import sleep as tempo_de_pausa
from random import randint

def jogo_2():
        
        # APRESENTAÇÃO DO JOGO
        jogo_da_velha_mostruário ='''
          1 | 2 |  3 
         ___|___|___ 
          4 | 5 | 6  
         ___|___|___ 
          7 | 8 | 9  
            |   |    
        '''

        print(jogo_da_velha_mostruário)

            
        # APRESENTAÇÃO DAS REGRAS
        print(magenta()+'REGRAS:\nPode jogar na horizontal, na vertical ou na diagonal\n')
        print('Vence aquele que completar primeiro a coluna,\nou a linha, ou a diagonal com seu respectivo caractere.\n')

        # tempo_de_pausa(1)

        print('Escolha um local para jogar, dente estes 9 listados na imagem acima,usando os caracteres: X e O\nBoa sorte!',apaga())

        # print('Você terá 5 chances de vencer o computador\nCaso você perca estas 5 chances, lhe será adcionado apenas 10 moedas em seu saldo\n')


        # ESCOLHER O CARACTERE
        escolha_do_jogador=(input('Qual seu caractere?\n[X]-para "x"\n[O]-Para "O"\n').lower().strip()[0])

        while escolha_do_jogador not in 'xo':

            escolha_do_jogador=(input('ERRO! VALOR INVÁLIDO! Qual seu caractere?\n[X]-para "x"\n[O]-Para "O"\n').lower().strip()[0])
      
        if escolha_do_jogador=='x':
            escolha_por_pc='o'

        elif escolha_do_jogador=='o':
            escolha_por_pc='x'
    
        # ESTRUTURA DO JOGO    
        
        contador_jogadas=0
        jogador_vencedor=0

        lista_1_horizontal=[]
        lista_2_horizontal=[]
        lista_3_horizontal=[]

        lista_1_vertical=[]
        lista_2_vertical=[]
        lista_3_vertical=[]

        lista_1_diagonal=[]
        lista_2_diagonal=[]

        jogo=['a','a','a','a','a','a','a','a','a']

        while jogador_vencedor!=5:


            contador_jogadas+=1

            if 'a' not in jogo:
                print(tabuleiro_novo)
                tempo_de_pausa(1)
                print('EMPATE')
                tempo_de_pausa(1)
                print('COMEÇANDO NOVO JOGO...')
                tempo_de_pausa(1)

                contador_jogadas=0

                lista_1_horizontal=[]
                lista_2_horizontal=[]
                lista_3_horizontal=[]

                lista_1_vertical=[]
                lista_2_vertical=[]
                lista_3_vertical=[]

                lista_1_diagonal=[]
                lista_2_diagonal=[]

                jogo=['a','a','a','a','a','a','a','a','a']

            tabuleiro_novo='''
                {}  | {} |  {} 
                ___|___|___ 
                {}  | {} | {}  
                ___|___|___ 
                {}  | {} | {}  
                   |   |    
                '''.format(jogo[0],jogo[1],jogo[2],jogo[3],jogo[4],jogo[5],jogo[6],jogo[7],jogo[8])
            print(tabuleiro_novo)

            # JOGADA DA PESSOA
            if contador_jogadas%2==0:
                escolha_local=int(input('Qual local você deseja jogar? de 1 a 9.\n'))

                while 1>escolha_local<1 or escolha_local>9 or jogo[escolha_local-1]!='a':
                    escolha_local=int(input('ERRO! VALOR INVÁLIDO! Qual local você deseja jogar? de 1 a 9.\n'))

                jogo.pop(escolha_local-1)
                jogo.insert(escolha_local-1,escolha_do_jogador)


            # JOGADA DO COMPUTADOR
            else:   
                escolha_local=randint(1, 9)

                while jogo[escolha_local-1]!='a':
                    escolha_local = randint(1, 9)

                print(f'Computador jogou na posição {escolha_local}')
                jogo[escolha_local-1]=escolha_por_pc



            # ORGANIZAÇÃO DOS DADOS

            if escolha_local in [1, 2, 3]:
                lista_1_horizontal.append(jogo[escolha_local - 1])
            elif escolha_local in [4, 5, 6]:
                lista_2_horizontal.append(jogo[escolha_local - 1])
            elif escolha_local in [7, 8, 9]:
                lista_3_horizontal.append(jogo[escolha_local - 1])
            elif escolha_local in [1, 4, 7]:
                lista_1_vertical.append(jogo[escolha_local - 1])
            elif escolha_local in [2, 5, 8]:
                lista_2_vertical.append(jogo[escolha_local - 1])
            elif escolha_local in [3, 6, 9]:
                lista_3_vertical.append(jogo[escolha_local - 1])
            elif escolha_local in [1, 5, 9]:
                lista_1_diagonal.append(jogo[escolha_local - 1])
            elif escolha_local in [3, 5, 7]:
                lista_2_diagonal.append(jogo[escolha_local - 1])

            # CONFERIR O VENCEDOR

            def verificar_o_vencedor(jogo):
                # CONFERIR LINHAS
                for elemento in range(0, 9, 3):
                    if jogo[elemento]==jogo[elemento + 1]==jogo[elemento + 2] and jogo[elemento]!='a':
                        return jogo[elemento]

                # CONFERIR COLUNAS
                for elemento_2 in range(3):
                    if jogo[elemento_2]==jogo[elemento_2 + 3]==jogo[elemento_2 + 6] and jogo[elemento_2]!='a':
                        return jogo[elemento_2]

                # CONFERIR DIAGONAIS
                if jogo[0]==jogo[4]==jogo[8] and jogo[0]!='a':
                    return jogo[0]
                if jogo[2]==jogo[4]==jogo[6] and jogo[2]!='a':
                    return jogo[elemento_2]

                return None
            
            vencedor=verificar_o_vencedor(jogo)
            if vencedor:
                if vencedor==escolha_do_jogador:
                    print('JOGADOR VENCEU')
                    jogador_vencedor+=1
                else:
                    print('Computador venceu')

                

                print('COMEÇANDO UM NOVO JOGO...')
                tempo_de_pausa(1)

                contador_jogadas=0

                lista_1_horizontal=[]
                lista_2_horizontal=[]
                lista_3_horizontal=[]

                lista_1_vertical=[]
                lista_2_vertical=[]
                lista_3_vertical=[]

                lista_1_diagonal=[]
                lista_2_diagonal=[]

                jogo=['a','a','a','a','a','a','a','a','a']
                
                
        
            tempo_de_pausa(1)
        print('O JOGO DA VITÓRIA, PARABÉNS CAMPEÃO.')

             
jogo_2()    
