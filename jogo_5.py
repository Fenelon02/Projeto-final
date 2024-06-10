from funcoes_jogo_forca import *
from cores import * 


def jogo_quinta_fase(): 
           
    palavra_secreta = obter_palavra_aleatoria()
    letras_permitidas = []
    vidas = 6
    renderizar_vida_do_jogador(vidas)
    renderizar_palavra_secreta(palavra_secreta)
    

    while True:
        print(palavra_secreta)
        palpite, tipo = reconhecer_entrada(palavra_secreta)
        
        if tipo == 'palavra':
            if palpite == palavra_secreta:
                print('PARABÉNS, VOCÊ GANHOU!')
                break
            else:
                vidas -= 1
                print('VOCÊ ERROU!')
                renderizar_vida_do_jogador(vidas)
            if vidas==0:
                print('VOCÊ PERDEU')
                
                

        elif tipo == 'char':
            if palpite[0] in palavra_secreta:
                letras_permitidas.append(palpite[0])
                renderizar_palavra_secreta(palavra_secreta, letras_permitidas)
            else:
                vidas -= 1
                print('LETRA NÃO INCLUSA')
                renderizar_vida_do_jogador(vidas)
            
            if palavra_secreta_adivinhada(palavra_secreta, letras_permitidas):
                print('PARABÉNS, VOCÊ VENCEU!')
                break

            if vidas==0:
                print('VOCÊ PERDEU')
                
        

jogo_quinta_fase()