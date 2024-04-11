import BDP
import sqlite3
from time import sleep


def LvJogador():
    while True:
        QtdeExp = Busca('QtdeExp', 'Jogador', 'one')
        EXP = Busca('EXP', 'Jogador', 'one')
        if QtdeExp[0] >= EXP[0]:
            Lv = Busca('Level', 'Jogador', 'one')
            uplv = Lv[0] + 1
            Update('Jogador', 'Level', uplv, Lv[0])
            upexp = EXP[0] * 2
            Update('Jogador', 'EXP', upexp, EXP)

            Vida = Busca('Vida', 'Jogador', 'one')
            HP = Busca('HP', 'Jogador', 'one')
            uphp = HP[0] + 10
            Update('Jogador', 'HP', uphp, HP[0])
            HP = Busca('HP', 'Jogador', 'one')
            Update('Jogador', 'Vida', HP[0], Vida[0])

            Mana = Busca('Mana', 'Jogador', 'one')
            Qtdemana = Busca('QtdeMana', 'Jogador', 'one')
            upqtdemana = Qtdemana[0] + 10
            Update('Jogador', 'QtdeMana', upqtdemana, Qtdemana[0])
            Qtdemana = Busca('QtdeMana', 'Jogador', 'one')
            Update('Jogador', 'Mana', Qtdemana[0], Mana[0])

            diamante = Busca('Diamante', 'Jogador', 'one')
            ganhodiamante = diamante[0] + uplv
            Update('Jogador', 'Diamante', ganhodiamante, diamante[0])

            pontos = Busca('Pontos', 'Jogador', 'one')
            ganhopontos = pontos[0] + 1
            Update('Jogador', 'Pontos', ganhopontos, pontos[0])

            print(f'Up Lv.{uplv}')
            sleep(1)
            print(f'Você ganhou {uplv} diamantes')
            print('Você ganhou 1 pontos de atributos')
            sleep(1)
        else:
            break


def LevelAnimal(locais, tecla1, indanimal, nomeanimal):
    qtde = Busca('Morte', locais, 'all')
    qtde = qtde[indanimal][0] - 1
    LvAnimal = 0
    lvanimal = Busca('Level', locais, 'all')
    lvanimal = lvanimal[indanimal][0]

    if qtde % 50 == 0:
        LvAnimal = qtde / 50
        LvAnimal += BDP.mobs[tecla1][indanimal][1]

    while True:
        if LvAnimal > lvanimal:
            if LvAnimal > BDP.mobs[tecla1][indanimal][1] + 10:
                pass

            else:
                UpdateNome(locais, 'level', LvAnimal, nomeanimal)

                hpanimal = Busca('HP', locais, 'all')
                hpanimal = hpanimal[tecla1][indanimal][0]
                ganhohp = hpanimal + 1
                UpdateNome(locais, 'HP', ganhohp, nomeanimal)

                danoanimal = Busca('Dano', locais, 'all')
                danoanimal = danoanimal[indanimal][0]
                ganhodano = danoanimal + 1
                UpdateNome(locais, 'Dano', ganhodano, nomeanimal)

                expanimal = Busca('Exp', locais, 'all')
                expanimal = expanimal[indanimal][0]

                ganhoexp = expanimal + 1
                UpdateNome(locais, 'Exp', ganhoexp, nomeanimal)

                dinheiroanimal = Busca('Dinheiro', locais, 'all')
                dinheiroanimal = dinheiroanimal[indanimal][0]
                ganhodinheiro = dinheiroanimal + 1
                UpdateNome(locais, 'Dinheiro', ganhodinheiro, nomeanimal)
        break


def LvPet(expanimal):
    Nomepet = Busca('Nome', 'PetsJogador', 'one')
    lvpet = Busca('Level', 'PetsJogador', 'one')
    qtdeexp = Busca('QtdeExp', 'Pets', 'one')
    exppet = Busca('Exp', 'Pets', 'one')
    ganhoexp = (exppet[0] - 1) + expanimal
    UpdateNome('Pets', 'Exp', ganhoexp, Nomepet[0])
    while True:
        if exppet[0] - 1 >= qtdeexp[0]:
            UpdateNome('Pets', 'Level', lvpet[0] + 1, Nomepet[0])
            lvpet = Busca('Level', 'Pets', 'one')
            print(f'Pet Up Lv.{lvpet[0]}')
        else:
            break

    print(f'Pet ganhou {expanimal} exp')
    exppet = Busca('Exp', 'Pets', 'one')
    print(f'Pet tem {exppet[0] - 1}/{qtdeexp[0]} exp')
