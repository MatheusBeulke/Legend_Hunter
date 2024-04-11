from time import sleep


def habilidades():
    while True:
        print('[0] Mostrar Habilidades')
        print('[1] Melhorar Habilidades')
        print('[C] Voltar')
        while True:
            tecla = str(input('Tecla: ')).strip().upper()
            if tecla in '01C':
                break
            else:
                print('\033[31mErro:  \033[mOpção inválida, tente novamente')

        lvatack = Busca('Atack', 'Habilidades', 'one')
        lvdefese = Busca('Defese', 'Habilidades', 'one')

        if tecla in 'C':
            break

        elif tecla in '0':
            print(f'Atacak: {lvatack[0]}')
            print(f'Defesa: {lvdefese[0]}')

        elif tecla in '1':
            tempoatack = Busca('TempoAtack', 'Habilidades', 'one')
            tempodefese = Busca('TempoDefese', 'Habilidades', 'one')

            print('Treinar:')
            print(f'[0] Atacak = {tempoatack[0]} segundos')
            print(f'[1] Defesa = {tempodefese[0]} segundos')
            print('[C] Voltar')
            while True:
                tecla1 = str(input('Tecla: ')).strip().upper()
                if tecla1 in '01C':
                    break
                else:
                    print('\033[31mErro:  \033[mOpção inválida, tente novamente')
            if tecla1 in 'C':
                pass

            elif tecla1 in '0':
                for i in range(tempoatack[0], -1, -1):
                    mnts = tempoatack[0] - 1
                    print(f'\r{tempoatack[0]}', end='')
                    if tempoatack[0] == 0:
                        uplvatack = lvatack[0] + 1
                        Update('Habilidades', 'Atack', uplvatack, lvatack[0])
                        qtdeuptempo = uplvatack * 60
                        Update('Habilidades', 'TempoAtack', qtdeuptempo, mnts)
                        break
                    Update('Habilidades', 'TempoAtack', mnts, tempoatack[0])
                    sleep(1)
                print('\nVocê upou sua habilidade de atack')

            elif tecla1 in '1':
                for i in range(tempodefese[0], -1, -1):
                    tempodefese = Busca('TempoDefese', 'Habilidades', 'one')
                    mnts = tempodefese[0] - 1
                    print(f'\r{tempodefese[0]}', end='')
                    if tempodefese[0] == 0:
                        uplvdefese = lvdefese[0] + 1
                        Update('TempoDefese', 'Defese', uplvdefese, lvdefese[0])
                        qtdeuptempo = uplvdefese * 60
                        Update('Habilidades', 'TempoDefese', qtdeuptempo, mnts)
                        break
                    Update('Habilidades', 'TempoDefese', mnts, tempodefese[0])
                    sleep(1)
                print('\nVocê upou sua habilidade de defese')
