import numpy as np

while True:
    print("MENU: ")
    print("Escolha: [1] para jogar ou [0] para sair: ")
    resposta = int(input())
    if (resposta == 0):
        print("Fim do Jogo.")
        break
    elif (resposta != 1):
        print("Erro. Escolha de novo")
    else:
        segredo = np.random.randint(1, 101, 1)
        # print(f"Segredo: {segredo[0]}") - Para deixar o segredo amostra
    tentativas = 0
    cont = 1
    while tentativas < 7:
        resp1 = int(input(f'{cont}º tentativa: '))
        tentativas += 1
        cont += 1
        if resp1 != segredo:
            print('-------------------------------------------------------------------------------------')
            print(f'{cont - 1}º tentativa errada! vamos para a próxima tentativa\nAntes te daremos uma dica')
            if resp1 > segredo:
                print(f'Dica {cont - 1} - O segredo é um número menor que o chutado {resp1}')
                print('-------------------------------------------------------------------------------------')
            else:
                print(f'Dica {cont - 1} - O segredo é um número maior que o chutado {resp1}')
                print('-------------------------------------------------------------------------------------')

        else:
            print('-------------------------------------------------------------------------------------')
            print(f'Parabéeeeeeens! Você acertou na {tentativas}º tentativas')
            print('-------------------------------------------------------------------------------------')
            break