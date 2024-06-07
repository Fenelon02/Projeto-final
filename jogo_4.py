from cores import *
from time import sleep as tempo_de_pausa
from random import randint

def jogo_quarta_fase():

    print(fuligem()+'\nBem vindo a sua fase 4 do jogo!')

    tempo_de_pausa(1)

    print('Nesta fase iremos testar seus conhecimemntos matemáticos em diferentes problemas.\n')

    tempo_de_pausa(1)

    print("Iremos usar os seguintes sinais:\n[+]-para adição\n[-]-para subtração\n[*]-para multiplicação\n[/]-para divisão\n[**]-para potenciação\n")

    tempo_de_pausa(1)

    print('Dito isso, bons resultados para você!')


    # DESAFIO 1
    print('Problema matemático número 1: \n')

    elemento_1=randint(1,10)
    elemento_2=randint(1,10)

    resultado=elemento_1+elemento_2

    print(f'{elemento_1}+{elemento_2}=?')  

    tempo_de_pausa(1)

    resposta=int(input('Digite o resultado: '+apaga())) 

    if resposta==resultado:
        print(verde()+f'CORRETO! a operação {elemento_1}+{elemento_2} tem como resposta {resultado}'+apaga()) 

    else:
        while resultado!=resposta:
            resposta=int(input(vermelho()+'RESPOSTA ERRADA! Digite o resultado: '+apaga())) 

            if resposta==resultado:
                print(verde()+f'CORRETO! a operação {elemento_1}+{elemento_2} tem como resposta {resultado}'+apaga()) 
    

    # DESAFIO 2
    tempo_de_pausa(1)
    print(fuligem()+'\nProblema matemático 2')
    elemento_1=randint(1,10)
    elemento_2=randint(1,10)
    elemento_3=randint(1,10)

    resultado=elemento_1+elemento_2-elemento_3

    print(f'{elemento_1}+{elemento_2}-{elemento_3}=?') 

    resposta=int(input('Digite o resultado: '+apaga())) 

    if resposta==resultado:
        print(verde()+f'CORRETO! a operação {elemento_1}+{elemento_2}-{elemento_3} tem como resposta {resultado}'+apaga()) 

    else:
        while resultado!=resposta:
            resposta=int(input(vermelho()+'RESPOSTA ERRADA! Digite o resultado: '+apaga())) 

            if resposta==resultado:
                print(verde()+f'CORRETO! a operação {elemento_1}+{elemento_2}-{elemento_3} tem como resposta {resultado}'+apaga()) 


    # DESAFIO 3

    tempo_de_pausa(1)
    print(fuligem()+'\nDesafio matemático 3')

    elemento_1=randint(1,10)
    elemento_2=randint(1,10)
    elemento_3=randint(1,10)
    elemento_4=randint(1,15)

    resultado=elemento_1-elemento_2+(elemento_3*elemento_4)

    print(f'{elemento_1}-{elemento_2}+({elemento_3}*{elemento_4})=?') 

    resposta=int(input('Digite o resultado: '+apaga())) 

    if resposta==resultado:
        print(verde()+f'CORRETO! a operação {elemento_1}-{elemento_2}+({elemento_3}*{elemento_4}) tem como resposta {resultado}'+apaga()) 

    else:
        while resultado!=resposta:
            resposta=int(input(vermelho()+'RESPOSTA ERRADA! Digite o resultado: '+apaga())) 

            if resposta==resultado:
                print(verde()+f'CORRETO! a operação {elemento_1}-{elemento_2}+({elemento_3}*{elemento_4}) tem como resposta {resultado}'+apaga())


    # DESAFIO 4

    tempo_de_pausa(1)
    print(fuligem()+'\nDesafio matemático 4',apaga())
    print(vermelho()+'DETALHE IMPORTANTE:'+apaga(),end='')
    print(verde()+' SEMPRE ADCIONE UMA CASA DECIMAL, CASO TENHA MAIS QUE UMA CASA, ARESCENTE APENAS UMA CASA DECIMAL.'+apaga())
    tempo_de_pausa(1)
    print(fuligem()+'Em alguns casos, os números são arredondados,ex: 2.28->2.3')

    elemento_1=randint(1,10)
    elemento_2=randint(1,10)
    elemento_3=randint(1,10)
    elemento_4=randint(1,15)
    elemento_5=randint(1,10)

    resultado=(elemento_1-elemento_2+(elemento_3*elemento_4))/elemento_5
    resultado=(f'{resultado:.1f}')
    resultado=float(resultado)
        
    print(f'({elemento_1}-{elemento_2}+({elemento_3}*{elemento_4}))/{elemento_5}=?') 

    resposta=float(input('Digite o resultado: '+apaga()))

    if resposta==resultado:
        print(verde()+f'CORRETO! a operação ({elemento_1}-{elemento_2}+({elemento_3}*{elemento_4}))/{elemento_5} tem como resposta {resultado}'+apaga()) 

    else:
        while resultado!=resposta:
            resposta=float(input(vermelho()+'RESPOSTA ERRADA! Digite o resultado: '+apaga())) 

            if round(resposta,1)==resultado:
                print(verde()+f'CORRETO! a operação ({elemento_1}-{elemento_2}+({elemento_3}*{elemento_4}))/{elemento_5} tem como resposta {resultado}'+apaga())

    # DESAFIO 5

    from calculadora_2_grau import calculadora_segundo_grau
    
    calculadora_segundo_grau()
    

    print(verde()+'PARABÉNS! VOCÊ CHEGOU AO FIM DA PENULTIMA FASE!'+apaga())
     


jogo_quarta_fase()