# Código desenvolvido em parceria com (@github) Lucas-BRT

from random import randint
from cores import *

def renderizar_vida_do_jogador(vidas = 0):
    estados_de_vida = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
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
           |   |
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
               |
               |
               |
               |
        ---------
        """
    ]
    print(ciano()+estados_de_vida[vidas]+apaga())

def renderizar_palavra_secreta(palavra='', letras_permitidas=[]):
    for letra in palavra:
        letra_permitida = False
        for caracter in letras_permitidas:
            if letra == caracter:
                letra_permitida = True
        if letra_permitida:
            print(letra, end='')
        else:
            print('_', end='')
    print()

def obter_palavra_aleatoria():
    indice_palavra = randint(0, 3)
    palavras = ["data","result","value","item","index","count","temp","name","while","elif"]
    palavra_escolhida = palavras[indice_palavra]
    return palavra_escolhida

def reconhecer_entrada(palavra_da_maquina=''):
    palavra_do_jogador = input('Digite seu palpite: ').lower()
    if len(palavra_do_jogador) == len(palavra_da_maquina):
        return (palavra_do_jogador, 'palavra')  
    else:
        return (palavra_do_jogador, 'char')

def palavra_secreta_adivinhada(palavra_secreta='', letras_permitidas=[]):
    for char in palavra_secreta:
        if not char in letras_permitidas:
            return False
    return True

