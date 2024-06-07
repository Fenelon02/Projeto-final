from cores import *
def personagem_fase_1():
    personagem_primeira_fase=[
        "     _____     ",
        "   /       \\   ",
        "  /  o   o  \\  ",
        " /     ^     \\ ",
        " \\   \\___/   / ",
        "  \\_________/  ",
        "   /|     |\\   ",
        "  /_|_____|_\\  ",
        " /           \\ ",
        "/DEV INICIANTE\\",
        "\\             /",
        " \\           / ",
        "  \\_________/  "
    ]

    for linha in personagem_primeira_fase:
        print(marrom(),linha,apaga())

