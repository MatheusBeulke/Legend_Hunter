def atributos():
    while True:
        print('[0] Mostrar Atributos')
        print('[1] Melhorar Atributos')
        print('[C] Voltar')
        while True:
            tecla = str(input('Tecla: ')).strip().upper()
            if tecla in '01C':
                break
            else:
                print('\033[31mErro:  \033[mOpção inválida, tente novamente')

        if tecla in 'C':
            break

        elif tecla in '0':
            lvatack = Busca('Atack', 'Atributos', 'one')
            lvdefese = Busca('Defese', 'Atributos', 'one')
            print(f'Atack: {lvatack[0]}')
            print(f'Defesa: {lvdefese[0]}')

        elif tecla in '1':
            Pontos = Busca('Pontos', 'Jogador', 'one')
            qtdepontos = Pontos[0] - 1
            print(f'Quantidade de pontos: {int(qtdepontos)}')
            print(f'[0] Atack = 1 ponto')
            print(f'[1] Defesa = 1 ponto')
            print(f'[C] Voltar')
            while True:
                tecla1 = str(input('Tecla: ')).strip().upper()
                if tecla1 in '01C':
                    break
                else:
                    print('\033[31mErro:  \033[mOpção inválida, tente novamente')

            if tecla1 in 'C':
                pass

            elif qtdepontos >= 1:
                custo = int(qtdepontos)
                Update('Jogador', 'Pontos', custo, Pontos[0])

                # atack
                if tecla1 in '0':
                    qtdeatack = Busca('Atack', 'Atributos', 'one')
                    aumento = int(qtdeatack[0]) + 1
                    Update('Atributos', 'Atack', aumento, Pontos[0])

                # defesa
                elif tecla1 in '1':
                    qtdedefese = Busca('Defese', 'Atributos', 'one')
                    aumento = int(qtdedefese[0]) + 1
                    Update('Atributos', 'Defese', aumento, Pontos[0])

            else:
                print('\033[33mErro: \033[mPontos insuficiente.')
