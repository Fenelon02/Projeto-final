def comidas_a_comprar(saldo=0):

    comidas=[
        {'comida': 'bolo', 'preco': 10},
        {'comida': 'pizza', 'preco': 8},
        {'comida': 'refrigerante', 'preco': 5},
        {'comida': 'sanduiche', 'preco': 20},
        {'comida': 'sorvete', 'preco': 3},
        {'comida': 'hamburguer', 'preco': 35},
        {'comida': 'batata frita', 'preco': 13},
        {'comida': 'sushi', 'preco': 2},
        {'comida': 'cafe', 'preco': 1},
        {'comida': 'salada', 'preco': 110}
    ]
    for posicao,alimento in enumerate(comidas):
        
        print(f'N{posicao+1} {alimento}')


    valor=int(input('Digite a posição do ítem desejado:\n[999]-Para não comprar nada\n'))
    while True:
        if valor==999:
            print('Penalidade de -10 pontos em seu saldo.')
            saldo-=10
            print(f'Seu saldo atual é de {saldo} moedas.\n')
            print('Que pena, estava com fome.')
            break
            

        elif saldo-comidas[valor-1]['preco']>0 or saldo-comidas[valor-1]['preco']==0:
            saldo=saldo-comidas[valor-1]['preco']
            print(f'Você comprou um(a) {comidas[valor-1]['comida']}, que lhe custou {comidas[valor-1]['preco']} moedas, sobrando {saldo} moedas de saldo\n')
            print('Estou alimentado! Obrigado')
            break
            

        else:
            print('SALDO INSUFICIENTE! ESCOLHA UM ÍTEM MAIS BARATO!')
            valor=int(input('Digite a posição do ítem desejado:\n[999]-Para não comprar nada\n'))

    return saldo