from random import randint


def render_player_life(life=0):

    states_of_life=[
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
    print(states_of_life[life])
        

def render_secret_word(word='',allowed_chars=[]):

    for letra in word:
        is_letra_allowed=False

        for character in allowed_chars:
            if letra==character:
                is_letra_allowed=True

        if is_letra_allowed:
            print(letra,end='')
        else:
            print('_',end='')
    print()
    

def get_random_word():
    choice_word=randint(0,3)
    palavra=['frango','piru','pinico','banana']

    choiced_word=palavra[choice_word]

    return choiced_word


def recognize_input(word_of_the_machine=''):

    word_of_the_player=input('Digite seu palpite: ').lower()

    if len(word_of_the_player)==len(word_of_the_machine):
        return (word_of_the_player, 'word')  
    else:
        return (word_of_the_player,'char')





secreate_word=get_random_word()

allowerd_chars=[]
life=6
render_player_life(life)
render_secret_word(secreate_word)
while True:
    word,type=recognize_input(secreate_word)
    
    if type=='word':
        if word==secreate_word:
            print('PARABÉNS VC GANHOU!')
            break
        else:
            life-=1
            print('VOCEÊ ERROU!')
            render_player_life(life)

    else:
        allowerd_chars.append(word[0])
        render_secret_word(secreate_word,allowerd_chars)
        
    




























































