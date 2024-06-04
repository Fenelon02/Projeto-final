from cores import *
def personagem_1():


    #printar o personagem na fase 0, o personagem inicial.

    desenho=[
        "     _____     ",
        "   /       \\   ",
        "  /  o   o  \\  ",
        " /     ^     \\ ",
        " \\   \\___/   / ",
        "  \\_________/  ",
        "   /       \\   ",
        "  /         \\  ",
        " /           \\ ",
        "/             \\",
        "\\             /",
        " \\___________/ "
    ]


    for linha in desenho: 
        print(marrom(),linha.center(30),apaga())