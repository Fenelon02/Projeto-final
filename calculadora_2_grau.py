from cores import *
from time import sleep as tempo_de_pausa
from random import randint
  

def calculadora_segundo_grau():
    while True:
        from math import sqrt
        print(fuligem()+'CALCULAR EQUAÇÃO DE 2 GRAU'+apaga())
        print(vermelho()+'DETALHE IMPORTANTE:'+apaga(),end='')
        print(verde()+' SEMPRE ADCIONE UMA CASA DECIMAL, CASO TENHA MAIS QUE UMA CASA, ARESCENTE APENAS UMA CASA DECIMAL.'+apaga())
        a=randint(1,100)
        b=randint(-100,100)
        c=randint(-100,100)
        print(fuligem()+f'A={a} B={b} C={c}')
        tempo_de_pausa(1)
        print('\nPARA CALCULAR O DELTA=b**2-4*a*c')
        tempo_de_pausa(2)
        print('\nPARA OBTER AS RAÍZES:\nX1=(-b+sqrt(delta))/(2*a)\nX2=(-b-sqrt(delta))/(2*a)')

        delta=(b**2)-(4*a*c)


        if delta<0:
            print('DELTA NEGATIVO\nCALCULANDO NOVOS VALORES PARA A B E C...\n')
            while delta<0:
                a=randint(1,100)
                b=randint(-100,100)
                c=randint(-100,100)
                delta=(b**2)-(4*a*c)

            print(f'A={a} B={b} C={c}')

            resultado_1=(-b+sqrt(delta))/(2*a)
            resultado_1=round(resultado_1,1)
            

            resultado_2=(-b-sqrt(delta))/(2*a)
            resultado_2=round(resultado_2,1)
            

        else:
            resultado_1=(-b+sqrt(delta))/(2*a)
            resultado_1=round(resultado_1,1)
            

            resultado_2=(-b-sqrt(delta))/(2*a)
            resultado_2=round(resultado_2,1)

        tempo_de_pausa(2)
        resposta_positiva=float(input('Resposta para x1: '))

        resposta_negativa=float(input('Resposta para x2: '+apaga()))

        if resposta_negativa==resultado_2 and resposta_positiva==resultado_1:
            print(verde()+f'CORRETO! O x1 e o x2 são respectivamente {resposta_positiva} e {resposta_negativa}'+apaga())
            break

        elif resposta_positiva==resultado_1 and resposta_negativa!=resultado_2:
            print(verde()+f'X1 ESTÁ CORRETO! sua resposta é {resposta_positiva}'+apaga(),end='')
            while resposta_negativa!=resultado_2:
                print(vermelho()+f' mas a resposta do X2 está errada, não é {resposta_negativa}.'+apaga())
                resposta_negativa=float(input(fuligem()+'Resposta correta para x2: '+apaga()))

            print(verde()+f'CORRETO! O x1 e o x2 são respectivamente {resposta_positiva} e {resposta_negativa}'+apaga())
            break

        elif resposta_positiva!=resultado_1 and resposta_negativa==resultado_2:
            print(verde()+f'X2 ESTÁ CORRETO! sua resposta é {resposta_negativa}'+apaga(),end='')
            while resposta_positiva!=resultado_1:
                print(vermelho()+f' mas a resposta do X1 está errada, não é {resposta_positiva}.'+apaga())
                resposta_positiva=float(input(fuligem()+'Resposta correta para x1: '+apaga()))

            print(verde()+f'CORRETO! O x1 e o x2 são respectivamente {resposta_positiva} e {resposta_negativa}'+apaga())
            break

        else:
            while resposta_positiva!=resultado_1 and resposta_negativa!=resultado_2:
                tempo_de_pausa(1)
                print(vermelho()+'AMBOS OS RESULTADOS ESTÃO ERRADOS'+apaga())
                resposta_positiva=float(input(fuligem()+'Resposta correta para x1: '+apaga()))

                resposta_negativa=float(input(fuligem()+'Resposta correta para x2: '+apaga()))
                if resposta_negativa==resultado_2 and resposta_positiva==resultado_1:
                    print(verde()+f'CORRETO! O x1 e o x2 são respectivamente {resposta_positiva} e {resposta_negativa}'+apaga())
                    break

                elif resposta_positiva==resultado_1 and resposta_negativa!=resultado_2:
                    print(verde()+f'X1 ESTÁ CORRETO! sua resposta é {resposta_positiva}'+apaga(),end='')
                    while resposta_negativa!=resultado_2:
                        print(vermelho()+f' mas a resposta do X2 está errada, não é {resposta_negativa}.'+apaga())
                        resposta_negativa=float(input(fuligem()+'Resposta correta para x2: '+apaga()))

                    print(verde()+f'CORRETO! O x1 e o x2 são respectivamente {resposta_positiva} e {resposta_negativa}'+apaga())
                    break

                elif resposta_positiva!=resultado_1 and resposta_negativa==resultado_2:
                    print(verde()+f'X2 ESTÁ CORRETO! sua resposta é {resposta_negativa}'+apaga(),end='')
                    while resposta_positiva!=resultado_1:
                        print(vermelho()+f' mas a resposta do X1 está errada, não é {resposta_positiva}.'+apaga())
                        resposta_positiva=float(input(fuligem()+'Resposta correta para x1: '+apaga()))

                    print(verde()+f'CORRETO! O x1 e o x2 são respectivamente {resposta_positiva} e {resposta_negativa}'+apaga())
                    break
            
            break

            