# Código desenvolvido em parceria com (@github) Lucas-BRT

from funcoes_jogo_forca import *
from cores import * 
from time import sleep as tempo_de_pausa

def jogo_quinta_fase(): 
    contador_de_vitorias=0
    print(guarana()+'SEJA BEM VINDO AO JOGO DA FORCA!\n')
    tempo_de_pausa(1)

    print('NESTE VOCÊ TERÁ QUE ACERTAR 5 PALAVRAS PARA PASSAR DE FASE.\n')
    tempo_de_pausa(1)

    print('VOCÊ PODE INSERIR A PALAVRA INTEIRA OU APENAS A LETRA QUE VOCÊ ACHA!\n')
    tempo_de_pausa(1)

    print('VOCÊ TERÁ 7 CHANCES DE ACERTAR A PALAVRA!\n')
    tempo_de_pausa(1)

    print('SÓ LEMBRANDO QUE PODE HAVER REPETIÇÃO DE PALAVRAS\n\nTODAS ELAS SÃO RELACIONADAS AO PYTHON!\n')
    tempo_de_pausa(1)

    print('BOM JOGO!'+apaga())

    while True:       
        palavra_secreta = obter_palavra_aleatoria()
        letras_permitidas = []
        vidas = 6
        renderizar_vida_do_jogador(vidas)
        renderizar_palavra_secreta(palavra_secreta)
        

            
        while True:
            
            if vidas==0:
                    print(apaga()+vermelho()+'VOCÊ PERDEU'+apaga())
                    break
            
            print(azul())
            palpite, tipo = reconhecer_entrada(palavra_secreta)

            
            if tipo == 'palavra':

                if palpite == palavra_secreta:
                    print(apaga()+verde()+'PARABÉNS, VOCÊ GANHOU!'+apaga())
                    contador_de_vitorias+=1
                    break
                else:
                    vidas -= 1
                    print(apaga()+vermelho()+'VOCÊ ERROU!'+apaga())
                    renderizar_vida_do_jogador(vidas)
                    
                    
                    

            elif tipo == 'char':

                if palpite[0] in palavra_secreta:
                    letras_permitidas.append(palpite[0])
                    renderizar_palavra_secreta(palavra_secreta, letras_permitidas)
                else:
                    vidas -= 1
                    print(apaga()+vermelho()+'LETRA NÃO INCLUSA'+apaga())
                    renderizar_vida_do_jogador(vidas)
                    
                
                if palavra_secreta_adivinhada(palavra_secreta, letras_permitidas):
                    print(apaga()+verde()+'PARABÉNS, VOCÊ VENCEU!'+apaga())
                    contador_de_vitorias+=1
                    break


        if contador_de_vitorias==5:
            break

    print(verde()+'PARABÉNS! VOCÊ ZEROU O JOGO!'+apaga())

