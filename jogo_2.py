from cores import *
from time import sleep as tempo_de_pausa
from random import randint

def jogo_2():
        
        # APRESENTAÇÃO DO JOGO
        jogo_da_velha_mostruário = [
        "  1 | 2 |  3 ",
        " ___|___|___ ",
        "  4 | 5 | 6  ",
        " ___|___|___ ",
        "  7 | 8 | 9  ",
        "    |   |    "
        ]

        for linha in jogo_da_velha_mostruário:
            print(azul(),linha,apaga())

            
        # APRESENTAÇÃO DAS REGRAS
        print(magenta()+'REGRAS:\nPode jogar na horizontal, na vertical ou na diagonal\n')
        print('Vence aquele que completar primeiro a coluna,\nou a linha, ou a diagonal com seu respectivo caractere.\n')

        tempo_de_pausa(1)

        print('Escolha um local para jogar, dente estes 9 listados na imagem acima, ',end='')

        print('usando os caracteres: X e O\n')
        print('Você terá 5 chances de vencer o computador\nCaso você perca estas 5 chances, lhe será adcionado apenas 10 moedas em seu saldo\n')

        tempo_de_pausa(1)

        print('Boa sorte!',apaga())


        # ESCOLHER O CARACTERE
        escolha_do_jogador=(input('Vc deseja escolher seu caractere ou deseja que o computador escolha?\n[s]-Usuário escolhe\n[n]-Computador escolhe\n').lower().strip()[0])

        while escolha_do_jogador not in 'sn':

            escolha_do_jogador=(input('ERRO! VALOR INVÁLIDO! Você deseja escolher seu caractere ou deseja que o computador escolha?\n[s]-Usuário escolhe\n[n]-Computador escolhe\n').lower().strip()[0])

        
        if escolha_do_jogador=='s':

                escolhido=input('Qual caractere você escolhe?\n[x] ou [O]').lower().strip()[0]
                
                while escolhido not in 'xo':

                    escolhido=input(('ERRO! VALOR INVÁLIDO! Qual caractere você escolhe?\n[x] ou [O]\n')).lower().strip()[0]


                if escolhido in 'xo':
                        
                        if escolhido=='x':
                            escolha_do_jogador=escolhido
                            escolha_por_pc='O'

                        else:  
                            escolha_do_jogador=escolhido
                            escolha_por_pc='x'
                        
        
        elif escolha_do_jogador=='n':

            escolha_por_pc=randint(1,2)

            if escolha_por_pc==1:
                escolha_por_pc='x'
                escolha_do_jogador='O'

            else:
                escolha_por_pc='O'
                escolha_do_jogador='X'

        print(f'A escolha do computador foi {escolha_por_pc} e a sua foi {escolha_do_jogador}')

    
        # ESTRUTURA DO JOGOs    
        
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

        while contador_jogadas<=9:


            if contador_jogadas==9:
                print("\n   |   |   ")
                print(" " + jogo[0] + " | " + jogo[1] + " | " + jogo[2] + " ")
                print("___|___|___")
                print("   |   |   ")
                print(" " + jogo[3] + " | " + jogo[4] + " | " + jogo[5] + " ")
                print("___|___|___")
                print("   |   |   ")
                print(" " + jogo[6] + " | " + jogo[7] + " | " + jogo[8] + " ")
                print("   |   |   \n")
                break
                 


            print("\n   |   |   ")
            print(" " + jogo[0] + " | " + jogo[1] + " | " + jogo[2] + " ")
            print("___|___|___")
            print("   |   |   ")
            print(" " + jogo[3] + " | " + jogo[4] + " | " + jogo[5] + " ")
            print("___|___|___")
            print("   |   |   ")
            print(" " + jogo[6] + " | " + jogo[7] + " | " + jogo[8] + " ")
            print("   |   |   \n")



            # JOGADA DA PESSOA
            if contador_jogadas%2==0:
                escolha_local=int(input('Qual local você deseja jogar? de 1 a 9.\n'))

                while 1>escolha_local<1 or escolha_local>9 or jogo[escolha_local-1]!='a':
                    escolha_local=int(input('ERRO! VALOR INVÁLIDO! Qual local você deseja jogar? de 1 a 9.\n'))

                jogo.pop(escolha_local-1)
                jogo.insert(escolha_local-1,escolha_do_jogador)


            # JOGADA DO COMPUTADOR
            else:   
                escolha_local = randint(1, 9)
                while jogo[escolha_local-1] != 'a':
                    escolha_local = randint(1, 9)
                print(f'Computador jogou na posição {escolha_local}')
                jogo[escolha_local-1] = escolha_por_pc


            if escolha_local==1 or escolha_local==2 or escolha_local==3:
                lista_1_horizontal.append(jogo[escolha_local-1])
            
            if escolha_local==4 or escolha_local==5 or escolha_local==6:
                lista_2_horizontal.append(jogo[escolha_local-1])
            

            if escolha_local==7 or escolha_local==8 or escolha_local==9:
                lista_3_horizontal.append(jogo[escolha_local-1])

            if escolha_local==1 or escolha_local==4 or escolha_local==7:
                lista_1_vertical.append(jogo[escolha_local-1])

            if escolha_local==2 or escolha_local==5 or escolha_local==8:
                lista_2_vertical.append(jogo[escolha_local-1])
            
            if escolha_local==3 or escolha_local==6 or escolha_local==9:
                 lista_3_vertical.append(jogo[escolha_local-1])


            contador_jogadas+=1
            print(f'horizontal 1={lista_1_horizontal}, horizontal 2={lista_2_horizontal}, horizontal 3={lista_3_horizontal}\n vertotal 1={lista_1_vertical}, vertical 2={lista_2_vertical}, vertical 3={lista_3_vertical}')
            
             
jogo_2()    



                                                                                 