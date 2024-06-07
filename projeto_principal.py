from personagens.personagem_inicial import personagem_1
from cores import *
from time import sleep as tempo_de_pausa
from personagens.personagem_fase_1 import personagem_fase_1




# CABEÇÁRIO INICIAL

print(azul()+'=-'*20)
print('SEJA BEM VINDO!'.center(40))
print('=-'*20+apaga())

tempo_de_pausa(1)
print(vermelho(),'Atualmente, este é o seu personagem, na fase estagiário!'.center(30),apaga())
tempo_de_pausa(1)

personagem_1()

tempo_de_pausa(1)


# NOMEAR O PERSONAGEM

nome_do_personagem=input(azul()+'Qual nome você deseja colocar em seu personagem? '+apaga())
nome_do_personagem=nome_do_personagem.title().strip()

tempo_de_pausa(1)

print(azul()+f'Olá {nome_do_personagem}, que nome lindo!\n'+apaga())


# APRESENTAÇÃO DAS REGRAS
tempo_de_pausa(1)


print(ciano()+f'Bem, {nome_do_personagem}, vou te falar mais sobre o jogo.\n')

tempo_de_pausa(2)

print('Neste jogo, seu boneco avança de fase de acordo com suas conquistas\nque serão adquiridas ao desenrolar de sua jornada.\n')

tempo_de_pausa(1.2)

print('Detalhe importante, seu personagem sente fome!\nÉ possível comprar alimentos para ele.\n')

tempo_de_pausa(1)
print('Você consegue saldo para comprar alimentos avançando as fases, que lhe aparecerão.\nSendo questionários, jogos, entre outras coisas.\n')

tempo_de_pausa(1)
print('AAHH, e já ia esqueçendo, seu personagem muda de skin de acordo com sua fase!\n')

tempo_de_pausa(1)

print('Dito isso, bom jogo para você!\n'+apaga())

# FASE 1

prosseguir=str(input(azul()+'Bem, após esta introdução, vamos ao primeiro jogo?\n[S] para continuar\n[N] para parar\n'+apaga()))
prosseguir=prosseguir.lower().strip()[0]


    # INSERIR UM VALOR VÁLIDO
while prosseguir not in 'sn':
    prosseguir=str(input(azul()+'ERRO! VALOR INVÁLIDO!\n[S] para continuar\n[N] para parar\n'+apaga()))
    prosseguir=prosseguir.lower().strip()[0]

    if prosseguir in 'sn':
        prosseguir=prosseguir
        break
     

while True:
    
    if prosseguir=='s':
        print(ciano()+'Que legal que você escolheu jogar a primeira fase!')
        print('Aqui estão as regras do jogo, que é um...')
        
        tempo_de_pausa(1)
        print('JOKENPO!!!')
        
        tempo_de_pausa(1)
        print('PEDRA PERDE DO PAPEL\n\nPEDRA GANHA DA TESOURA\n\nPAPEL PERDE DA TESOURA\n\nPAPEL GANHA DA PEDRA\n\nTESOURA GANHA DO PAPEL\n\nTESOURA PERDE DA PEDRA\n')
        
        tempo_de_pausa(1)
        print('CASO A O JOGADOR E O COMPUTADOR JOGUEM O MESMO ÍTEM, GERA UM EMPATE\n')
        
        tempo_de_pausa(1)
        print('O JOGADOR VENCE QUANDO O JOGADOR GANHAR 5 PARTIDAS')

        tempo_de_pausa(2)
        break
    else: 
        break

from jogo_1 import jogo_1
if prosseguir=='s':
    jogo_1()



confirmar=''

while prosseguir=='n':
        
    confirmar=input(azul()+'Tem certeza que deseja acabar o jogo?\n[S] para continuar\n[N] para parar\n')
    confirmar=confirmar.lower().strip()[0]


    # DIGITAR UM VALOR VÁLIDO
    while confirmar not in 'sn':
        confirmar=str(input(azul()+'ERRO! VALOR INVÁLIDO!\n[S] para continuar\n[N] para parar\n'+apaga()))
        confirmar=confirmar.lower().strip()[0]

        if confirmar in 'sn':
            confirmar=confirmar
            break

    if confirmar=='n':
            break


    elif confirmar=='s':
        jogo_1()
        print(apaga()+magenta()+'Parabéns! Você consegiu passar esta fase! Vamos a próxima!\n')
        print('Com isso, recebeu um saldo de 50 moedas!\n'+apaga())
        break


contador=0
        

# INÍCIO DA SEGUNDA FASE

saldo=50
print('Você é um campeão! Parabéns por chegar a fase 2!\n')

print(f'Dito isso, você acaba de desbloquear uma nova skin!\nO {nome_do_personagem} dev iniciante!'+apaga())

tempo_de_pausa(1)
personagem_fase_1()

print(azul(),'Legal né? Bem, a segunda fase é um jogo da velha!')

tempo_de_pausa(1)
# print(f'Serão 10 perguntas, com resposta em A,B,C,D')

tempo_de_pausa(1)
print('Mas antes,me alimente por favor, estou com fome!')


# COMPRAR COMIDAS
from comidas import comidas_a_comprar

tempo_de_pausa(1)
saldo=comidas_a_comprar(saldo)
print(apaga())

# INÍCIO DA FASE 2

print(magenta()+'Feito isso, vamos a fase 2 do seu jogo!'+apaga())
tempo_de_pausa(1)
from jogo_2 import jogo_2
jogo_2()


# FASE 3
from personagens.personagem_fase_2 import *
saldo+=100
print(magenta()+'Após este longa jogada, bem vindo á fase 3!')

print('Esta jornada especial lhe rendeu um saldo de mais 100 moedas!')

tempo_de_pausa(1)

print(f'Dito isso, você acaba de desbloquear uma nova skin!\nO {nome_do_personagem} dev júnior!'+apaga())

personagem_fase_2()

tempo_de_pausa(1)
print(azul()+'Mas antes de começarmos a fase 3,me alimente por favor, estou com fome!')


# COMPRAR COMIDAS

tempo_de_pausa(1)
saldo=comidas_a_comprar(saldo)
print(apaga())
tempo_de_pausa(1)

# INÍCIO OFC DA FASE 3

from jogo_3 import jogo_terceira_fase

jogo_terceira_fase()


# FASE 4
saldo+=70
print(magenta()+'Após testar seus conhecimentos em python na fase 3, bem vindo a fase 4!')

print('Esta jornada lhe rendeu 70 moedas.\n')

tempo_de_pausa(1)

print(f'Dito isso, você acaba de desbloquear uma nova skin!\nO {nome_do_personagem} dev pleno!'+apaga())

from personagens.personagem_fase_3 import *

personagem_fase_3()

# ALIMENTAÇÃO
tempo_de_pausa(1)
print(azul()+'Mas antes de começarmos a fase 4,me alimente por favor, estou com fome!')


# COMPRAR COMIDAS

tempo_de_pausa(1)
saldo=comidas_a_comprar(saldo)
print(apaga())
tempo_de_pausa(1)

# JOGO 4 EM SI

from jogo_4 import jogo_quarta_fase

jogo_quarta_fase()

# FASE 5

saldo+=110
print(magenta()+'Após esta jornada matemática,seja-bem-vinda fase 5!\nNossa última fase!')

print('Esta jornada lhe rendeu 110 moedas.\n')

tempo_de_pausa(1)

print(f'Dito isso, você acaba de desbloquear uma nova skin!\nO {nome_do_personagem} dev sênior!'+apaga())

from personagens.personagem_fase_4 import *

personagem_fase_4()

# ALIMENTAÇÃO
tempo_de_pausa(1)
print(azul()+'Mas antes de começarmos a fase 4,me alimente por favor, estou com fome!')


# COMPRAR COMIDAS

tempo_de_pausa(1)
saldo=comidas_a_comprar(saldo)
print(apaga())
tempo_de_pausa(1)





