from time import sleep
from random import randint
from math import trunc
import sqlite3
import BDP


def Connecte():
    log = 0
    banco = sqlite3.connect('Banco_Dados.db')
    cursor = banco.cursor()
    if log == 0:
        CriandoBD(cursor, banco)
    else:
        inicio()


def CriandoBD(cursor, banco):
    # Jogador
    cursor.execute('CREATE TABLE Jogador (Nome text, Level integer, HP integer, Vida integer, QtdeExp integer,'
                   'EXP integer, Dinheiro integer, Diamante integer, Pontos integer)')

    while True:
        nome = str(input('Nome: ')).strip()
        if nome in '':
            print('Campo Vázio')
        else:
            print('Conta Criado com sucesso!')
            break

    cursor.execute("INSERT INTO Jogador VALUES('" + nome + "', 1, 100, 100, 1, 100, 1, 1, 1)")

    # Bolsa
    cursor.execute('CREATE TABLE Bolsa (PoçãoPequena integer, PoçãoMédia integer, PoçãoGrande integer,'
                   'PoçãoGigante integer, HiperPoção integer, PoçãoMagica integer)')

    cursor.execute("INSERT INTO Bolsa VALUES(11, 1, 1, 1, 1, 1)")

    # MobsColinaVerde
    cursor.execute('CREATE TABLE MobsColinaVerde (Nome text, Level integer, HP integer, Dano integer,'
                   ' DanoElementar integer, Exp integer, Dinheiro integer, Morte integer)')

    #                                                 Nome,   Lv,  HP, D, DF, E, D, M
    cursor.execute("INSERT INTO MobsColinaVerde VALUES('Rats', 1,  12, 7 , 2, 5, 3, 1)")
    cursor.execute("INSERT INTO MobsColinaVerde VALUES('Crow', 15,  40, 25, 4, 17, 15, 1)")
    cursor.execute("INSERT INTO MobsColinaVerde VALUES('Wolf', 30,  70, 47, 6, 34, 29, 1)")
    cursor.execute("INSERT INTO MobsColinaVerde VALUES('Lizard', 45,  102, 71, 8, 53, 45, 1)")
    cursor.execute("INSERT INTO MobsColinaVerde VALUES('Slime' , 60,  136, 97, 10, 74, 63, 1)")
    cursor.execute("INSERT INTO MobsColinaVerde VALUES('Assasin', 75,  172, 125, 12, 97, 83, 1)")
    cursor.execute("INSERT INTO MobsColinaVerde VALUES('Bear', 90,  210, 155, 14, 122, 105, 1)")
    cursor.execute("INSERT INTO MobsColinaVerde VALUES('Goblin', 105,  250, 187, 16, 149, 129, 1)")
    cursor.execute("INSERT INTO MobsColinaVerde VALUES('Minotaur', 120,  292, 221, 18, 178, 155, 1)")

    # Deserto
    cursor.execute('CREATE TABLE MobsDeserto (Nome text, Level integer, HP integer, Dano integer,'
                   ' DanoElementar integer, Exp integer, Dinheiro integer, Morte integer)')

    #                                               Nome,    Lv,   HP,  D, DF   E,   D,  M
    cursor.execute("INSERT INTO MobsDeserto VALUES('Scorpion', 135, 350, 300, 24, 230, 200, 1)")
    cursor.execute("INSERT INTO MobsDeserto VALUES('Snake', 150, 378, 320, 26, 245, 212, 1)")
    cursor.execute("INSERT INTO MobsDeserto VALUES('Worm', 165, 408, 342, 28, 262, 226, 1)")
    cursor.execute("INSERT INTO MobsDeserto VALUES('Scarab', 180, 440, 366, 30, 281, 242, 1)")
    cursor.execute("INSERT INTO MobsDeserto VALUES('Cactus', 195, 474, 392, 32, 302, 260, 1)")
    cursor.execute("INSERT INTO MobsDeserto VALUES('Raptor', 210, 510, 420, 34, 325, 280, 1)")
    cursor.execute("INSERT INTO MobsDeserto VALUES('Mummy', 225, 548, 450, 36, 350, 302, 1)")
    cursor.execute("INSERT INTO MobsDeserto VALUES('Pharao', 240, 588, 482, 38, 377, 326, 1)")
    cursor.execute("INSERT INTO MobsDeserto VALUES('Anubis', 255, 630, 516, 40, 406, 352, 1)")
    cursor.execute("INSERT INTO MobsDeserto VALUES('Sandstone Golem', 270, 674, 552, 42, 437, 380, 1)")

    # Caverna de Minerção
    cursor.execute('CREATE TABLE MobsCavernaMinerção (Nome text, Level integer, HP integer, Dano integer,'
                   ' DanoElementar ingeter, Exp integer, Dinheiro integer, Morte integer)')

    #                                                       Nome,  Lv,  HP,  D, DF,  E,    D,  M
    cursor.execute("INSERT INTO MobsCavernaMinerção VALUES('Bat', 285, 700, 580, 44, 450, 400, 1)")
    cursor.execute("INSERT INTO MobsCavernaMinerção VALUES('Gigantula', 300, 728, 600, 46, 465, 412, 1)")
    cursor.execute("INSERT INTO MobsCavernaMinerção VALUES('Dwarf', 315, 758, 622, 48, 482, 426, 1)")
    cursor.execute("INSERT INTO MobsCavernaMinerção VALUES('Miner', 330, 790, 646, 50, 501, 442, 1)")
    cursor.execute("INSERT INTO MobsCavernaMinerção VALUES('Troll', 345, 824, 672, 52, 522, 460, 1)")
    cursor.execute("INSERT INTO MobsCavernaMinerção VALUES('Orc', 360, 850, 700, 54, 545, 480, 1)")
    cursor.execute("INSERT INTO MobsCavernaMinerção VALUES('Djinn', 375, 888, 730, 56, 570, 502, 1)")
    cursor.execute("INSERT INTO MobsCavernaMinerção VALUES('Ciclops', 390, 948, 762, 58, 597, 526, 1)")

    # Floresta Sombria
    cursor.execute('CREATE TABLE MobsFlorestaSombria (Nome text, Level integer, HP integer, Dano integer,'
                   ' DanoElementar integer, Exp integer, Dinheiro integer, Morte integer)')

    #                                                       Nome,      Lv,   HP,  D, DF,  E,    D,  M
    cursor.execute("INSERT INTO MobsFlorestaSombria VALUES('Skeleton', 405, 986, 804, 60, 626, 549, 1)")
    cursor.execute("INSERT INTO MobsFlorestaSombria VALUES('Zombie', 420, 1014, 824, 62, 641, 561, 1)")
    cursor.execute("INSERT INTO MobsFlorestaSombria VALUES('Ghost', 435, 1044, 846, 64, 658, 575, 1)")
    cursor.execute("INSERT INTO MobsFlorestaSombria VALUES('Witch', 450, 1076, 870, 66, 677, 591, 1)")
    cursor.execute("INSERT INTO MobsFlorestaSombria VALUES('Lich', 465, 1110, 896, 68, 698, 609, 1)")
    cursor.execute("INSERT INTO MobsFlorestaSombria VALUES('Shandow', 480, 1146, 924, 70, 721, 629, 1)")
    cursor.execute("INSERT INTO MobsFlorestaSombria VALUES('Phanton Flame', 495, 1184, 954, 72, 746, 651, 1)")
    cursor.execute("INSERT INTO MobsFlorestaSombria VALUES('Phanton Fiend', 510, 1224, 986, 74, 773, 675, 1)")
    cursor.execute("INSERT INTO MobsFlorestaSombria VALUES('Skeleton Dragon', 525, 1266, 1020, 76, 802, 701, 1)")
    cursor.execute("INSERT INTO MobsFlorestaSombria VALUES('Gargoyle', 540, 1310, 1056, 78, 833, 729, 1)")
    cursor.execute("INSERT INTO MobsFlorestaSombria VALUES('Spectral Flame', 555, 1356, 1094, 80, 866, 759, 1)")
    cursor.execute("INSERT INTO MobsFlorestaSombria VALUES('Spcetral Fiend', 570, 1404, 1134, 82, 901, 791, 1)")
    cursor.execute("INSERT INTO MobsFlorestaSombria VALUES('Vampire', 585, 1454, 1176, 84, 938, 825, 1)")

    # Icy
    cursor.execute('CREATE TABLE MobsIcy (Nome text, Level integer, HP integer, Dano integer, DanoElementar integer,'
                   ' Exp integer, Dinheiro integer, Morte integer)')

    #                                            Nome,      Lv,   HP,   D,  DF    E,   D,  M
    cursor.execute("INSERT INTO MobsIcy VALUES('Icy Flame', 600, 1500, 1200, 86, 970, 850, 1)")
    cursor.execute("INSERT INTO MobsIcy VALUES('Snow Golem', 615, 1528, 1220, 88, 985, 862, 1)")
    cursor.execute("INSERT INTO MobsIcy VALUES('Mammoth', 630, 1558, 1242, 90, 1002, 876, 1)")
    cursor.execute("INSERT INTO MobsIcy VALUES('Yeti', 645, 1590, 1266, 92, 1021, 892, 1)")
    cursor.execute("INSERT INTO MobsIcy VALUES('Icy Wizard', 660, 1624, 1292, 94, 1042, 910, 1)")
    cursor.execute("INSERT INTO MobsIcy VALUES('Icy Dragon', 675, 1660, 1320, 96, 1065, 930, 1)")
    cursor.execute("INSERT INTO MobsIcy VALUES('Icy Fiend', 690, 1698, 1350, 98, 1090, 952, 1)")

    # Eletrico
    cursor.execute('CREATE TABLE MobsElectric (Nome text, Level integer, HP integer, Dano integer,'
                   'DanoElementar integer, Exp integer, Dinheiro integer, Morte integer)')

    #                                                  Nome,           Lv,  HP,   D,  DF,   E,  D,  M
    cursor.execute("INSERT INTO MobsElectric VALUES('Electric Flame', 705, 1750, 1400, 100, 1150, 1000, 1)")
    cursor.execute("INSERT INTO MobsElectric VALUES('Electric Golem', 720, 1778, 1420, 102, 1165, 1012, 1)")
    cursor.execute("INSERT INTO MobsElectric VALUES('Electric Yeti', 735, 1808, 1442, 104, 1182, 1026, 1)")
    cursor.execute("INSERT INTO MobsElectric VALUES('Electric Wizard', 750, 1840, 1466, 106, 1201, 1042, 1)")
    cursor.execute("INSERT INTO MobsElectric VALUES('Electric Dragon', 765, 1874, 1492, 108, 1222, 1060, 1)")
    cursor.execute("INSERT INTO MobsElectric VALUES('Electric Fiend', 780, 1910, 1520, 110, 1245, 1080, 1)")

    # Fogo
    cursor.execute('CREATE TABLE MobsFire (Nome text, Level integer, HP integer, Dano integer,'
                   'DanoElementar integer, Exp integer, Dinheiro integer, Morte integer)')

    #                                            Nome,   Lv,  HP,   D,    DF,  E,    D,    M
    cursor.execute("INSERT INTO MobsFire VALUES('Flame', 795, 1960, 1580, 112, 1270, 1100, 1)")
    cursor.execute("INSERT INTO MobsFire VALUES('Fire Golem', 810, 1988, 1600, 114, 1285, 1112, 1)")
    cursor.execute("INSERT INTO MobsFire VALUES('Wizard', 825, 2018, 1622, 116, 1302, 1126, 1)")
    cursor.execute("INSERT INTO MobsFire VALUES('Dragon', 840, 2050, 1646, 118, 1321, 1142, 1)")
    cursor.execute("INSERT INTO MobsFire VALUES('Demon', 855, 2084, 1672, 120, 1342, 1160, 1)")

    # Fragmentos
    cursor.execute('CREATE TABLE Fragmentos (FragmentoHit integer, FragmentoAr integer, FragmentoPsiquico integer,'
                   'FragmentoAlma integer, FragmentoGelo integer, FragmentoEletrico integer, FragmentoFogo integer)')
    cursor.execute("INSERT INTO Fragmentos VALUES(1, 1, 1, 1, 1, 1, 1)")

    # Atributos
    cursor.execute('CREATE TABLE Atributos (Defese integer, Atack integer )')
    cursor.execute("INSERT INTO Atributos VALUES(1, 4)")

    # Skill
    cursor.execute('CREATE TABLE Habilidades (Defese integer, TempoDefese integer, Atack integer, TempoAtack integer)')
    cursor.execute("INSERT INTO Habilidades VALUES(1, 60, 1, 60)")

    banco.commit()
    inicio()


def inicio():
    banco = sqlite3.connect('Banco_Dados.db')
    cursor = banco.cursor()
    while True:
        print('Funções de controle:')
        print('[A] Jogar')
        print('[B] Informações')
        print('[C] Loja')
        while True:
            tecla = str(input('Tecla: ')).upper().strip()
            if tecla in 'ABC':
                break
            else:
                print('\033[31mErro:  \033[mOpção inválida, tente novamente')

        if tecla in 'A':
            print('MAPA:')
            for pos, i in enumerate(BDP.nmapa):
                print(f'[{pos}] {BDP.mapa[pos]}')
            print('[C] Voltar')
            while True:
                tecla1 = str(input('Tecla: ')).strip().upper()
                if tecla1 in BDP.nmapa or tecla1 in 'C':
                    break
                else:
                    print('\033[31mErro:  \033[mOpção inválida, tente novamente')

            if tecla1 in 'C':
                pass
            else:
                mapa = BDP.mapa[int(tecla1)]
                Mapa(mapa)

        elif tecla in 'B':
            while True:
                print('Informações:')
                print('[0] Personagem')
                print('[1] Atributos')
                print('[2] Habilidades')
                print('[3] Proteção Elementar')
                print('[4] Mochila')
                print('[5] Quantidade de mob matado')
                print('[C] Voltar')
                while True:
                    tecla1 = str(input('Tecla: ')).strip().upper()
                    if tecla1 in '012345C':
                        break
                    else:
                        print('\033[31mErro:  \033[mOpção inválida, tente novamente')
                if tecla1 in 'C':
                    break

                elif tecla1 in '0':
                    cursor.execute('SELECT Nome FROM Jogador')
                    Nome = cursor.fetchone()
                    print(f'Nome: {Nome[0]}')
                    cursor.execute('SELECT Level FROM Jogador')
                    Level = cursor.fetchone()
                    print(f'Level: {Level[0]}')
                    cursor.execute('SELECT QtdeExp FROM Jogador')
                    exp = cursor.fetchone()
                    cursor.execute('SELECT EXP FROM Jogador')
                    totalexp = cursor.fetchone()
                    print(f'Exp: {exp[0] - 1}/{totalexp[0]}')
                    cursor.execute('SELECT Dinheiro FROM Jogador')
                    dinheiro = cursor.fetchone()
                    print(f'Dinheiro: {int(dinheiro[0]) - 1}')
                    cursor.execute('SELECT Diamante FROM Jogador')
                    diamante = cursor.fetchone()
                    print(f'Diamante: {int(diamante[0]) - 1}')
                    sleep(2)

                elif tecla1 in '1':
                    atributos()

                elif tecla1 in '2':
                    habilidades()

                elif tecla1 in '3':
                    print('Quantidade de Fragmentos:')
                    cursor.execute('''SELECT * FROM Fragmentos''')
                    Fragmentos = cursor.fetchall()
                    for pos, i in enumerate(Fragmentos):
                        fragmentos = Fragmentos[0][pos] - 1
                        if fragmentos >= 1:
                            print(f'{i} = {fragmentos}')
                    sleep(1)

                elif tecla1 in '4':
                    print('Mochila:')
                    Bolsa = cursor.execute('''SELECT * FROM Bolsa''')
                    for itens in Bolsa:
                        for pos, Qtde in enumerate(itens):
                            Qtde -= 1
                            if Qtde > 0:
                                print(f'{BDP.Loja[pos][0]} = {Qtde}')
                    sleep(2)

                elif tecla1 in '5':
                    print('Quantidade de Mobs matados:')
                    sleep(1)
                    Mortesmobs()

        elif tecla in 'C':
            loja()


def Mapa(mapa):
    banco = sqlite3.connect('Banco_Dados.db')
    cursor = banco.cursor()
    while True:
        cursor.execute('SELECT HP FROM Jogador')
        HP = cursor.fetchone()
        cursor.execute('SELECT Vida FROM Jogador')
        Vida = cursor.fetchone()

        if BDP.mortejogador == 1:
            BDP.mortejogador = 0
            cursor.execute("UPDATE Jogador SET Vida = '" + str(HP[0]) + "' WHERE '" + str(Vida[0]) + "'")
            banco.commit()
            break
        print('Mobs:')

        if mapa in 'Colina Verde':
            for pos, i in enumerate(BDP.mobscolinaverde):
                print(f'[{pos}] {BDP.mobscolinaverde[pos][0]}')

        elif mapa in 'Deserto':
            for pos, i in enumerate(BDP.mobsdeseto):
                print(f'[{pos}] {BDP.mobsdeseto[pos][0]}')

        elif mapa in 'Caverna de Mineração':
            for pos, i in enumerate(BDP.mobscarvenaminer):
                print(f'[{pos}] {BDP.mobscarvenaminer[pos][0]}')

        elif mapa in 'Floresta Sombria':
            for pos, i in enumerate(BDP.mobsflorestasombria):
                print(f'[{pos}] {BDP.mobsflorestasombria[pos][0]}')

        elif mapa in 'Polo Norte':
            for pos, i in enumerate(BDP.mobsicy):
                print(f'[{pos}] {BDP.mobsicy[pos][0]}')

        elif mapa in 'Eletrico':
            for pos, i in enumerate(BDP.mobselectric):
                print(f'[{pos}] {BDP.mobselectric[pos][0]}')

        elif mapa in 'Vulcão':
            for pos, i in enumerate(BDP.mobsfire):
                print(f'[{pos}] {BDP.mobsfire[pos][0]}')

        print('[C] Voltar')
        while True:
            tecla2 = str(input('Tecla: ')).strip().upper()
            if tecla2 in '':
                print('\033[31mErro:  \033[mOpção inválida, tente novamente')

            elif mapa in 'Colina Verde':
                if tecla2 in BDP.nmobscolinaverde or tecla2 in 'C':
                    break
                else:
                    print('\033[31mErro:  \033[mOpção inválida, tente novamente')

            elif mapa in 'Deserto':
                if tecla2 in BDP.nmobsdeserto or tecla2 in 'C':
                    break
                else:
                    print('\033[31mErro:  \033[mOpção inválida, tente novamente')

            elif mapa in 'Caverna de Mineração':
                if tecla2 in BDP.nmobscavernaminer or tecla2 in 'C':
                    break
                else:
                    print('\033[31mErro:  \033[mOpção inválida, tente novamente')

            elif mapa in 'Floresta Sombria':
                if tecla2 in BDP.nmobsflorestasombria or tecla2 in 'C':
                    break
                else:
                    print('\033[31mErro:  \033[mOpção inválida, tente novamente')

            elif mapa in 'Polo Norte':
                if tecla2 in BDP.nmobsicy or tecla2 in 'C':
                    break
                else:
                    print('\033[31mErro:  \033[mOpção inválida, tente novamente')

            elif mapa in 'Eletrico':
                if tecla2 in BDP.nmobselectric or tecla2 in 'C':
                    break
                else:
                    print('\033[31mErro:  \033[mOpção inválida, tente novamente')

            elif mapa in 'Vulcão':
                if tecla2 in BDP.nmobsfire or tecla2 in 'C':
                    break
                else:
                    print('\033[31mErro:  \033[mOpção inválida, tente novamente')

        if tecla2 in 'C':
            break

        indanimal, lvanimal, HPanimal, Danoanimal, expanimal, dinheiroanimal, nomeanimal, Lvjogador = \
            infobatalha(mapa, tecla2)

        print(f'Você encontrou um(a): {nomeanimal}')
        sleep(3)
        print('-=' * 20)

        cursor.execute('SELECT Defese FROM Atributos')
        da = cursor.fetchone()
        cursor.execute('SELECT Defese FROM Habilidades')
        dh = cursor.fetchone()
        defesa = da[0] + dh[0]

        print(f'Mob: {nomeanimal} Lv.{lvanimal:.0f} \nHP: {HPanimal} \nDano: {Danoanimal - defesa}'
              f' \nDinheiro: {dinheiroanimal} \nExp: {expanimal}')
        print('-=' * 20)
        sleep(3)

        cursor.execute('SELECT Atack FROM Atributos')
        aa = cursor.fetchone()
        cursor.execute('SELECT Atack FROM Habilidades')
        ah = cursor.fetchone()
        atack = aa[0] + ah[0]

        cursor.execute('SELECT Nome FROM Jogador')
        nomejogador = cursor.fetchone()
        print(f'Jogador: {nomejogador[0]} Lv.{Lvjogador}\nHP: {Vida[0]}/{HP[0]}'
              f' \nDano: {atack - 4}-{atack}\nDefesa: {defesa}')
        print('-=' * 20)
        sleep(3)
        while True:
            print('[0] Atacar')
            print('[1] Recuar')
            print('[2] Recuperar vida')
            tecla3 = str(input('Tecla: ')).strip()
            if tecla3 in '01':
                break

            elif tecla3 in '2':
                RecuperarHP()

            else:
                print('\033[31mErro:  \033[mOpção inválida, tente novamente')

        if tecla3 in '0':
            while True:
                atacar = str(input('Looping de quantas vezes (Máximo 10 vezes): ')).strip()
                numero = atacar.isnumeric()
                ebool = str(numero)
                fimd = ebool.find('True')

                if fimd == 0:
                    atacar = int(atacar)
                    if atacar > 10 or atacar < 1:
                        print('\033[31mErro:  \033[mQuantidade não possivel')
                    else:
                        break
                else:
                    print('\033[31mErro:  \033[mOpção inválida, tente novamente')

            for i in range(1, atacar + 1):
                if i > 1:
                    print(f'Você encontrou outro(a) {nomeanimal}')
                    sleep(2)
                batalha(indanimal, nomeanimal, HPanimal, Danoanimal, dinheiroanimal, expanimal, mapa,
                        atack, defesa, HP)
                indanimal, lvanimal, HPanimal, Danoanimal, expanimal, dinheiroanimal, nomeanimal, Lvjogador = (
                    infobatalha(mapa, tecla2))

                if BDP.mortejogador == 1:
                    break

        elif tecla3 in '1':
            pass


def batalha(indanimal, nomeanimal, HPanimal, Danoanimal, dinheiroanimal, expanimal, mapa, atack, defese, HP):
    banco = sqlite3.connect('Banco_Dados.db')
    cursor = banco.cursor()

    Vidaanimal = HPanimal
    minimo = atack - 4
    while True:
        jogadoratack = randint(minimo, atack)
        print('-=' * 10)
        print('Jogador: \033[31m{}\033[m de atack'.format(jogadoratack))
        HPanimal -= jogadoratack

        if HPanimal <= 0:
            print('Jogador matou um(a): {}'.format(nomeanimal))
            sleep(2)
            if mapa in 'Colina Verde':
                cursor.execute('SELECT Morte FROM MobsColinaVerde')
                morte = cursor.fetchall()
                morte = morte[indanimal][0]
                kill = morte + 1
                cursor.execute("UPDATE MobsColinaVerde SET Morte = '" + str(kill) + "' WHERE Nome = '" + str(
                    nomeanimal) + "'")

            elif mapa in 'Deserto':
                cursor.execute('SELECT Morte FROM MobsDeserto')
                morte = cursor.fetchall()
                morte = morte[indanimal][0]
                kill = morte + 1
                cursor.execute(
                    "UPDATE MobsDeserto SET Morte = '" + str(kill) + "' WHERE Nome = '" + str(nomeanimal) + "'")

            elif mapa in 'Caverna de Mineração':
                cursor.execute('SELECT Morte FROM MobsCavernaMinerção')
                morte = cursor.fetchall()
                morte = morte[indanimal][0]
                kill = morte + 1
                cursor.execute("UPDATE MobsCavernaMinerção SET Morte ="
                               " '" + str(kill) + "' WHERE Nome = '" + str(nomeanimal) + "'")

            elif mapa in 'Floresta Sombria':
                cursor.execute('SELECT Morte FROM MobsFlorestaSombria')
                morte = cursor.fetchall()
                morte = morte[indanimal][0]
                kill = morte + 1
                cursor.execute("UPDATE MobsFlorestaSombria SET Morte ="
                               "'" + str(kill) + "' WHERE Nome = '" + str(nomeanimal) + "'")

            elif mapa in 'Polo Norte':
                cursor.execute('SELECT Morte FROM MobsIcy')
                morte = cursor.fetchall()
                morte = morte[indanimal][0]
                kill = morte + 1
                cursor.execute("UPDATE MobsIcy SET Morte = '" + str(kill) + "' WHERE Nome = '" + str(nomeanimal) + "'")

            elif mapa in 'Eletrico':
                cursor.execute('SELECT Morte FROM MobsElectric')
                morte = cursor.fetchall()
                morte = morte[indanimal][0]
                kill = morte + 1
                cursor.execute(
                    "UPDATE MobsElectric SET Morte = '" + str(kill) + "' WHERE Nome = '" + str(nomeanimal) + "'")

            banco.commit()
            cursor.execute('SELECT Dinheiro FROM Jogador')
            dinheiro = cursor.fetchone()
            ganhodinheiro = dinheiro[0] + dinheiroanimal
            cursor.execute(
                "UPDATE Jogador SET Dinheiro = '" + str(ganhodinheiro) + "' WHERE '" + str(dinheiro[0]) + "'")
            print(f'Jogador ganhou {dinheiroanimal} moedas')
            cursor.execute('SELECT Dinheiro FROM Jogador')
            dinheiro = cursor.fetchone()
            print(f'Jogador tem {dinheiro[0] - 1} moedas')
            sleep(2)

            cursor.execute('SELECT QtdeExp FROM Jogador')
            exp = cursor.fetchone()
            ganhoexp = exp[0] + expanimal
            cursor.execute("UPDATE Jogador SET QtdeExp = '" + str(ganhoexp) + "' WHERE '" + str(exp[0]) + "'")
            print(f'Jogador ganhou {expanimal} experiências')
            cursor.execute('SELECT Exp FROM Jogador')
            totalexp = cursor.fetchone()
            print(f'Jogador tem {ganhoexp - 1}/{totalexp[0]} experiência')
            banco.commit()
            sleep(2)
            print('-=' * 10)
            chancedrop = randint(1, 100)
            if mapa in 'Colina Verde':
                if chancedrop <= 5:
                    cursor.execute('SELECT FragmentoHit FROM Fragmentos')
                    fragmentos = cursor.fetchone()
                    fragmentos = fragmentos[0]
                    ganhofragmento = fragmentos + 1
                    cursor.execute("UPDATE Fragmentos SET FragmentoHit = '" + str(ganhofragmento) + "' WHERE '" + str(
                        fragmentos) + "'")
                    print('Você ganhou 1 Fragmento de Hit')
                    sleep(1)
                    banco.commit()

                LevelanimalColinaVerde(indanimal, nomeanimal)

            elif mapa in 'Deserto':
                if chancedrop <= 5:
                    cursor.execute('SELECT FragmentoAr FROM Fragmentos')
                    fragmentos = cursor.fetchone()
                    fragmentos = fragmentos[indanimal]
                    ganhofragmento = fragmentos + 1
                    cursor.execute("UPDATE Fragmentos SET FragmentoAr = '" + str(ganhofragmento) + "' WHERE '" + str(
                        fragmentos) + "'")
                    print('Você ganhou 1 Fragmento de Ar')
                    sleep(1)
                    banco.commit()
                LevelanimalDeserto(indanimal, nomeanimal)

            elif mapa in 'Caverna de Mineração':
                if chancedrop <= 5:
                    cursor.execute('SELECT FragmentoPsiquico FROM Fragmentos')
                    fragmentos = cursor.fetchone()
                    fragmentos = fragmentos[indanimal]
                    ganhofragmento = fragmentos + 1
                    cursor.execute("UPDATE Fragmentos SET FragmentoPsiquico = '" + str(ganhofragmento) + "' WHERE '" +
                                   str(fragmentos) + "'")
                    print('Você ganhou 1 Fragmento de Psíquico')
                    sleep(1)
                LevelanimalCavernaminer(indanimal, nomeanimal)

            elif mapa in 'Floresta Sombria':
                if chancedrop <= 5:
                    cursor.execute('SELECT FragmentoAlma FROM Fragmentos')
                    fragmentos = cursor.fetchone()
                    fragmentos = fragmentos[indanimal]
                    ganhofragmento = fragmentos + 1
                    cursor.execute("UPDATE Fragmentos SET FragmentoAlma = '" + str(ganhofragmento) + "' WHERE '" + str(
                        fragmentos) + "'")
                    print('Você ganhou 1 Fragmento de Alma')
                    sleep(1)
                    banco.commit()
                LevelanimalFlorestasombria(indanimal, nomeanimal)

            elif mapa in 'Polo Norte':
                if chancedrop <= 5:
                    cursor.execute('SELECT FragmentoGelo FROM Fragmentos')
                    fragmentos = cursor.fetchone()
                    fragmentos = fragmentos[indanimal]
                    ganhofragmento = fragmentos + 1
                    cursor.execute("UPDATE Fragmentos SET FragmentoGelo = '" + str(ganhofragmento) + "' WHERE '" + str(
                        fragmentos) + "'")
                    print('Você ganhou 1 Fragmento de Gelo')
                    sleep(1)
                    banco.commit()
                LevelanimalIcy(indanimal, nomeanimal)

            elif mapa in 'Eletrico':
                if chancedrop <= 5:
                    cursor.execute('SELECT FragmentoEletrico FROM Fragmentos')
                    fragmentos = cursor.fetchone()
                    fragmentos = fragmentos[indanimal]
                    ganhofragmento = fragmentos + 1
                    cursor.execute("UPDATE Fragmentos SET FragmentoEletrico = '" + str(ganhofragmento) + "' WHERE '" +
                                   str(fragmentos) + "'")
                    print('Você ganhou 1 Fragmento de Choque')
                    sleep(1)
                    banco.commit()
                LevelanimalElectric(indanimal, nomeanimal)

            elif mapa in 'Vulcão':
                if chancedrop <= 5:
                    cursor.execute('SELECT FragmentoFogo FROM Fragmentos')
                    fragmentos = cursor.fetchone()
                    fragmentos = fragmentos[indanimal]
                    ganhofragmento = fragmentos + 1
                    cursor.execute("UPDATE Fragmentos SET FragmentoFogo = '" + str(ganhofragmento) + "' WHERE '" +
                                   str(fragmentos) + "'")
                    print('Você ganhou 1 Fragmento de Fogo')
                    sleep(1)
                    banco.commit()
                LevelanimalVulcao(indanimal, nomeanimal)

            LvJogador()
            break

        print(f'{nomeanimal}: {HPanimal}/{Vidaanimal}HP')
        print('-=' * 10)
        sleep(5)
        if defese < Danoanimal:
            atackanimal = Danoanimal - defese
        else:
            atackanimal = 0

        cursor.execute('SELECT Vida FROM Jogador')
        Vida = cursor.fetchone()
        vida = Vida[0] - atackanimal
        cursor.execute("UPDATE Jogador SET Vida = '" + str(vida) + "' WHERE '" + str(Vida[0]) + "' ")
        print('{}: \033[32m{}\033[m de atack'.format(nomeanimal, atackanimal))
        if vida <= 0:
            print(f'{nomeanimal} matou Jogador')
            sleep(5)
            BDP.mortejogador = 1
            banco.commit()
            break
        print(f'Jogador: {vida}/{HP[0]}')
        print('-=' * 10)
        sleep(5)
        banco.commit()


def atributos():
    banco = sqlite3.connect('Banco_Dados.db')
    cursor = banco.cursor()
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
            cursor.execute('SELECT Atack FROM Atributos')
            lvatack = cursor.fetchone()
            cursor.execute('SELECT Defese FROM Atributos')
            lvdefese = cursor.fetchone()
            print(f'Atack: {lvatack[0]}')
            print(f'Defesa: {lvdefese[0]}')

        elif tecla in '1':
            cursor.execute('SELECT Pontos FROM Jogador')
            Pontos = cursor.fetchone()
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
                cursor.execute("UPDATE Jogador SET Pontos = '" + str(custo) + "' WHERE '" + str(Pontos[0]) + "'")

                # atack
                if tecla1 in '0':
                    cursor.execute('SELECT Atack FROM Atributos')
                    qtdeatack = cursor.fetchone()
                    aumento = int(qtdeatack[0]) + 1
                    cursor.execute("UPDATE Atributos SET Atack = '" + str(aumento) + "' WHERE '" + str(Pontos[0]) + "'")
                    banco.commit()

                # defesa
                elif tecla1 in '1':
                    cursor.execute('SELECT Defese FROM Atributos')
                    qtdedefese = cursor.fetchone()
                    aumento = int(qtdedefese[0]) + 1
                    cursor.execute(
                        "UPDATE Atributos SET Defese = '" + str(aumento) + "' WHERE '" + str(Pontos[0]) + "'")
                    banco.commit()

            else:
                print('\033[33mErro: \033[mPontos insuficiente.')


def habilidades():
    banco = sqlite3.connect('Banco_Dados.db')
    cursor = banco.cursor()
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

        cursor.execute('SELECT Atack FROM Habilidades')
        lvatack = cursor.fetchone()
        cursor.execute('SELECT Defese FROM Habilidades')
        lvdefese = cursor.fetchone()

        if tecla in 'C':
            break

        elif tecla in '0':
            print(f'Atacak: {lvatack[0]}')
            print(f'Defesa: {lvdefese[0]}')

        elif tecla in '1':
            cursor.execute('SELECT TempoAtack FROM Habilidades')
            tempoatack = cursor.fetchone()
            cursor.execute('SELECT TempoDefese FROM Habilidades')
            tempodefese = cursor.fetchone()

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
                    cursor.execute('SELECT TempoAtack FROM Habilidades')
                    tempoatack = cursor.fetchone()
                    mnts = tempoatack[0] - 1
                    print(f'\r{tempoatack[0]}', end='')
                    if tempoatack[0] == 0:
                        uplvatack = lvatack[0] + 1
                        cursor.execute("UPDATE Habilidades SET Atack = '" + str(uplvatack) + "' WHERE '" + str(
                            lvatack[0]) + "'")
                        qtdeuptempo = uplvatack * 60
                        cursor.execute("UPDATE Habilidades SET TempoAtack = '" + str(qtdeuptempo) + "' WHERE '" + str(
                            mnts) + "'")
                        banco.commit()

                        break
                    cursor.execute(
                        "UPDATE Habilidades SET TempoAtack = '" + str(mnts) + "' WHERE '" + str(tempoatack[0]) + "'")
                    banco.commit()
                    sleep(1)

                print('\nVocê upou sua habilidade de atack')

            elif tecla1 in '1':
                for i in range(tempodefese[0], -1, -1):
                    cursor.execute('SELECT TempoDefese FROM Habilidades')
                    tempodefese = cursor.fetchone()
                    mnts = tempodefese[0] - 1
                    print(f'\r{tempodefese[0]}', end='')
                    if tempodefese[0] == 0:
                        uplvdefese = lvdefese[0] + 1
                        cursor.execute("UPDATE Habilidades SET Defese = '" + str(uplvdefese) + "' WHERE '" + str(
                            lvdefese[0]) + "'")
                        qtdeuptempo = uplvdefese * 60
                        cursor.execute("UPDATE Habilidades SET TempoDefese = '" + str(qtdeuptempo) + "' WHERE '" + str(
                            mnts) + "'")
                        banco.commit()

                        break
                    cursor.execute(
                        "UPDATE Habilidades SET TempoDefese = '" + str(mnts) + "' WHERE '" + str(tempodefese[0]) + "'")
                    banco.commit()
                    sleep(1)
                print('\nVocê upou sua habilidade de defese')


def infobatalha(mapa, tecla2):
    banco = sqlite3.connect('Banco_Dados.db')
    cursor = banco.cursor()

    if mapa in 'Colina Verde':
        indanimal = int(tecla2)
        cursor.execute('SELECT Nome FROM MobsColinaVerde')
        nomeanimal = cursor.fetchall()
        nomeanimal = nomeanimal[indanimal][0]

        cursor.execute('SELECT Level FROM MobsColinaVerde')
        lvanimal = cursor.fetchall()
        lvanimal = lvanimal[indanimal][0]

        cursor.execute('SELECT HP FROM MobsColinaVerde')
        hpanimal = cursor.fetchall()
        hpanimal = hpanimal[indanimal][0]

        cursor.execute('SELECT Dano FROM MobsColinaVerde')
        danoanimal = cursor.fetchall()
        danoanimal = danoanimal[indanimal][0]

        cursor.execute('SELECT Level FROM Jogador')
        Lvjogador = cursor.fetchone()
        Lvjogador = Lvjogador[0]

        cursor.execute('SELECT DanoElementar FROM MobsColinaVerde')
        danoelementar = cursor.fetchall()
        danoelementar = danoelementar[indanimal][0]

        cursor.execute('SELECT * FROM Fragmentos')
        defesaelementar = cursor.fetchall()
        defesaelementar = defesaelementar[0][indanimal] - 1

        diferencaelementar = danoelementar - defesaelementar
        if diferencaelementar < 0:
            diferencaelementar = 0
        diferencalv = lvanimal - Lvjogador
        HPanimal = hpanimal
        Danoanimal = danoanimal + diferencaelementar
        if Lvjogador >= lvanimal or diferencalv <= 0:
            pass
        else:
            HPanimal = hpanimal + diferencalv
            Danoanimal = danoanimal + diferencalv + diferencaelementar

        cursor.execute('SELECT Exp FROM MobsColinaVerde')
        expanimal = cursor.fetchall()
        expanimal = expanimal[indanimal][0]

        cursor.execute('SELECT Dinheiro FROM MobsColinaVerde')
        dinheiroanimal = cursor.fetchall()
        dinheiroanimal = dinheiroanimal[indanimal][0]
        return indanimal, lvanimal, HPanimal, Danoanimal, expanimal, dinheiroanimal, nomeanimal, Lvjogador

    elif mapa in 'Deserto':
        indanimal = int(tecla2)
        cursor.execute('SELECT Nome FROM MobsDeserto')
        nomeanimal = cursor.fetchall()
        nomeanimal = nomeanimal[indanimal][0]

        cursor.execute('SELECT Level FROM MobsDeserto')
        lvanimal = cursor.fetchall()
        lvanimal = lvanimal[indanimal][0]

        cursor.execute('SELECT HP FROM MobsDeserto')
        hpanimal = cursor.fetchall()
        hpanimal = hpanimal[indanimal][0]

        cursor.execute('SELECT Dano FROM MobsDeserto')
        danoanimal = cursor.fetchall()
        danoanimal = danoanimal[indanimal][0]

        cursor.execute('SELECT Level FROM Jogador')
        Lvjogador = cursor.fetchone()
        Lvjogador = Lvjogador[0]

        cursor.execute('SELECT DanoElementar FROM MobsDeserto')
        danoelementar = cursor.fetchall()
        danoelementar = danoelementar[indanimal][0]

        cursor.execute('SELECT * FROM Fragmentos')
        defesaelementar = cursor.fetchall()
        defesaelementar = defesaelementar[0][indanimal] - 1

        diferencaelementar = danoelementar - defesaelementar
        if diferencaelementar < 0:
            diferencaelementar = 0

        diferencalv = lvanimal - Lvjogador
        HPanimal = hpanimal
        Danoanimal = danoanimal + diferencaelementar
        if Lvjogador >= lvanimal or diferencalv <= 0:
            pass
        else:
            HPanimal = hpanimal + diferencalv
            Danoanimal = danoanimal + diferencalv + diferencaelementar

        cursor.execute('SELECT Exp FROM MobsDeserto')
        expanimal = cursor.fetchall()
        expanimal = expanimal[indanimal][0]

        cursor.execute('SELECT Dinheiro FROM MobsDeserto')
        dinheiroanimal = cursor.fetchall()
        dinheiroanimal = dinheiroanimal[indanimal][0]
        return indanimal, lvanimal, HPanimal, Danoanimal, expanimal, dinheiroanimal, nomeanimal, Lvjogador

    elif mapa in 'Caverna de Mineração':
        indanimal = int(tecla2)
        cursor.execute('SELECT Nome FROM MobsCavernaMinerção')
        nomeanimal = cursor.fetchall()
        nomeanimal = nomeanimal[indanimal][0]

        cursor.execute('SELECT Level FROM MobsCavernaMinerção')
        lvanimal = cursor.fetchall()
        lvanimal = lvanimal[indanimal][0]

        cursor.execute('SELECT HP FROM MobsCavernaMinerção')
        hpanimal = cursor.fetchall()
        hpanimal = hpanimal[indanimal][0]

        cursor.execute('SELECT Dano FROM MobsCavernaMinerção')
        danoanimal = cursor.fetchall()
        danoanimal = danoanimal[indanimal][0]

        cursor.execute('SELECT Level FROM Jogador')
        Lvjogador = cursor.fetchone()
        Lvjogador = Lvjogador[0]

        cursor.execute('SELECT DanoElementar FROM MobsCavernaMinerção')
        danoelementar = cursor.fetchall()
        danoelementar = danoelementar[indanimal][0]

        cursor.execute('SELECT * FROM Fragmentos')
        defesaelementar = cursor.fetchall()
        defesaelementar = defesaelementar[0][indanimal]

        diferencaelementar = danoelementar - defesaelementar
        if diferencaelementar < 0:
            diferencaelementar = 0

        diferencalv = lvanimal - Lvjogador
        HPanimal = hpanimal
        Danoanimal = danoanimal + diferencaelementar
        if Lvjogador >= lvanimal or diferencalv <= 0:
            pass
        else:
            HPanimal = hpanimal + diferencalv
            Danoanimal = danoanimal + diferencalv + diferencaelementar

        cursor.execute('SELECT Exp FROM MobsCavernaMinerção')
        expanimal = cursor.fetchall()
        expanimal = expanimal[indanimal][0]

        cursor.execute('SELECT Dinheiro FROM MobsCavernaMinerção')
        dinheiroanimal = cursor.fetchall()
        dinheiroanimal = dinheiroanimal[indanimal][0]
        return indanimal, lvanimal, HPanimal, Danoanimal, expanimal, dinheiroanimal, nomeanimal, Lvjogador

    elif mapa in 'Floresta Sombria':
        indanimal = int(tecla2)
        cursor.execute('SELECT Nome FROM MobsFlorestaSombria')
        nomeanimal = cursor.fetchall()
        nomeanimal = nomeanimal[indanimal][0]

        cursor.execute('SELECT Level FROM MobsFlorestaSombria')
        lvanimal = cursor.fetchall()
        lvanimal = lvanimal[indanimal][0]

        cursor.execute('SELECT HP FROM MobsFlorestaSombria')
        hpanimal = cursor.fetchall()
        hpanimal = hpanimal[indanimal][0]

        cursor.execute('SELECT Dano FROM MobsFlorestaSombria')
        danoanimal = cursor.fetchall()
        danoanimal = danoanimal[indanimal][0]

        cursor.execute('SELECT Level FROM Jogador')
        Lvjogador = cursor.fetchone()
        Lvjogador = Lvjogador[0]

        cursor.execute('SELECT DanoElementar FROM MobsFlorestaSombria')
        danoelementar = cursor.fetchall()
        danoelementar = danoelementar[indanimal][0]

        cursor.execute('SELECT * FROM Fragmentos')
        defesaelementar = cursor.fetchall()
        defesaelementar = defesaelementar[0][indanimal] - 1

        diferencaelementar = danoelementar - defesaelementar
        if diferencaelementar < 0:
            diferencaelementar = 0

        diferencalv = lvanimal - Lvjogador
        HPanimal = hpanimal
        Danoanimal = danoanimal + diferencaelementar
        if Lvjogador >= lvanimal or diferencalv <= 0:
            pass
        else:
            HPanimal = hpanimal + diferencalv
            Danoanimal = danoanimal + diferencalv + diferencaelementar

        cursor.execute('SELECT Exp FROM MobsFlorestaSombria')
        expanimal = cursor.fetchall()
        expanimal = expanimal[indanimal][0]

        cursor.execute('SELECT Dinheiro FROM MobsFlorestaSombria')
        dinheiroanimal = cursor.fetchall()
        dinheiroanimal = dinheiroanimal[indanimal][0]

        return indanimal, lvanimal, HPanimal, Danoanimal, expanimal, dinheiroanimal, nomeanimal, Lvjogador

    elif mapa in 'Polo Norte':
        indanimal = int(tecla2)
        cursor.execute('SELECT Nome FROM MobsIcy')
        nomeanimal = cursor.fetchall()
        nomeanimal = nomeanimal[indanimal][0]

        cursor.execute('SELECT Level FROM MobsIcy')
        lvanimal = cursor.fetchall()
        lvanimal = lvanimal[indanimal][0]

        cursor.execute('SELECT HP FROM MobsIcy')
        hpanimal = cursor.fetchall()
        hpanimal = hpanimal[indanimal][0]

        cursor.execute('SELECT Dano FROM MobsIcy')
        danoanimal = cursor.fetchall()
        danoanimal = danoanimal[indanimal][0]

        cursor.execute('SELECT Level FROM Jogador')
        Lvjogador = cursor.fetchone()
        Lvjogador = Lvjogador[0]

        cursor.execute('SELECT DanoElementar FROM MobsIcy')
        danoelementar = cursor.fetchall()
        danoelementar = danoelementar[indanimal][0]

        cursor.execute('SELECT * FROM Fragmentos')
        defesaelementar = cursor.fetchall()
        defesaelementar = defesaelementar[0][indanimal] - 1

        diferencaelementar = danoelementar - defesaelementar
        if diferencaelementar < 0:
            diferencaelementar = 0

        diferencalv = lvanimal - Lvjogador
        HPanimal = hpanimal
        Danoanimal = danoanimal + diferencaelementar
        if Lvjogador >= lvanimal or diferencalv <= 0:
            pass
        else:
            HPanimal = hpanimal + diferencalv
            Danoanimal = danoanimal + diferencalv + diferencaelementar

        cursor.execute('SELECT Exp FROM MobsIcy')
        expanimal = cursor.fetchall()
        expanimal = expanimal[indanimal][0]

        cursor.execute('SELECT Dinheiro FROM MobsIcy')
        dinheiroanimal = cursor.fetchall()
        dinheiroanimal = dinheiroanimal[indanimal][0]
        return indanimal, lvanimal, HPanimal, Danoanimal, expanimal, dinheiroanimal, nomeanimal, Lvjogador

    elif mapa in 'Eletrico':
        indanimal = int(tecla2)
        cursor.execute('SELECT Nome FROM MobsElectric')
        nomeanimal = cursor.fetchall()
        nomeanimal = nomeanimal[indanimal][0]

        cursor.execute('SELECT Level FROM MobsElectric')
        lvanimal = cursor.fetchall()
        lvanimal = lvanimal[indanimal][0]

        cursor.execute('SELECT HP FROM MobsElectric')
        hpanimal = cursor.fetchall()
        hpanimal = hpanimal[indanimal][0]

        cursor.execute('SELECT Dano FROM MobsElectric')
        danoanimal = cursor.fetchall()
        danoanimal = danoanimal[indanimal][0]

        cursor.execute('SELECT Level FROM Jogador')
        Lvjogador = cursor.fetchone()
        Lvjogador = Lvjogador[0]

        cursor.execute('SELECT DanoElementar FROM MobsElectric')
        danoelementar = cursor.fetchall()
        danoelementar = danoelementar[indanimal][0]

        cursor.execute('SELECT * FROM Fragmentos')
        defesaelementar = cursor.fetchall()
        defesaelementar = defesaelementar[0][indanimal] - 1

        diferencaelementar = danoelementar - defesaelementar
        if diferencaelementar < 0:
            diferencaelementar = 0

        diferencalv = lvanimal - Lvjogador
        HPanimal = hpanimal
        Danoanimal = danoanimal + diferencaelementar
        if Lvjogador >= lvanimal or diferencalv <= 0:
            pass
        else:
            HPanimal = hpanimal + diferencalv
            Danoanimal = danoanimal + diferencalv + diferencaelementar

        cursor.execute('SELECT Exp FROM MobsElectric')
        expanimal = cursor.fetchall()
        expanimal = expanimal[indanimal][0]

        cursor.execute('SELECT Dinheiro FROM MobsElectric')
        dinheiroanimal = cursor.fetchall()
        dinheiroanimal = dinheiroanimal[indanimal][0]
        return indanimal, lvanimal, HPanimal, Danoanimal, expanimal, dinheiroanimal, nomeanimal, Lvjogador

    elif mapa in 'Vulcão':
        indanimal = int(tecla2)
        cursor.execute('SELECT Nome FROM MobsFire')
        nomeanimal = cursor.fetchall()
        nomeanimal = nomeanimal[indanimal][0]

        cursor.execute('SELECT Level FROM MobsFire')
        lvanimal = cursor.fetchall()
        lvanimal = lvanimal[indanimal][0]

        cursor.execute('SELECT HP FROM MobsFire')
        hpanimal = cursor.fetchall()
        hpanimal = hpanimal[indanimal][0]

        cursor.execute('SELECT Dano FROM MobsFire')
        danoanimal = cursor.fetchall()
        danoanimal = danoanimal[indanimal][0]

        cursor.execute('SELECT Level FROM Jogador')
        Lvjogador = cursor.fetchone()
        Lvjogador = Lvjogador[0]

        cursor.execute('SELECT DanoElementar FROM MobsFire')
        danoelementar = cursor.fetchall()
        danoelementar = danoelementar[indanimal][0]

        cursor.execute('SELECT * FROM Fragmentos')
        defesaelementar = cursor.fetchall()
        defesaelementar = defesaelementar[0][indanimal] - 1

        diferencaelementar = danoelementar - defesaelementar
        if diferencaelementar < 0:
            diferencaelementar = 0

        diferencalv = lvanimal - Lvjogador
        HPanimal = hpanimal
        Danoanimal = danoanimal + diferencaelementar
        if Lvjogador >= lvanimal or diferencalv <= 0:
            pass
        else:
            HPanimal = hpanimal + diferencalv
            Danoanimal = danoanimal + diferencalv + diferencaelementar

        cursor.execute('SELECT Exp FROM MobsFire')
        expanimal = cursor.fetchall()
        expanimal = expanimal[indanimal][0]

        cursor.execute('SELECT Dinheiro FROM MobsFire')
        dinheiroanimal = cursor.fetchall()
        dinheiroanimal = dinheiroanimal[indanimal][0]
        return indanimal, lvanimal, HPanimal, Danoanimal, expanimal, dinheiroanimal, nomeanimal, Lvjogador


def loja():
    banco = sqlite3.connect('Banco_Dados.db')
    cursor = banco.cursor()
    while True:
        print('Loja de poções:')
        for i in range(0, len(BDP.Loja)):
            print(f'[{i}] {BDP.Loja[i][0]} (+{BDP.Loja[i][2]}HP) = {BDP.Loja[i][1]} moedas')
        print('[C] Voltar')
        tecla = 10
        while True:
            strtecla = str(input('Tecla: ')).strip().upper()
            isnumeric = strtecla.isnumeric()
            ebool = str(isnumeric)
            find = ebool.find('True')
            if find == 0:
                tecla = int(strtecla)
                if tecla < 0 or tecla >= len(BDP.Loja):
                    print('\033[31mErro:  \033[mOpção inválida, tente novamente')
                else:
                    break
            else:
                if strtecla in 'C':
                    break
                print('\033[31mErro:  \033[mOpção inválida, tente novamente')
        if strtecla in 'C':
            break

        while True:
            cursor.execute('''SELECT Dinheiro FROM Jogador''')
            Dinheiro = cursor.fetchone()
            maximo = (Dinheiro[0] - 1) / BDP.Loja[tecla][1]
            print(f'Compra Máxima de {trunc(maximo)} poções')
            qtde = str(input(f'Quantidade de {BDP.Loja[tecla][0]}: '))
            isnumeric = qtde.isnumeric()
            ebool = str(isnumeric)
            find = ebool.find('True')
            if find == 0:
                qtde = int(qtde)
                custo = BDP.Loja[tecla][1] * qtde
                if (Dinheiro[0] - 1) >= custo or qtde == 0:
                    break
                else:
                    print('\033[33mErro: \033[mDinheiro insuficiente.')
            else:
                print('\033[31mErro:  \033[mOpção inválida, tente novamente')

        busca = BDP.Loja[tecla][0]
        pagamento = (Dinheiro[0] - 1) - custo
        cursor.execute("UPDATE Jogador SET Dinheiro = '" + str(pagamento) + "' WHERE '" + str(Dinheiro[0] - 1) + "'")
        cursor.execute('''SELECT * FROM Bolsa''')
        buscapot = cursor.fetchall()
        compra = buscapot[0][tecla] + qtde
        cursor.execute(
            "UPDATE Bolsa SET '" + str(busca) + "' = '" + str(compra) + "' WHERE '" + str(buscapot[0][tecla]) + "'")
        banco.commit()


def RecuperarHP():
    banco = sqlite3.connect('Banco_Dados.db')
    cursor = banco.cursor()
    lista = []
    while True:
        cursor.execute('SELECT Vida FROM Jogador')
        vida = cursor.fetchone()
        cursor.execute('SELECT HP FROM Jogador')
        HP = cursor.fetchone()
        if vida[0] == HP[0]:
            print("HP cheio")
            sleep(1)
            break
        print('Usar qual poção:')
        for i in range(0, len(BDP.Loja)):
            cursor.execute('SELECT * FROM Bolsa')
            qtdepot = cursor.fetchall()
            qtde = qtdepot[0][i] - 1
            if qtde > 0:
                n = str(i)
                lista.append(n)

                print(f'[{BDP.Loja[i][4]}] {BDP.Loja[i][0]} (+{BDP.Loja[i][2]}HP) = {qtde}')
        print('[C] Voltar')
        while True:
            tecla3 = str(input('tecla: ')).strip().upper()
            if tecla3 in lista or tecla3 in 'C':
                break
            else:
                print('\033[31mErro:  \033[mOpção inválida, tente novamente')
        if tecla3 in 'C':
            break

        tecla3 = int(tecla3)
        busca = BDP.Loja[tecla3][0]
        cursor.execute('SELECT Vida FROM Jogador')
        Vida = cursor.fetchone()
        rec = Vida[0] + BDP.Loja[tecla3][2]
        if rec >= HP[0]:
            cursor.execute("UPDATE Jogador SET Vida = '" + str(HP[0]) + "' WHERE '" + str(Vida[0]) + "'")

        else:
            cursor.execute("UPDATE Jogador SET Vida = '" + str(rec) + "' WHERE '" + str(Vida[0]) + "'")

        banco.commit()
        for i in lista:
            lista.remove(i)

        cursor.execute('SELECT * FROM Bolsa')
        qtdepot = cursor.fetchone()
        qtde = qtdepot[tecla3] - 1
        cursor.execute(
            "UPDATE Bolsa SET '" + str(busca) + "' = '" + str(qtde) + "' WHERE '" + str(qtdepot[tecla3]) + "'")
        cursor.execute('SELECT HP FROM Jogador')
        HP = cursor.fetchone()
        cursor.execute('SELECT Vida FROM Jogador')
        Vida = cursor.fetchone()
        print(f'HP: {Vida[0]}/{HP[0]}')
        sleep(1)
        banco.commit()
        break


def LvJogador():
    while True:
        banco = sqlite3.connect('Banco_Dados.db')
        cursor = banco.cursor()
        cursor.execute('SELECT QtdeExp FROM Jogador')
        QtdeExp = cursor.fetchone()
        cursor.execute('SELECT EXP FROM Jogador')
        EXP = cursor.fetchone()
        if QtdeExp[0] >= EXP[0]:
            cursor.execute('SELECT Level FROM Jogador')
            Lv = cursor.fetchone()
            uplv = Lv[0] + 1
            cursor.execute("UPDATE Jogador SET Level = '" + str(uplv) + "' WHERE '" + str(Lv[0]) + "' ")

            upexp = EXP[0] * 2
            cursor.execute("UPDATE Jogador SET EXP = '" + str(upexp) + "' WHERE '" + str(EXP[0]) + "' ")

            banco.commit()
            cursor.execute('SELECT Vida FROM Jogador')
            Vida = cursor.fetchone()
            cursor.execute('SELECT HP FROM Jogador')
            HP = cursor.fetchone()

            uphp = HP[0] + 20
            cursor.execute("UPDATE Jogador SET HP = '" + str(uphp) + "' WHERE '" + str(HP[0]) + "' ")
            banco.commit()
            cursor.execute('SELECT HP FROM Jogador')
            HP = cursor.fetchone()
            cursor.execute("UPDATE Jogador SET Vida = '" + str(HP[0]) + "' WHERE '" + str(Vida[0]) + "' ")

            cursor.execute('SELECT Diamante FROM Jogador')
            diamante = cursor.fetchone()
            ganhodiamante = diamante[0] + uplv
            cursor.execute(
                "UPDATE Jogador SET Diamante = '" + str(ganhodiamante) + "' WHERE '" + str(diamante[0]) + "' ")

            cursor.execute('SELECT Pontos FROM Jogador')
            pontos = cursor.fetchone()
            ganhopontos = pontos[0] + 1
            cursor.execute("UPDATE Jogador SET Pontos = '" + str(ganhopontos) + "' WHERE '" + str(pontos[0]) + "' ")

            print(f'Up Lv.{uplv}')
            sleep(1)
            print(f'Você ganhou {uplv} diamantes')
            print('Você ganhou 1 pontos de atributos')
            sleep(1)
            banco.commit()
        else:
            break


def LevelanimalColinaVerde(indanimal, nomeanimal):
    banco = sqlite3.connect('Banco_Dados.db')
    cursor = banco.cursor()
    cursor.execute('SELECT Morte FROM MobsColinaVerde')
    qtde = cursor.fetchall()
    qtde = qtde[indanimal][0] - 1
    LvAnimal = 0
    cursor.execute('SELECT Level FROM MobsColinaVerde')
    lvanimal = cursor.fetchall()
    lvanimal = lvanimal[indanimal][0]

    if qtde % 50 == 0:
        LvAnimal = qtde / 50
        LvAnimal += BDP.mobscolinaverde[indanimal][1]

    while True:
        if LvAnimal > lvanimal:
            if LvAnimal > BDP.mobscolinaverde[indanimal][1] + 10:
                pass

            else:
                cursor.execute(
                    "UPDATE MobsColinaVerde SET Level = '" + str(LvAnimal) + "' WHERE Nome = '" + str(nomeanimal) + "'")

                cursor.execute('SELECT HP FROM MobsColinaVerde')
                hpanimal = cursor.fetchall()
                hpanimal = hpanimal[indanimal][0]
                ganhohp = hpanimal + 1
                cursor.execute(
                    "UPDATE MobsColinaVerde SET HP = '" + str(ganhohp) + "' WHERE Nome = '" + str(nomeanimal) + "'")

                cursor.execute('SELECT Dano FROM MobsColinaVerde')
                danoanimal = cursor.fetchall()
                danoanimal = danoanimal[indanimal][0]
                ganhodano = danoanimal + 1
                cursor.execute("UPDATE MobsColinaVerde SET Dano = '" + str(ganhodano) + "' WHERE Nome = '" + str(
                    nomeanimal) + "'")

                cursor.execute('SELECT Exp FROM MobsColinaVerde')
                expanimal = cursor.fetchall()
                expanimal = expanimal[indanimal][0]

                ganhoexp = expanimal + 1
                cursor.execute("UPDATE MobsColinaVerde SET Exp = '" + str(ganhoexp) + "' WHERE Nome = '" + str(
                    nomeanimal) + "'")

                cursor.execute('SELECT Dinheiro FROM MobsColinaVerde')
                dinheiroanimal = cursor.fetchall()
                dinheiroanimal = dinheiroanimal[indanimal][0]
                ganhodinheiro = dinheiroanimal + 1
                cursor.execute("UPDATE MobsColinaVerde SET Dinheiro = '" + str(ganhodinheiro) + "' WHERE Nome = '" +
                               str(nomeanimal) + "'")
                banco.commit()
        break


def LevelanimalDeserto(indanimal, nomeanimal):
    banco = sqlite3.connect('Banco_Dados.db')
    cursor = banco.cursor()
    cursor.execute('SELECT Morte FROM MobsDeserto')
    qtde = cursor.fetchall()
    qtde = qtde[indanimal][0] - 1
    LvAnimal = 0
    cursor.execute('SELECT Level FROM MobsDeserto')
    lvanimal = cursor.fetchall()
    lvanimal = lvanimal[indanimal][0]

    if qtde % 50 == 0:
        LvAnimal = qtde / 50

    while True:
        if LvAnimal > lvanimal:
            if LvAnimal > BDP.mobsdeseto[indanimal][1] + 10:
                pass

            else:
                cursor.execute(
                    "UPDATE MobsDeserto SET Level = '" + str(LvAnimal) + "' WHERE Nome = '" + str(nomeanimal) + "'")

                cursor.execute('SELECT HP FROM MobsDeserto')
                hpanimal = cursor.fetchall()
                hpanimal = hpanimal[indanimal][0]
                ganhohp = hpanimal + 1
                cursor.execute(
                    "UPDATE MobsDeserto SET HP = '" + str(ganhohp) + "' WHERE Nome = '" + str(nomeanimal) + "'")

                cursor.execute('SELECT Dano FROM MobsDeserto')
                danoanimal = cursor.fetchall()
                danoanimal = danoanimal[indanimal][0]
                ganhodano = danoanimal + 1
                cursor.execute("UPDATE MobsDeserto SET Dano = '" + str(ganhodano) + "' WHERE Nome = '" + str(
                    nomeanimal) + "'")

                cursor.execute('SELECT Exp FROM MobsDeserto')
                expanimal = cursor.fetchall()
                expanimal = expanimal[indanimal][0]
                ganhoexp = expanimal + 1
                cursor.execute("UPDATE MobsDeserto SET Exp = '" + str(ganhoexp) + "' WHERE Nome = '" + str(
                    nomeanimal) + "'")

                cursor.execute('SELECT Dinheiro FROM MobsDeserto')
                dinheiroanimal = cursor.fetchall()
                dinheiroanimal = dinheiroanimal[indanimal][0]
                ganhodinheiro = dinheiroanimal + 1
                cursor.execute("UPDATE MobsDeserto SET Dinheiro = '" + str(ganhodinheiro) + "' WHERE Nome = '" + str(
                    nomeanimal) + "'")
                banco.commit()
        break


def LevelanimalCavernaminer(indanimal, nomeanimal):
    banco = sqlite3.connect('Banco_Dados.db')
    cursor = banco.cursor()
    cursor.execute('SELECT Morte FROM MobsCavernaMinerção')
    qtde = cursor.fetchall()
    qtde = qtde[indanimal][0] - 1
    LvAnimal = 0
    cursor.execute('SELECT Level FROM MobsCavernaMinerção')
    lvanimal = cursor.fetchall()
    lvanimal = lvanimal[indanimal][0]

    if qtde % 50 == 0:
        LvAnimal = qtde / 50

    while True:
        if LvAnimal > lvanimal:
            if LvAnimal > BDP.mobscarvenaminer[indanimal][1] + 10:
                pass

            else:
                cursor.execute(
                    "UPDATE MobsCavernaMinerção SET Level = '" + str(LvAnimal) + "' WHERE Nome = '" + str(
                        nomeanimal) + "'")

                cursor.execute('SELECT HP FROM MobsCavernaMinerção')
                hpanimal = cursor.fetchall()
                hpanimal = hpanimal[indanimal][0]
                ganhohp = hpanimal + 1
                cursor.execute(
                    "UPDATE MobsCavernaMinerção SET HP = '" + str(ganhohp) + "' WHERE Nome = '" + str(nomeanimal) + "'")

                cursor.execute('SELECT Dano FROM MobsCavernaMinerção')
                danoanimal = cursor.fetchall()
                danoanimal = danoanimal[indanimal][0]
                ganhodano = danoanimal + 1
                cursor.execute("UPDATE MobsCavernaMinerção SET Dano = '" + str(ganhodano) + "' WHERE Nome = '" + str(
                    nomeanimal) + "'")

                cursor.execute('SELECT Exp FROM MobsCavernaMinerção')
                expanimal = cursor.fetchall()
                expanimal = expanimal[indanimal][0]
                ganhoexp = expanimal + 1
                cursor.execute("UPDATE MobsCavernaMinerção SET Exp = '" + str(ganhoexp) + "' WHERE Nome = '" + str(
                    nomeanimal) + "'")

                cursor.execute('SELECT Dinheiro FROM MobsCavernaMinerção')
                dinheiroanimal = cursor.fetchall()
                dinheiroanimal = dinheiroanimal[indanimal][0]
                ganhodinheiro = dinheiroanimal + 1
                cursor.execute("UPDATE MobsCavernaMinerção SET Dinheiro = '" + str(ganhodinheiro) + "' WHERE Nome = '" +
                               str(nomeanimal) + "'")
                banco.commit()
        break


def LevelanimalFlorestasombria(indanimal, nomeanimal):
    banco = sqlite3.connect('Banco_Dados.db')
    cursor = banco.cursor()
    cursor.execute('SELECT Morte FROM MobsFlorestaSombria')
    qtde = cursor.fetchall()
    qtde = qtde[indanimal][0] - 1
    LvAnimal = 0
    cursor.execute('SELECT Level FROM MobsFlorestaSombria')
    lvanimal = cursor.fetchall()
    lvanimal = lvanimal[indanimal][0]

    if qtde % 50 == 0:
        LvAnimal = qtde / 50

    while True:
        if LvAnimal > lvanimal:
            if LvAnimal > BDP.mobsflorestasombria[indanimal][1] + 10:
                pass

            else:
                cursor.execute(
                    "UPDATE MobsFlorestaSombria SET Level = '" + str(LvAnimal) + "' WHERE Nome = '" + str(
                        nomeanimal) + "'")

                cursor.execute('SELECT HP FROM MobsFlorestaSombria')
                hpanimal = cursor.fetchall()
                hpanimal = hpanimal[indanimal][0]
                ganhohp = hpanimal + 1
                cursor.execute(
                    "UPDATE MobsFlorestaSombria SET HP = '" + str(ganhohp) + "' WHERE Nome = '" + str(nomeanimal) + "'")

                cursor.execute('SELECT Dano FROM MobsFlorestaSombria')
                danoanimal = cursor.fetchall()
                danoanimal = danoanimal[indanimal][0]
                ganhodano = danoanimal + 1
                cursor.execute("UPDATE MobsFlorestaSombria SET Dano = '" + str(ganhodano) + "' WHERE Nome = '" + str(
                    nomeanimal) + "'")

                cursor.execute('SELECT Exp FROM MobsFlorestaSombria ')
                expanimal = cursor.fetchall()
                expanimal = expanimal[indanimal][0]
                ganhoexp = expanimal + 1
                cursor.execute("UPDATE MobsFlorestaSombria SET Exp = '" + str(ganhoexp) + "' WHERE Nome = '" + str(
                    nomeanimal) + "'")

                cursor.execute('SELECT Dinheiro FROM MobsFlorestaSombria')
                dinheiroanimal = cursor.fetchall()
                dinheiroanimal = dinheiroanimal[indanimal][0]
                ganhodinheiro = dinheiroanimal + 1
                cursor.execute("UPDATE MobsFlorestaSombria SET Dinheiro = '" + str(ganhodinheiro) + "' WHERE Nome = '" +
                               str(nomeanimal) + "'")
                banco.commit()
        break


def LevelanimalIcy(indanimal, nomeanimal):
    banco = sqlite3.connect('Banco_Dados.db')
    cursor = banco.cursor()
    cursor.execute('SELECT Morte FROM MobsIcy')
    qtde = cursor.fetchall()
    qtde = qtde[indanimal][0] - 1
    LvAnimal = 0
    cursor.execute('SELECT Level FROM MobsIcy')
    lvanimal = cursor.fetchall()
    lvanimal = lvanimal[indanimal][0]

    if qtde % 50 == 0:
        LvAnimal = qtde / 50

    while True:
        if LvAnimal > lvanimal:
            if LvAnimal > BDP.mobsicy[indanimal][1] + 10:
                pass

            else:
                cursor.execute(
                    "UPDATE MobsIcy SET Level = '" + str(LvAnimal) + "' WHERE Nome = '" + str(nomeanimal) + "'")

                cursor.execute('SELECT HP FROM MobsIcy')
                hpanimal = cursor.fetchall()
                hpanimal = hpanimal[indanimal][0]
                ganhohp = hpanimal + 1
                cursor.execute("UPDATE MobsIcy SET HP = '" + str(ganhohp) + "' WHERE Nome = '" + str(nomeanimal) + "'")

                cursor.execute('SELECT Dano FROM MobsIcy')
                danoanimal = cursor.fetchall()
                danoanimal = danoanimal[indanimal][0]
                ganhodano = danoanimal + 1
                cursor.execute(
                    "UPDATE MobsIcy SET Dano = '" + str(ganhodano) + "' WHERE Nome = '" + str(nomeanimal) + "'")

                cursor.execute('SELECT Exp FROM MobsIcy')
                expanimal = cursor.fetchall()
                expanimal = expanimal[indanimal][0]
                ganhoexp = expanimal + 1
                cursor.execute("UPDATE MobsIcy SET Exp = '" + str(ganhoexp) + "' WHERE Nome = '" + str(
                    nomeanimal) + "'")

                cursor.execute('SELECT Dinheiro FROM MobsIcy')
                dinheiroanimal = cursor.fetchall()
                dinheiroanimal = dinheiroanimal[indanimal][0]
                ganhodinheiro = dinheiroanimal + 1
                cursor.execute("UPDATE MobsIcy SET Dinheiro = '" + str(ganhodinheiro) + "' WHERE Nome = '" +
                               str(nomeanimal) + "'")
                banco.commit()
        break


def LevelanimalElectric(indanimal, nomeanimal):
    banco = sqlite3.connect('Banco_Dados.db')
    cursor = banco.cursor()
    cursor.execute('SELECT Morte FROM MobsElectric')
    qtde = cursor.fetchall()
    qtde = qtde[indanimal][0] - 1
    LvAnimal = 0
    cursor.execute('SELECT Level FROM MobsElectric')
    lvanimal = cursor.fetchall()
    lvanimal = lvanimal[indanimal][0]

    if qtde % 50 == 0:
        LvAnimal = qtde / 50

    while True:
        if LvAnimal > lvanimal:
            if LvAnimal > BDP.mobselectric[indanimal][1] + 10:
                pass

            else:
                cursor.execute("UPDATE MobsElectric SET Level = '" + str(LvAnimal) + "' WHERE Nome = '" + str(
                    nomeanimal) + "'")

                cursor.execute('SELECT HP FROM MobsElectric')
                hpanimal = cursor.fetchall()
                hpanimal = hpanimal[indanimal][0]
                ganhohp = hpanimal + 1
                cursor.execute("UPDATE MobsElectric SET HP = '" + str(ganhohp) + "' WHERE Nome = '" + str(
                    nomeanimal) + "'")

                cursor.execute('SELECT Dano FROM MobsElectric')
                danoanimal = cursor.fetchall()
                danoanimal = danoanimal[indanimal][0]
                ganhodano = danoanimal + 1
                cursor.execute("UPDATE MobsElectric SET Dano = '" + str(ganhodano) + "' WHERE Nome = '" + str(
                    nomeanimal) + "'")

                cursor.execute('SELECT Exp FROM MobsElectric')
                expanimal = cursor.fetchall()
                expanimal = expanimal[indanimal][0]
                ganhoexp = expanimal + 1
                cursor.execute("UPDATE MobsElectric SET Exp = '" + str(ganhoexp) + "' WHERE Nome = '" + str(
                    nomeanimal) + "'")

                cursor.execute('SELECT Dinheiro FROM MobsElectric')
                dinheiroanimal = cursor.fetchall()
                dinheiroanimal = dinheiroanimal[indanimal][0]
                ganhodinheiro = dinheiroanimal + 1
                cursor.execute("UPDATE MobsElectric SET Dinheiro = '" + str(ganhodinheiro) + "' WHERE Nome = '" +
                               str(nomeanimal) + "'")
                banco.commit()
        break


def LevelanimalVulcao(indanimal, nomeanimal):
    banco = sqlite3.connect('Banco_Dados.db')
    cursor = banco.cursor()
    cursor.execute('SELECT Morte FROM MobsFire')
    qtde = cursor.fetchall()
    qtde = qtde[indanimal][0] - 1
    LvAnimal = 0
    cursor.execute('SELECT Level FROM MobsFire')
    lvanimal = cursor.fetchall()
    lvanimal = lvanimal[indanimal][0]

    if qtde % 50 == 0:
        LvAnimal = qtde / 50
        LvAnimal += BDP.mobsfire[indanimal][1]

    while True:
        if LvAnimal > lvanimal:
            if LvAnimal > BDP.mobscolinaverde[indanimal][1] + 10:
                pass

            else:
                cursor.execute(
                    "UPDATE MobsColinaVerde SET Level = '" + str(LvAnimal) + "' WHERE Nome = '" + str(nomeanimal) + "'")

                cursor.execute('SELECT HP FROM MobsFire')
                hpanimal = cursor.fetchall()
                hpanimal = hpanimal[indanimal][0]
                ganhohp = hpanimal + 1
                cursor.execute(
                    "UPDATE MobsFire SET HP = '" + str(ganhohp) + "' WHERE Nome = '" + str(nomeanimal) + "'")

                cursor.execute('SELECT Dano FROM MobsFire')
                danoanimal = cursor.fetchall()
                danoanimal = danoanimal[indanimal][0]
                ganhodano = danoanimal + 1
                cursor.execute("UPDATE MobsFire SET Dano = '" + str(ganhodano) + "' WHERE Nome = '" + str(
                    nomeanimal) + "'")

                cursor.execute('SELECT Exp FROM MobsFire')
                expanimal = cursor.fetchall()
                expanimal = expanimal[indanimal][0]

                ganhoexp = expanimal + 1
                cursor.execute("UPDATE MobsFire SET Exp = '" + str(ganhoexp) + "' WHERE Nome = '" + str(
                    nomeanimal) + "'")

                cursor.execute('SELECT Dinheiro FROM MobsFire')
                dinheiroanimal = cursor.fetchall()
                dinheiroanimal = dinheiroanimal[indanimal][0]
                ganhodinheiro = dinheiroanimal + 1
                cursor.execute("UPDATE MobsFire SET Dinheiro = '" + str(ganhodinheiro) + "' WHERE Nome = '" +
                               str(nomeanimal) + "'")
                banco.commit()
        break


def Mortesmobs():
    while True:
        banco = sqlite3.connect('Banco_Dados.db')
        cursor = banco.cursor()

        # Colina Verde
        cursor.execute('SELECT Morte FROM MobsColinaVerde')
        kill = cursor.fetchall()
        for pos, morte in enumerate(kill):
            for qtde in morte:
                qtde -= 1
                if qtde > 0:
                    print(f'{BDP.mobscolinaverde[pos][0]} = {qtde}')

        # Deserto
        cursor.execute('SELECT Morte FROM MobsDeserto')
        kill = cursor.fetchall()
        for pos, morte in enumerate(kill):
            for qtde in morte:
                qtde -= 1
                if qtde > 0:
                    print(f'{BDP.mobsdeseto[pos][0]} = {qtde}')

        # Caverna de Mineração
        cursor.execute('SELECT Morte FROM MobsCavernaMinerção')
        kill = cursor.fetchall()
        for pos, morte in enumerate(kill):
            for qtde in morte:
                qtde -= 1
                if qtde > 0:
                    print(f'{BDP.mobscarvenaminer[pos][0]} = {qtde}')

        # Floresta Sombria
        cursor.execute('SELECT Morte FROM MobsFlorestaSombria')
        kill = cursor.fetchall()
        for pos, morte in enumerate(kill):
            for qtde in morte:
                qtde -= 1
                if qtde > 0:
                    print(f'{BDP.mobsflorestasombria[pos][0]} = {qtde}')

        # Icy
        cursor.execute('SELECT Morte FROM MobsIcy')
        kill = cursor.fetchall()
        for pos, morte in enumerate(kill):
            for qtde in morte:
                qtde -= 1
                if qtde > 0:
                    print(f'{BDP.mobsicy[pos][0]} = {qtde}')

        # Electric
        cursor.execute('SELECT Morte FROM MobsElectric')
        kill = cursor.fetchall()
        for pos, morte in enumerate(kill):
            for qtde in morte:
                qtde -= 1
                if qtde > 0:
                    print(f'{BDP.mobselectric[pos][0]} = {qtde}')

        # Fire
        cursor.execute('SELECT Morte FROM MobsFire')
        kill = cursor.fetchall()
        for pos, morte in enumerate(kill):
            for qtde in morte:
                qtde -= 1
                if qtde > 0:
                    print(f'{BDP.mobsfire[pos][0]} = {qtde}')
        break


Connecte()
