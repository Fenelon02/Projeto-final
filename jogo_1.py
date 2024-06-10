def jogo_1():
    from random import randint
    from time import sleep

    contador_personagem=0
    while True:

        if contador_personagem==5:
            print('PARABÉNS! VOCÊ VENCEU')
            break
        

        # GERAR O JOGO DO OPONENTE
        itens=('pedra', 'papel' , 'tesoura')
        escolhido_pelo_computador=randint(0, 2)


        # GERAR JOGO DO JOGADOR
        print('Suas opções:\n[0] pedra\n[1] papel\n[2] tesoura')
        pessoa_jogou=int(input('Digite seu número escolhido: '))


        # JOGAR APENAS NO INTERVALO DELIMITADO
        while pessoa_jogou<0 or pessoa_jogou>2:
            pessoa_jogou=int(input('ERRO! Digite seu número escolhido entre 0 e 2: '))
            if pessoa_jogou<=0 or pessoa_jogou<=2:
                pessoa_jogou=pessoa_jogou
                break


        print(f'Jogador jogou {itens[pessoa_jogou]}')
        print(f'O escolhido pelo computador foi {itens[escolhido_pelo_computador]}')


        #INUTIL APENAS PRA DECORAR
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO')
        sleep(1)



        # ESTRUTURA DO JOGO EM SI
        if escolhido_pelo_computador==0:
            if pessoa_jogou==0:
                print('EMPATE')
            elif pessoa_jogou==1:
                print('VENCEU')
                contador_personagem+=1
            elif pessoa_jogou==2:
                print('PERDEU')
            else:
                print('INVÁLIDO')
            

        elif escolhido_pelo_computador==1:
            if pessoa_jogou==0:
                print('PERDEU')
            elif pessoa_jogou==1:
                print('EMPATE')
            elif pessoa_jogou==2:
                print('GANHOU')
                contador_personagem+=1
            else:
                print('INVÁLIDA')

        elif escolhido_pelo_computador==2:
            if pessoa_jogou==0:
                print('GANHOU')
                contador_personagem+=1
            elif pessoa_jogou==1:
                print('PERDEU')
            elif pessoa_jogou==2:
                print('EMPATE')
            else:
                print('INVÁLIDO')


        # MOSTRAR A PONTUAÇÃO DO JOGADOR
        print(f'Sua pontuação atual é de {contador_personagem} pontos.')


        