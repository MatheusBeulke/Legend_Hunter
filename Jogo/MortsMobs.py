import sqlite3
import BDP


def Mortesmobs():
    for num, local in enumerate(BDP.locais):
        kill = Busca('Morte', local, 'all')
        for pos, morte in enumerate(kill):
            for qtde in morte:
                qtde -= 1
                if BDP.mobs[num][pos][0] in ['Peixes', 'Pedras', 'Madeiras']:
                    pass

                else:
                    if qtde > 0:
                        print(f'{BDP.mobs[num][pos][0]} = {qtde}')


def mortemob(locais, indanimal, nomeanimal, tecla1, dinheiroanimal, expanimal, NomeJogador, Nomepet):
    # Jogador mata Mob

    morte = Busca('Morte', locais, 'all')
    morte = morte[indanimal][0]
    kill = morte + 1
    UpdateNome(locais, 'Morte', kill, nomeanimal)

    dinheiro = Busca('Dinheiro', 'Jogador', 'one')
    ganhodinheiro = dinheiro[0] + dinheiroanimal
    Update('Jogador', 'Dinheiro', ganhodinheiro, dinheiro[0])
    print(f'{NomeJogador[0]} ganhou {dinheiroanimal} moedas')
    dinheiro = Busca('Dinheiro', 'Jogador', 'one')
    print(f'{NomeJogador[0]} tem {dinheiro[0] - 1} moedas')
    sleep(5)

    exp = Busca('QtdeExp', 'Jogador', 'one')
    ganhoexp = exp[0] + expanimal
    Update('Jogador', 'QtdeExp', ganhoexp, exp[0])
    print(f'{NomeJogador[0]} ganhou {expanimal} experiências')
    totalexp = Busca('Exp', 'Jogador', 'one')
    print(f'{NomeJogador[0]} tem {ganhoexp - 1}/{totalexp[0]} experiência')
    sleep(5)

    # Drop Fragmentos
    chancedrop = randint(1, 100)
    if nomeanimal in 'Bear':
        chancecouro = randint(1, 100)
        if chancecouro <= 25:
            qtdecouro = Busca('Couros', 'Itens', 'one')
            qtdecouro = qtdecouro[0]
            Update('Itens', 'Couros', qtdecouro + 1, qtdecouro)
            print('Você ganhou 1 couro')
            sleep(3)

    if chancedrop <= 5:
        fragmentos = Busca(BDP.fragmentos[tecla1], 'Fragmentos', 'all')

        ganhofragmento = fragmentos[0][0] + 1
        Update('Fragmentos', BDP.fragmentos[tecla1], ganhofragmento, fragmentos)
        print(f'Você ganhou 1 {BDP.Fragmentos[tecla1]}')
        sleep(3)
    print('-=' * 10)
    LevelAnimal(locais, tecla1, indanimal, nomeanimal)
    LvJogador()
    if Nomepet[0] in '':
        pass
    else:
        LvPet(expanimal)
