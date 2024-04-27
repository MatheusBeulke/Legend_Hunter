from time import sleep
from math import trunc
import BDP
from random import randint
import sqlite3
from pathlib import Path


def Busca(Select, From, Tipo):
    banco = sqlite3.connect('Banco_Dados.db')
    cursor = banco.cursor()
    if Select in '*':
        cursor.execute('SELECT * FROM "' + str(From) + '"')
        if Tipo in 'all':
            busca = cursor.fetchall()
            return busca

        else:
            busca = cursor.fetchone()
            return busca

    cursor.execute(f'SELECT {Select} FROM {From}')
    if Tipo in 'one':
        busca = cursor.fetchone()
        return busca
    elif Tipo in 'all':
        busca = cursor.fetchall()
        return busca


def Update(update, Set, Igual, Where):
    banco = sqlite3.connect('Banco_Dados.db')
    cursor = banco.cursor()

    cursor.execute(
        "UPDATE '" + str(update) + "' SET '" + str(Set) + "' = '" + str(Igual) + "' WHERE '" + str(Where) + "'")
    banco.commit()


def UpdateNome(update, Set, Igual, Where):
    banco = sqlite3.connect('Banco_Dados.db')
    cursor = banco.cursor()

    cursor.execute(
        "UPDATE '" + str(update) + "' SET '" + str(Set) + "' = '" + str(Igual) + "' WHERE Nome = '" + str(Where) + "'")
    banco.commit()


def Connecte():
    caminho = Path('Banco_Dados.db')
    if caminho.exists():
        inicio()
    else:
        banco = sqlite3.connect('Banco_Dados.db')
        cursor = banco.cursor()
        CriandoBD(cursor, banco)


def CriandoBD(cursor, banco):
    # Jogador
    cursor.execute('CREATE TABLE Jogador (Nome text, Level integer, HP integer, Vida integer, Mana integer,'
                   'QtdeMana integer, QtdeExp integer, EXP integer, Dinheiro integer, Diamante integer,'
                   'Pontos integer)')
    while True:
        nome = str(input('Nome: ')).strip()
        if nome in '':
            print('Campo Vázio')
        else:
            print('Conta Criado com sucesso!')
            break

    cursor.execute("INSERT INTO Jogador VALUES('" + nome + "', 1, 100, 100, 100, 100, 1, 100, 1, 1, 1)")

    # Bolsa
    cursor.execute('CREATE TABLE Bolsa (PoçãoPequena integer, PoçãoMédia integer, PoçãoGrande integer,'
                   'PoçãoGigante integer, HiperPoção integer, PoçãoMagica integer)')

    cursor.execute("INSERT INTO Bolsa VALUES(11, 1, 1, 1, 1, 1)")

    # Itens
    cursor.execute('CREATE TABLE Itens (Madeiras integer, Pedras integer, Peixes integer, Couros integer)')
    cursor.execute("INSERT INTO Itens VALUES(1, 1, 1, 1)")

    # MobsColinaVerde
    cursor.execute('CREATE TABLE MobsColinaVerde (Nome text, Level integer, HP integer, Dano integer,'
                   ' DanoElementar integer, Exp integer, Dinheiro integer, Morte integer)')

    #                                                Nome,   Lv,  HP, D, DF, E, D, M
    cursor.execute("INSERT INTO MobsColinaVerde VALUES('Rats', 1, 12, 7 , 2, 5, 3, 1)")
    cursor.execute("INSERT INTO MobsColinaVerde VALUES('Crow', 15, 40, 25, 4, 17, 15, 1)")
    cursor.execute("INSERT INTO MobsColinaVerde VALUES('Wolf', 30, 70, 47, 6, 34, 29, 1)")
    cursor.execute("INSERT INTO MobsColinaVerde VALUES('Lizard', 45, 102, 71, 8, 53, 45, 1)")
    cursor.execute("INSERT INTO MobsColinaVerde VALUES('Slime', 60, 136, 97, 10, 74, 63, 1)")
    cursor.execute("INSERT INTO MobsColinaVerde VALUES('Assasin', 75, 172, 125, 12, 97, 83, 1)")
    cursor.execute("INSERT INTO MobsColinaVerde VALUES('Bear', 90, 210, 155, 14, 122, 105, 1)")
    cursor.execute("INSERT INTO MobsColinaVerde VALUES('Goblin', 105, 250, 187, 16, 149, 129, 1)")
    cursor.execute("INSERT INTO MobsColinaVerde VALUES('Minotaur', 120, 292, 221, 18, 178, 155, 1)")
    cursor.execute("INSERT INTO MobsColinaVerde VALUES('Peixes', 0, 0, 0, 0, 0, 0, 0)")
    cursor.execute("INSERT INTO MobsColinaVerde VALUES('Boss', 1, 800, 400, 100, 1000, 500, 1)")

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
    cursor.execute("INSERT INTO MobsDeserto VALUES('Boss', 1, 1200, 900, 100, 1500, 1000, 1)")

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
    cursor.execute("INSERT INTO MobsCavernaMinerção VALUES('Pedras', 0, 0, 0, 0, 0, 0, 0)")
    cursor.execute("INSERT INTO MobsCavernaMinerção VALUES('Boss', 1, 1700, 1400, 100, 2000, 1500, 1)")

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
    cursor.execute("INSERT INTO MobsFlorestaSombria VALUES('Madeira', 0, 0, 0, 0, 0, 0, 0)")
    cursor.execute("INSERT INTO MobsFlorestaSombria VALUES('Boss', 1, 2300, 1900, 100, 2500, 2000, 1)")

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
    cursor.execute("INSERT INTO MobsIcy VALUES('Boss', 1, 3000, 2400, 100, 3000, 2500, 1)")

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
    cursor.execute("INSERT INTO MobsElectric VALUES('Boss', 1, 3800, 2900, 100, 3500, 3000, 1)")

    # Fogo
    cursor.execute('CREATE TABLE MobsFire (Nome text, Level integer, HP integer, Dano integer,'
                   'DanoElementar integer, Exp integer, Dinheiro integer, Morte integer)')

    #                                            Nome,   Lv,  HP,   D,    DF,  E,    D,    M
    cursor.execute("INSERT INTO MobsFire VALUES('Flame', 795, 1960, 1580, 112, 1270, 1100, 1)")
    cursor.execute("INSERT INTO MobsFire VALUES('Fire Golem', 810, 1988, 1600, 114, 1285, 1112, 1)")
    cursor.execute("INSERT INTO MobsFire VALUES('Wizard', 825, 2018, 1622, 116, 1302, 1126, 1)")
    cursor.execute("INSERT INTO MobsFire VALUES('Dragon', 840, 2050, 1646, 118, 1321, 1142, 1)")
    cursor.execute("INSERT INTO MobsFire VALUES('Demon', 855, 2084, 1672, 120, 1342, 1160, 1)")
    cursor.execute("INSERT INTO MobsFire VALUES('Boss', 1, 4700, 3400, 100, 4000, 3500, 1)")

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

    # Pet
    cursor.execute('CREATE TABLE Pets (Nome text, Level integer, HP integer, Vida integer, Dano integer, Qtde integer, '
                   'Exp integer, QtdeExp integer, Preco integer, id integer)')
    cursor.execute("INSERT INTO Pets VALUES('Wolf', 1, 50, 50, 5, 1, 1, 100, 100, 0)")
    cursor.execute("INSERT INTO Pets VALUES('Scorpion', 1, 330, 330, 25, 1, 1, 100, 200, 1)")
    cursor.execute("INSERT INTO Pets VALUES('Troll', 1, 800, 800, 45, 1, 1, 100, 300, 2)")
    cursor.execute("INSERT INTO Pets VALUES('Shandow', 1, 1126, 1126, 65, 1, 1, 100, 400, 3)")
    cursor.execute("INSERT INTO Pets VALUES('Icy Dragon', 1, 1640, 1640, 85, 1, 1, 100, 500, 4)")
    cursor.execute("INSERT INTO Pets VALUES('Electric Yeti', 1, 1780, 1780, 105, 1, 1, 100, 600, 5)")
    cursor.execute("INSERT INTO Pets VALUES('Demon', 1, 1988, 1988, 125, 1, 1, 100, 700, 6)")

    # PetsJogador
    cursor.execute('CREATE TABLE PetsJogador (Nome text, Level integer, HP integer, Vida integer, Dano integer,'
                   'id integer)')
    cursor.execute("INSERT INTO PetsJogador VALUES('', 1, 1, 1, 1, 1)")

    # Lojas
    cursor.execute('CREATE TABLE Lojas (Nome text, Level integer, CustoMadeiras integer, CustoPedras integer,'
                   'CustoPeixes integer, CustoCouros integer)')
    cursor.execute('INSERT INTO Lojas VALUES("Poções", 1, 10, 20, 30, 0)')
    cursor.execute('INSERT INTO Lojas VALUES("Ferramentas", 1, 10, 30, 0, 0)')
    cursor.execute('INSERT INTO Lojas VALUES("Pets", 1, 20, 30, 0, 0)')
    cursor.execute('INSERT INTO Lojas VALUES("Magias", 1, 10, 20, 0, 20)')

    # Picaretas
    cursor.execute('CREATE TABLE Picaretas (Nome text, Eficiencia integer, Preco integer, Qtde)')
    cursor.execute('INSERT INTO Picaretas VALUES("Picareta Inicial", 90, 50, 1)')
    cursor.execute('INSERT INTO Picaretas VALUES("Picareta de Ferro", 60, 100, 1)')
    cursor.execute('INSERT INTO Picaretas VALUES("Picareta de Titanio", 30, 150, 1)')
    cursor.execute('INSERT INTO Picaretas VALUES("Picareta dos Deuses", 15, 200, 1)')

    # Machados
    cursor.execute('CREATE TABLE Machados (Nome text, Eficiencia integer, Preco integer, Qtde)')
    cursor.execute('INSERT INTO Machados VALUES("Machado Inicial", 60, 20, 1)')
    cursor.execute('INSERT INTO Machados VALUES("Machado de Ferro", 40, 40, 1)')
    cursor.execute('INSERT INTO Machados VALUES("Machado de Titanio", 20, 60, 1)')
    cursor.execute('INSERT INTO Machados VALUES("Machado dos Deuses", 10, 80, 1)')

    # Vara de Pesca
    cursor.execute('CREATE TABLE VaraPesca (Nome text, Eficiencia integer, Preco integer, Qtde)')
    cursor.execute('INSERT INTO VaraPesca VALUES("Vara de Pesca", 40, 30, 1)')
    cursor.execute('INSERT INTO VaraPesca VALUES("Vara de Pesca com Comida", 20, 60, 1)')

    # Magias
    cursor.execute('Create TABLE Magias (Nome text, Lv integer, Mana integer, Dano integer, Preco integer,'
                   'Lvmin integer, tempo integer, Qtde integer, Id integer)')
    cursor.execute('INSERT INTO Magias VALUES("Hit1", 1, 60, 20, 10, 5, 1, 1, 0)')
    cursor.execute('INSERT INTO Magias VALUES("Hit2", 2, 120, 60, 50, 40, 1, 1, 0)')
    cursor.execute('INSERT INTO Magias VALUES("Hit3", 3, 180, 100, 100, 80, 1, 1, 0)')

    cursor.execute('INSERT INTO Magias VALUES("Ar1", 1, 240, 140, 150, 140, 1, 1, 1)')
    cursor.execute('INSERT INTO Magias VALUES("Ar2", 2, 300, 180, 190, 180, 1, 1, 1)')
    cursor.execute('INSERT INTO Magias VALUES("Ar3", 3, 360, 220, 250, 220, 1, 1, 1)')

    cursor.execute('INSERT INTO Magias VALUES("Psiquico1", 1, 420, 260, 100, 150, 1, 1, 2)')
    cursor.execute('INSERT INTO Magias VALUES("Psiquico2", 2, 480, 300, 110, 200, 1, 1, 2)')
    cursor.execute('INSERT INTO Magias VALUES("Psiquico3", 3, 540, 340, 200, 250, 1, 1, 2)')

    cursor.execute('INSERT INTO Magias VALUES("Alma1", 1, 600, 380, 150, 300, 1, 1, 3)')
    cursor.execute('INSERT INTO Magias VALUES("Alma2", 2, 660, 420, 200, 350, 1, 1, 3)')
    cursor.execute('INSERT INTO Magias VALUES("Alma3", 3, 720, 460, 250, 400, 1, 1, 3)')

    cursor.execute('INSERT INTO Magias VALUES("Gelo1", 1, 780, 500, 200, 450, 1, 1, 4)')
    cursor.execute('INSERT INTO Magias VALUES("Gelo2", 2, 840, 540, 250, 500, 1, 1, 4)')
    cursor.execute('INSERT INTO Magias VALUES("Gelo3", 3, 900, 580, 300, 550, 1, 1, 4)')

    cursor.execute('INSERT INTO Magias VALUES("Eletrico1", 1, 620, 720, 350, 600, 1, 1, 5)')
    cursor.execute('INSERT INTO Magias VALUES("Eletrico2", 2, 1020, 760, 400, 650, 1, 1, 5)')
    cursor.execute('INSERT INTO Magias VALUES("Eletrico3", 3, 1080, 800, 450, 650, 1, 1, 5)')

    cursor.execute('INSERT INTO Magias VALUES("Fogo1", 1, 1140, 840, 500, 700, 1, 1, 6)')
    cursor.execute('INSERT INTO Magias VALUES("Fogo2", 2, 1200, 880, 550, 750, 1, 1, 6)')
    cursor.execute('INSERT INTO Magias VALUES("Fogo3", 3, 1260, 920, 600, 800, 1, 1, 6)')

    # MagiaJogador
    cursor.execute('Create TABLE MagiaJogador (Nome text, Lv integer, Mana integer, Dano integer, tempo integer,'
                   'Id integer)')
    cursor.execute("INSERT INTO MagiaJogador VALUES('vazio', 1, 1, 1, 1, 1)")

    banco.commit()
    inicio()


def inicio():
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
            for num, local in enumerate(BDP.mapa):
                print(f'[{num}] {local}')
                sleep(0.5)
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
                tecla1 = int(tecla1)
                locais = BDP.locais[tecla1]
                Mapa(locais, tecla1)

        elif tecla in 'B':
            while True:
                print('Informações:')
                print('[0] Personagem')
                print('[1] Atributos')
                sleep(1)
                print('[2] Habilidades')
                print('[3] Proteção Elementar')
                sleep(1)
                print('[4] Mochila')
                print('[5] Ferramentas/Armas')
                sleep(1)
                print('[6] Pets')
                print('[7] Magias')
                
                print('[8] Quantidade de mob matado')
                print('[C] Voltar')
                while True:
                    tecla1 = str(input('Tecla: ')).strip().upper()
                    if tecla1 in '012345678C':
                        break
                    else:
                        print('\033[31mErro:  \033[mOpção inválida, tente novamente')
                if tecla1 in 'C':
                    break

                elif tecla1 in '0':
                    Nome = Busca('Nome', 'Jogador', 'one')
                    print(f'Nome: {Nome[0]}')

                    Level = Busca('Level', 'Jogador', 'one')
                    print(f'Level: {Level[0]}')

                    exp = Busca('QtdeExp', 'Jogador', 'one')
                    totalexp = Busca('EXP', 'Jogador', 'one')
                    print(f'Exp: {exp[0] - 1}/{totalexp[0]}')

                    dinheiro = Busca('Dinheiro', 'Jogador', 'one')
                    print(f'Dinheiro: {int(dinheiro[0]) - 1}')

                    diamante = Busca('Diamante', 'Jogador', 'one')
                    print(f'Diamante: {int(diamante[0]) - 1}')
                    sleep(2)

                elif tecla1 in '1':
                    atributos()

                elif tecla1 in '2':
                    habilidades()

                elif tecla1 in '3':
                    print('Quantidade de Fragmentos:')
                    Fragmentos = Busca('*', 'Fragmentos', 'all')
                    for num, f in enumerate(Fragmentos):
                        fragmentos = Fragmentos[0][num] - 1
                        if fragmentos >= 1:
                            print(f'{BDP.Fragmentos[num]} = {fragmentos}')
                    sleep(1)

                elif tecla1 in '4':
                    print('Mochila:')
                    Bolsa = Busca('*', 'Bolsa', 'all')
                    for itens in Bolsa:
                        for pos, Qtde in enumerate(itens):
                            Qtde -= 1
                            if Qtde > 0:
                                print(f'{BDP.Loja[pos][0]} = {Qtde}')
                                sleep(1)
                    sleep(2)
                    Itens = Busca('*', 'Itens', 'all')
                    for itens in Itens:
                        for pos, Qtde in enumerate(itens):
                            Qtde -= 1
                            if Qtde > 0:
                                print(f'{BDP.Itens[pos]} = {Qtde}')
                                sleep(1)
                    sleep(2)

                elif tecla1 in '5':
                    print("Ferramentas/Armas:")
                    qtdepicaretas = Busca('Qtde', 'Picaretas', 'all')
                    qtdemachados = Busca('Qtde', 'Machados', 'all')
                    qtdevarapesca = Busca('Qtde', 'VaraPesca', 'all')

                    for pos, i in enumerate(qtdepicaretas):
                        qtde = int(i[0]) - 1
                        if qtde >= 1:
                            print(f'{BDP.Picaretas[pos][0]} = {qtde}')
                    sleep(1)

                    for pos, i in enumerate(qtdemachados):
                        qtde = int(i[0]) - 1
                        if qtde >= 1:
                            print(f'{BDP.Machados[pos][0]} = {qtde}')
                    sleep(1)

                    for pos, i in enumerate(qtdevarapesca):
                        qtde = int(i[0]) - 1
                        if qtde >= 1:
                            print(f'{BDP.VaraPesca[pos][0]} = {qtde}')
                    sleep(1)

                elif tecla1 in '6':
                    lista = []
                    IdPet = Busca('Id', 'Pets', 'all')
                    NomePet = Busca('Nome', 'Pets', 'all')
                    Lv = Busca('Level', 'Pets', 'all')
                    HP = Busca('HP', 'Pets', 'all')
                    Vida = Busca('Vida', 'Pets', 'all')
                    Dano = Busca('Dano', 'Pets', 'all')
                    Qtde = Busca('Qtde', 'Pets', 'all')

                    for pos, i in enumerate(Qtde):
                        Qtde = int(i[0]) - 1
                        if Qtde == 1:
                            lista.append(pos)
                            if len(lista) == 1:
                                print('Usar qual Pet durante a batalha:')
                                sleep(1)
                            print(f'[{pos}] {NomePet[pos][0]} (Lv.{Lv[pos][0]}) '
                                  f'({Vida[pos][0]}/{HP[pos][0]}HP) (Dano {Dano[pos][0]})')
                            sleep(1)

                    if len(lista) >= 1:
                        print('[C] Voltar')
                        while True:
                            escolha = str(input('Tecla: ')).strip().upper()
                            if escolha.isnumeric():
                                escolha = int(escolha)
                                if escolha in lista:
                                    break
                                else:
                                    print('\033[31mErro:  \033[mOpção inválida, tente novamente')

                            elif escolha in 'C':
                                break
                            else:
                                print('\033[31mErro:  \033[mOpção inválida, tente novamente')

                        if str(escolha) in 'C':
                            pass
                        else:
                            PetJogador = Busca('Nome', 'PetsJogador', 'one')
                            UpdateNome('PetsJogador', 'Id', IdPet[escolha][0], PetJogador[0])
                            UpdateNome('PetsJogador', 'Level', Lv[escolha][0], PetJogador[0])
                            UpdateNome('PetsJogador', 'HP', HP[escolha][0], PetJogador[0])
                            UpdateNome('PetsJogador', 'Vida', Vida[escolha][0], PetJogador[0])
                            UpdateNome('PetsJogador', 'Dano', Dano[escolha][0], PetJogador[0])
                            UpdateNome('PetsJogador', 'Nome', NomePet[escolha][0], PetJogador[0])
                            print(f'Você escolheu usar o Pet {NomePet[escolha][0]}')
                            print(Busca('*', 'PetsJogador', 'all'))
                            sleep(2)
                    else:
                        print('Você não tem nenhum Pet')
                        sleep(3)

                elif tecla1 in '7':
                    print('Magias:')
                    lista = []
                    qtde = Busca('Qtde', 'Magias', 'all')
                    magia = Busca('Nome', 'Magias', 'all')
                    dano = Busca('Dano', 'Magias', 'all')
                    mana = Busca('Mana', 'Magias', 'all')
                    idmagia = Busca('Id', 'Magias', 'all')
                    for pos, i in enumerate(qtde):
                        qtde = int(i[0]) - 1
                        if qtde == 1:
                            lista.append(pos)
                            if len(lista) == 1:
                                print('Usar qual Magia durante a batalha:')
                                sleep(1)
                            print(f'[{pos}] {magia[pos][0]} ({dano[pos][0]} dano) ({mana[pos][0]} mana)')
                            sleep(1)

                    if len(lista) == 0:
                        print('Você não tem nenhuma Magia')
                        sleep(3)
                        pass
                    else:
                        print('[C] Voltar')
                        while True:
                            escolha = str(input('Tecla: ')).strip().upper()
                            if escolha in 'C':
                                break
                            elif escolha.isnumeric():
                                escolha = int(escolha)
                                if escolha in lista:
                                    break
                                else:
                                    print('\033[31mErro:  \033[mOpção inválida, tente novamente')
                            else:
                                print('\033[31mErro:  \033[mOpção inválida, tente novamente')

                        if escolha == 'C':
                            pass
                        else:
                            nome = Busca('Nome', 'MagiaJogador', 'one')

                            UpdateNome('MagiaJogador', 'Dano', dano[escolha][0], nome[0])
                            UpdateNome('MagiaJogador', 'Mana', mana[escolha][0], nome[0])
                            UpdateNome('MagiaJogador', 'Tempo', 1, nome[0])
                            UpdateNome('MagiaJogador', 'Id', idmagia[escolha][0], nome[0])
                            UpdateNome('MagiaJogador', 'Nome', magia[escolha][0], nome[0])
                            print(f'Você escolheu usar a magia {magia[escolha][0]}')
                            sleep(3)

                elif tecla1 in '8':
                    print('Quantidade de Mobs matados:')
                    sleep(1)
                    Mortesmobs()

        elif tecla in 'C':
            while True:
                print('[0] Loja de Poções')
                print('[1] Loja de Ferramentas')
                print('[2] Loja de Pet')
                print('[3] Loja de Magia')
                print('[C] Voltar')
                while True:
                    tecla2 = str(input('Tecla: ')).strip().upper()
                    if tecla2 in '0123C':
                        break
                    else:
                        print('\033[31mErro:  \033[mOpção inválida, tente novamente')
                if tecla2 in 'C':
                    break

                elif tecla2 in '0':
                    lojapot(int(tecla2))

                elif tecla2 in '1':
                    lojaferramentas(int(tecla2))

                elif tecla2 in '2':
                    lojapet(int(tecla2))

                elif tecla2 in '3':
                    lojamagia(int(tecla2))


def Mapa(locais, tecla1):
    while True:
        HP = Busca('HP', 'Jogador', 'one')
        Vida = Busca('Vida', 'Jogador', 'one')
        if BDP.mortejogador == 1:
            xp = Busca('QtdeExp', 'Jogador', 'one')

            if xp[0] >= BDP.perdaexp:
                perdaxp = xp[0] - BDP.perdaexp
                qtdeperdaxp = BDP.perdaexp
                print(f'Você perdeu {qtdeperdaxp} XP')
                sleep(1)
                Update('Jogador', 'QtdeExp', perdaxp, xp[0])

            else:
                BDP.qtdemorte += 1
                tempodefese = Busca('TempoDefese', 'Habilidades', 'one')
                tempoatack = Busca('TempoAtack', 'Habilidades', 'one')

                if BDP.qtdemorte % 2 == 0:
                    perdatempo = 600 + tempodefese[0]
                    Update('Habilidades', 'TempoDefese', perdatempo, tempodefese[0])
                    print('Você perdeu 10 minutos (600 segundos) na habilidade de defesa')
                    sleep(2)
                else:
                    perdatempo = 600 + tempoatack[0]
                    Update('Habilidades', 'TempoAtack', perdatempo, tempoatack[0])
                    print('Você perdeu 10 minutos (600 segundos) na habilidade de atack')
                    sleep(2)

            BDP.mortejogador = 0
            BDP.mortepet = 0
            BDP.perdaexp = 0
            Update('Jogador', 'Vida', HP[0], Vida[0])
            break

        print('Mobs:')
        boss = randint(1, 100)
        if boss <= 2:
            for num in range(0, int(BDP.nmobs[tecla1][-1]) + 1):
                print(f'[{num}] {BDP.mobs[tecla1][num][0]}')
        else:
            for num in range(0, int(BDP.nmobs[tecla1][-1])):
                print(f'[{num}] {BDP.mobs[tecla1][num][0]}')

        print('[C] Voltar')
        while True:
            tecla2 = str(input('Tecla: ')).strip().upper()
            if tecla2 in '':
                print('\033[31mErro:  \033[mOpção inválida, tente novamente')

            elif tecla2 in 'C':
                break

            elif tecla2 in BDP.nmobs[tecla1]:
                if boss >= 2 and int(tecla2) == BDP.nmobs[tecla1][-1]:
                    print('\033[31mErro:  \033[mOpção inválida, tente novamente')
                else:
                    break
            else:
                print('\033[31mErro:  \033[mOpção inválida, tente novamente')

        if tecla2 in 'C':
            break

        (indanimal, lvanimal, HPanimal, Danoanimal, expanimal, dinheiroanimal, nomeanimal, Lvjogador,
         defesa) = infobatalha(locais, tecla1, tecla2)

        if nomeanimal in 'Madeira':
            Qtde = Busca('Qtde', 'Machados', 'all')
            lista = []
            print("Usar qual Machado:")
            for pos, qtde in enumerate(Qtde):
                if int(qtde[0]) > 1:
                    print(f'[{pos}] {BDP.Machados[pos][0]}')
                    lista.append(str(pos))
            if not lista:
                print('Você não tem um machado')
                sleep(2)
            else:
                while True:
                    tecla3 = str(input('Tecla: ')).strip().upper()
                    if tecla3 in lista or tecla3 in 'C':
                        break
                    else:
                        print('\033[31mErro:  \033[mOpção inválida, tente novamente')

                if tecla3 in 'C':
                    pass

                else:
                    while True:
                        print('Cortando Madeiras...')
                        tempo = Busca('Eficiencia', 'Machados', 'all')
                        for i in range(tempo[int(tecla3)][0], -1, -1):
                            print(f'\r{i}', end='')
                            sleep(1)
                        print()
                        qtde = Busca('Madeiras', 'Itens', 'one')
                        Update('Itens', 'Madeiras', qtde[0] + 1, qtde[0])
                        print('Você coletou 1 madeira')
                        sleep(1)

        elif nomeanimal in 'Pedras':
            Qtde = Busca('Qtdde', 'Picaretas', 'all')
            lista = []
            print("Usar qual Picareta:")
            for pos, qtde in enumerate(Qtde):
                if int(qtde[0]) > 1:
                    print(f'[{pos}] {BDP.Picaretas[pos][0]}')
                    lista.append(str(pos))

            if not lista:
                print('Você não tem uma picareta')
                sleep(2)
            else:
                while True:
                    tecla3 = str(input('Tecla: ')).strip().upper()
                    if tecla3 in lista or tecla3 in 'C':
                        break
                    else:
                        print('\033[31mErro:  \033[mOpção inválida, tente novamente')

                if tecla3 in 'C':
                    pass

                else:
                    while True:
                        print('Minerando Pedras...')
                        tempo = Busca('Eficiencia', 'Picaretas', 'all')

                        for i in range(tempo[int(tecla3)][0], -1, -1):
                            print(f'\r{i}', end='')
                            sleep(1)
                        print()
                        qtde = Busca('Pedras', 'Itens', 'one')
                        Update('Itens', 'Pedras', qtde[0] + 1, qtde[0])
                        print('Você coletou 1 pedra')
                        sleep(1)

        elif nomeanimal in 'Peixes':
            Qtde = Busca('Qtde', 'VaraPesca', 'all')
            lista = []
            print("Usar qual Vara de Pesca:")
            for pos, qtde in enumerate(Qtde):
                if int(qtde[0]) > 1:
                    print(f'[{pos}] {BDP.VaraPesca[pos][0]}')
                    lista.append(str(pos))

            if not lista:
                print('Você não tem uma Vara de Pesca')
                sleep(2)
            else:
                while True:
                    tecla3 = str(input('Tecla: ')).strip().upper()
                    if tecla3 in lista or tecla3 in 'C':
                        break
                    else:
                        print('\033[31mErro:  \033[mOpção inválida, tente novamente')

                if tecla3 in 'C':
                    pass

                else:
                    while True:
                        print('Pescando...')
                        tempo = Busca('Eficiencia', 'VaraPesca', 'all')
                        for i in range(tempo[int(tecla3)][0], -1, -1):
                            print(f'\r{i}', end='')
                            sleep(1)
                        print()
                        qtde = Busca('Peixes', 'Itens', 'one')
                        Update('Itens', 'Peixes', qtde[0] + 1, qtde[0])
                        print('Você coletou 1 peixe')
                        sleep(1)

        else:
            print(f'Você encontrou um(a): {nomeanimal}')
            sleep(3)
            print('-=' * 20)

            print(f'Mob: {nomeanimal} Lv.{lvanimal:.0f} \nHP: {HPanimal} \nDano: {Danoanimal}'
                  f' \nDinheiro: {dinheiroanimal} \nExp: {expanimal}')
            print('-=' * 20)
            sleep(3)

            aa = Busca('Atack', 'Atributos', 'one')
            ah = Busca('Atack', 'Habilidades', 'one')
            atack = aa[0] + ah[0]

            nomejogador = Busca('Nome', 'Jogador', 'one')

            qtdemana = Busca('QtdeMana', 'Jogador', 'one')
            mana = Busca('Mana', 'Jogador', 'one')

            print(f'Jogador: {nomejogador[0]} Lv.{Lvjogador}\nHP: {Vida[0]}/{HP[0]}'
                  f' \nDano: {atack - 4}-{atack}\nDefesa: {defesa} \nMana: {mana[0]}/{qtdemana[0]}')
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

            if tecla3 in '1':
                pass

            elif tecla3 in '0':
                if nomeanimal in 'Boss':
                    atacar = 1
                    pass
                else:
                    while True:
                        atacar = str(input('Looping de quantas vezes (Máximo 10 vezes): ')).strip()
                        if atacar.isnumeric():
                            atacar = int(atacar)
                            if atacar > 10 or atacar < 1:
                                print('\033[31mErro:  \033[mQuantidade não possivel')
                            else:
                                break
                        else:
                            print('\033[31mErro:  \033[mOpção inválida, tente novamente')

                sleep(1)
                listapocao = []
                for i in range(0, len(BDP.Loja)):
                    qtdepot = Busca('*', 'Bolsa', 'all')
                    qtde = qtdepot[0][i] - 1
                    if qtde > 0:
                        listapocao.append(str(i))
                        if len(listapocao) == 1:
                            print('Usar qual poção durante a batalha:')
                        print(f'[{BDP.Loja[i][4]}] {BDP.Loja[i][0]} (+{BDP.Loja[i][2]}HP) = {qtde}')

                recquando = 0
                if len(listapocao) > 0:
                    while True:
                        tecla3 = str(input('tecla: ')).strip().upper()
                        if tecla3 in listapocao:
                            break
                        else:
                            print('\033[31mErro:  \033[mOpção inválida, tente novamente')

                    while True:
                        strtecla = str(input('Usar a poção quando a Vida estiver menor ou igual a: '))
                        if strtecla.isnumeric():
                            recquando = int(strtecla)
                            if HP[0] >= recquando >= 0:
                                tecla3 = int(tecla3)
                                break
                            else:
                                print('\033[31mErro:  \033[mOpção inválida, tente novamente')
                        else:
                            print('\033[31mErro:  \033[mOpção inválida, tente novamente')

                for i in range(1, atacar + 1):
                    if i > 1:
                        print(f'Você encontrou outro(a) {nomeanimal}')
                        sleep(2)
                    batalha(indanimal, nomeanimal, HPanimal, Danoanimal, dinheiroanimal, expanimal, locais, atack,
                            HP, tecla3, recquando, listapocao, tecla1)
                    (indanimal, lvanimal, HPanimal, Danoanimal, expanimal, dinheiroanimal, nomeanimal, Lvjogador,
                     defesa) = (infobatalha(locais, tecla1, tecla2))

                    if BDP.mortejogador == 1:
                        break


def infobatalha(locais, tecla1, tecla2):
    indanimal = int(tecla2)
    nomeanimal = Busca('Nome', locais, 'all')
    nomeanimal = nomeanimal[indanimal][0]

    lvanimal = Busca('Level', locais, 'all')
    lvanimal = lvanimal[indanimal][0]

    hpanimal = Busca('HP', locais, 'all')
    hpanimal = hpanimal[indanimal][0]

    danoanimal = Busca('Dano', locais, 'all')
    danoanimal = danoanimal[indanimal][0]

    Lvjogador = Busca('Level', 'Jogador', 'one')
    Lvjogador = Lvjogador[0]

    danoelementar = Busca('DanoElementar', locais, 'all')
    danoelementar = danoelementar[indanimal][0]

    defesaelementar = Busca('*', 'Fragmentos', 'all')
    defesaelementar = defesaelementar[0][tecla1] - 1

    da = Busca('Defese', 'Atributos', 'one')
    dh = Busca('Defese', 'Habilidades', 'one')
    defesa = da[0] + dh[0]

    diferencaelementar = danoelementar - defesaelementar
    if diferencaelementar < 0:
        diferencaelementar = 0
    diferencalv = lvanimal - Lvjogador
    HPanimal = hpanimal
    Danoanimal = danoanimal + diferencaelementar - defesa
    if Lvjogador >= lvanimal or diferencalv <= 0:
        if nomeanimal in 'Boss':
            Danoanimal = danoanimal + diferencaelementar - defesa - (Lvjogador - 1)
        pass
    else:
        HPanimal = hpanimal + diferencalv
        Danoanimal = danoanimal + diferencalv + diferencaelementar - defesa

    if Danoanimal < 0:
        Danoanimal = 0

    expanimal = Busca('Exp', locais, 'all')
    expanimal = expanimal[indanimal][0]

    dinheiroanimal = Busca('Dinheiro', locais, 'all')
    dinheiroanimal = dinheiroanimal[indanimal][0]
    return indanimal, lvanimal, HPanimal, Danoanimal, expanimal, dinheiroanimal, nomeanimal, Lvjogador, defesa


def batalha(indanimal, nomeanimal, HPanimal, Danoanimal, dinheiroanimal, expanimal, locais, atack, HP, tecla3,
            recquando, listapocao, tecla1):
    Vidaanimal = HPanimal
    minimo = atack - 4
    Nomepet = Busca('Nome', 'PetsJogador', 'one')
    Nomejogador = Busca('Nome', 'Jogador', 'one')
    while True:

        # Jogador ataca Mob
        jogadoratack = randint(minimo, atack)
        print('-=' * 10)
        print(f'{Nomejogador[0]}: \033[31m{jogadoratack}\033[m de atack')
        HPanimal -= jogadoratack

        if HPanimal <= 0:
            print(f'{Nomejogador[0]} matou um(a): {nomeanimal}')
            sleep(2)
            mortemob(locais, indanimal, nomeanimal, tecla1, dinheiroanimal, expanimal, Nomejogador, Nomepet)
            break

        print(f'{nomeanimal}: {HPanimal}/{Vidaanimal}HP')
        sleep(1)

        nomemagia = Busca('Nome', 'MagiaJogador', 'one')
        tempomagia = Busca('tempo', 'MagiaJogador', 'one')
        idmagia = Busca('Id', 'MagiaJogador', 'one')
        qtdemana = Busca('QtdeMana', 'Jogador', 'one')
        mana = Busca('Mana', 'Jogador', 'one')
        if tempomagia[0] == 1 and nomemagia[0] not in 'vazio':
            danomagia = Busca('Dano', 'MagiaJogador', 'one')
            if idmagia[0] == tecla1:
                chancemagia = randint(danomagia[0] - 10, danomagia[0])
                customana = Busca('Mana', 'MagiaJogador', 'one')
                customana = customana[0]
            else:
                chancemagia = 0
                customana = 0
            if mana[0] >= customana:

                # Jogador usa Magia
                print(f'{Nomejogador[0]}: \033[31m{chancemagia}\033[m de atack (magia)')
                sleep(2)
                HPanimal -= chancemagia
                updatemana = mana[0] - customana
                Update('Jogador', 'Mana', updatemana, mana[0])
                Update('MagiaJogador', 'Tempo', tempomagia[0] + 1, tempomagia[0])
                mana = Busca('Mana', 'Jogador', 'one')
                print(f'{Nomejogador[0]}: {mana[0]}/{qtdemana[0]} Mana')
                sleep(3)

                if HPanimal <= 0:
                    print(f'{Nomejogador[0]} matou um(a): {nomeanimal}')
                    sleep(2)
                    mortemob(locais, indanimal, nomeanimal, tecla1, dinheiroanimal, expanimal, Nomejogador, Nomepet)
                    break

                print(f'{nomeanimal}: {HPanimal}/{Vidaanimal}HP')

            else:
                updatemana = mana[0] + 10
                Update('Jogador', 'Mana', updatemana, mana[0])
                mana = Busca('Mana', 'Jogador', 'one')
                print('Você recuperou +10 de mana')
                sleep(1)
                print(f'{Nomejogador[0]}: {mana[0]}/{qtdemana[0]} Mana')

        elif nomemagia[0] in '':
            pass
        else:
            if tempomagia[0] == 2:
                Update('MagiaJogador', 'Tempo', tempomagia[0] + 1, tempomagia[0])
            else:
                Update('MagiaJogador', 'Tempo', 1, tempomagia[0])

            if mana[0] <= qtdemana[0] - 10:
                updatemana = mana[0] + 10
                Update('Jogador', 'Mana', updatemana, mana[0])
                mana = Busca('Mana', 'Jogador', 'one')
                print('Você recuperou +10 de mana')
                sleep(1)
                print(f'{Nomejogador[0]}: {mana[0]}/{qtdemana[0]} Mana')
        print('-=' * 10)
        sleep(5)

        # Mob atack Jogador
        Vida = Busca('vida', 'Jogador', 'one')
        vida = Vida[0] - Danoanimal
        Update('Jogador', 'Vida', vida, Vida[0])
        print('{}: \033[32m{}\033[m de atack'.format(nomeanimal, Danoanimal))
        sleep(1)
        if vida <= 0:
            print('-=' * 10)
            print(f'{nomeanimal} matou {Nomejogador[0]}')
            sleep(5)
            BDP.mortejogador = 1
            BDP.perdaexp = expanimal
            break
        print(f'{Nomejogador[0]}: {vida}/{HP[0]}')
        sleep(1)
        qtdepot = Busca('*', 'Bolsa', 'all')
        if len(listapocao) > 0:

            # Jogador usa Pot
            if qtdepot[0][tecla3] - 1 > 0 and vida <= recquando:
                busca = BDP.Loja[tecla3][0]
                rec = vida + BDP.Loja[tecla3][2]
                if rec >= HP[0]:
                    Update('Jogador', 'Vida', HP[0], Vida[0])

                else:
                    Update('Jogador', 'Vida', rec, Vida[0])

                qtde = qtdepot[0][tecla3] - 1
                Update('Bolsa', busca, qtde, qtdepot[0][tecla3])
                print(f'Você usou uma poção {busca} (+{BDP.Loja[tecla3][2]} Vida)')
                sleep(4)
                Vida = Busca('Vida', 'Jogador', 'one')
                print(f'HP: {Vida[0]}/{HP[0]}')
                sleep(2)

        print('-=' * 10)
        sleep(5)

        if BDP.mortepet == 0:
            # Pet atack Mob
            if Nomepet[0] in '':
                pass
            else:
                if BDP.mortepet == 0:
                    idpet = Busca('Id', 'PetsJogador', 'one')
                    if idpet[0] == tecla1:
                        Danopet = Busca('Dano', 'PetsJogador', 'one')
                        Danopet = Danopet[0]
                    else:
                        Danopet = 0
                    HPanimal -= Danopet
                    print(f'Pet ({Nomepet[0]}): \033[32m{Danopet}\033[m de atack')
                    sleep(1)
                    if HPanimal <= 0:
                        print(f'{Nomepet[0]} matou um(a): {nomeanimal}')
                        sleep(2)
                        mortemob(locais, indanimal, nomeanimal, tecla1, dinheiroanimal, expanimal, Nomejogador, Nomepet)
                        break
                    print(f'{nomeanimal}: {HPanimal}/{Vidaanimal}HP')
                    print('-=' * 10)
                    sleep(5)

            # Mob atack Pet
            if Nomepet[0] in '':
                pass
            else:
                HPpet = Busca('HP', 'PetsJogador', 'one')
                Vidapet = Busca('Vida', 'PetsJogador', 'one')
                vida = Vidapet[0] - Danoanimal
                Update('PetsJogador', 'Vida', vida, Vidapet[0])
                print(f'{nomeanimal}: \033[32m{Danoanimal}\033[m de atack')
                sleep(1)
                if Vidapet[0] <= 0:
                    print(f'{nomeanimal} matou Pet ({Nomepet[0]})')
                    BDP.mortepet = 1
                    UpdateNome('Pets', 'Vida', HPpet[0], Nomepet[0])

                else:
                    print(f'Pet ({Nomepet[0]}): {vida}/{HPpet[0]}')
                print('-=' * 10)
                sleep(5)


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
                    tempoatack = Busca('TempoAtack', 'Habilidades', 'one')
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
                        Update('Habilidades', 'Defese', uplvdefese, lvdefese[0])
                        qtdeuptempo = uplvdefese * 60
                        Update('Habilidades', 'TempoDefese', qtdeuptempo, mnts)
                        break
                    Update('Habilidades', 'TempoDefese', mnts, tempodefese[0])
                    sleep(1)
                print('\nVocê upou sua habilidade de defese')


def lojapot(tecla2):
    while True:
        lvpocao = Busca('Level', 'Lojas', 'all')
        lvpocao = lvpocao[0][0]
        print('Loja de poções:')
        print('[0] Comprar poções')
        print('[1] Melhorar Loja de poções')
        print('[C] Voltar')
        while True:
            tecla = str(input("Tecla: ")).strip().upper()
            if tecla in '01C':
                break
            else:
                print('\033[31mErro:  \033[mOpção inválida, tente novamente')

        if tecla in 'C':
            break

        elif tecla in '0':
            lvmaximo = lvpocao
            if lvmaximo > 6:
                lvmaximo = 6
            for i in range(0, lvmaximo):
                print(f'[{i}] {BDP.Loja[i][0]} (+{BDP.Loja[i][2]}HP) = {BDP.Loja[i][1]} moedas')
            print('[C] Voltar')
            tecla1 = 10
            while True:
                strtecla = str(input('Tecla: ')).strip().upper()
                if strtecla.isnumeric():
                    tecla1 = int(strtecla)
                    if tecla1 < 0 or tecla1 >= lvpocao:
                        print('\033[31mErro:  \033[mOpção inválida, tente novamente')
                    else:
                        break
                else:
                    if strtecla in 'C':
                        break
                    print('\033[31mErro:  \033[mOpção inválida, tente novamente')
            if strtecla in 'C':
                pass
            else:
                while True:
                    Dinheiro = Busca('Dinheiro', 'Jogador', 'one')
                    maximo = (Dinheiro[0] - 1) / BDP.Loja[tecla1][1]
                    print(f'Compra Máxima de {trunc(maximo)} poções')
                    qtde = str(input(f'Quantidade de {BDP.Loja[tecla1][0]}: '))
                    if qtde.isnumeric():
                        qtde = int(qtde)
                        custo = BDP.Loja[tecla1][1] * qtde
                        if (Dinheiro[0] - 1) >= custo or qtde == 0:
                            break
                        else:
                            print('\033[33mErro: \033[mDinheiro insuficiente.')
                    else:
                        print('\033[31mErro:  \033[mOpção inválida, tente novamente')

                busca = BDP.Loja[tecla1][0]
                pagamento = (Dinheiro[0] - 1) - custo
                Update('Jogador', 'Dinheiro', pagamento, Dinheiro[0])
                buscapot = Busca('*', 'Bolsa', 'all')
                compra = buscapot[0][tecla1] + qtde
                Update('Bolsa', busca, compra, buscapot[0][tecla1])
                print(f'Você comprou {qtde} {busca} por {custo} moedas')

        if tecla in '1':
            MelhorarLoja(tecla2)


def lojaferramentas(tecla2):
    while True:
        lvferramentas = Busca('Level', 'Lojas', 'all')
        lvferramentas = lvferramentas[1][0]

        Diamante = Busca('Diamante', 'Jogador', 'one')
        Diamante = Diamante[0]

        print('Loja de Ferramentas:')
        print('[0] Comprar Picareta')
        print('[1] Comprar Machado')
        print('[2] Comprar Vara de Pesca')
        print('[3] Melhorar Loja de ferramentas')
        print('[C] Voltar')
        while True:
            tecla = str(input("Tecla: ")).strip().upper()
            if tecla in '0123C':
                break
            else:
                print('\033[31mErro:  \033[mOpção inválida, tente novamente')

        if tecla in 'C':
            break

        elif tecla in '0':
            if lvferramentas >= 4:
                lvferramentas = 4

            for i in range(0, lvferramentas):
                print(f'[{i}] {BDP.Picaretas[i][0]} ({BDP.Picaretas[i][1]} segundos) = {BDP.Picaretas[i][2]} diamantes')
            print('[C] Voltar')
            tecla1 = 10
            while True:
                strtecla = str(input('Tecla: ')).strip().upper()
                if strtecla.isnumeric():
                    tecla1 = int(strtecla)
                    if tecla1 < 0 or tecla1 >= lvferramentas:
                        print('\033[31mErro:  \033[mOpção inválida, tente novamente')
                    else:
                        break
                else:
                    if strtecla in 'C':
                        break
                    print('\033[31mErro:  \033[mOpção inválida, tente novamente')
            if strtecla in 'C':
                pass
            else:
                while True:
                    maximo = (Diamante - 1) / BDP.Picaretas[tecla1][2]
                    print(f'Compra Máxima de {trunc(maximo)} picaretas')
                    qtde = str(input(f'Quantidade de {BDP.Picaretas[tecla1][0]}: '))
                    if qtde.isnumeric():
                        qtde = int(qtde)
                        custo = BDP.Picaretas[tecla1][2] * qtde
                        if (Diamante - 1) >= custo or qtde == 0:
                            break
                        else:
                            print('\033[33mErro: \033[mDinheiro insuficiente.')
                    else:
                        print('\033[31mErro:  \033[mOpção inválida, tente novamente')

                busca = BDP.Picaretas[tecla1][0]
                pagamento = Diamante - custo
                Update('Jogador', 'Diamante', pagamento, Diamante)
                buscapicareta = Busca('Qtde', 'Picaretas', 'all')
                compra = buscapicareta[tecla1][0] + qtde
                Update('Picaretas', 'Qtde', compra, busca)
                print(f'Você comprou {qtde} {busca} por {custo} diamantes')
                sleep(1)

        elif tecla in '1':
            if lvferramentas >= 4:
                lvferramentas = 4

            for i in range(0, lvferramentas):
                print(f'[{i}] {BDP.Machados[i][0]} ({BDP.Machados[i][1]} segundos) = {BDP.Machados[i][2]} diamantes')
            print('[C] Voltar')
            tecla1 = 10
            while True:
                strtecla = str(input('Tecla: ')).strip().upper()
                if strtecla.isnumeric():
                    tecla1 = int(strtecla)
                    if tecla1 < 0 or tecla1 >= lvferramentas:
                        print('\033[31mErro:  \033[mOpção inválida, tente novamente')
                    else:
                        break
                else:
                    if strtecla in 'C':
                        break
                    print('\033[31mErro:  \033[mOpção inválida, tente novamente')
            if strtecla in 'C':
                pass
            else:
                while True:
                    maximo = (Diamante - 1) / BDP.Machados[tecla1][2]
                    print(f'Compra Máxima de {trunc(maximo)} machados')
                    qtde = str(input(f'Quantidade de {BDP.Machados[tecla1][0]}: '))
                    if qtde.isnumeric():
                        qtde = int(qtde)
                        custo = BDP.Machados[tecla1][2] * qtde
                        if (Diamante - 1) >= custo or qtde == 0:
                            break
                        else:
                            print('\033[33mErro: \033[mDinheiro insuficiente.')
                    else:
                        print('\033[31mErro:  \033[mOpção inválida, tente novamente')

                busca = BDP.Machados[tecla1][0]
                pagamento = Diamante - custo
                Update('Jogador', 'Diamante', pagamento, Diamante)
                buscamachados = Busca('Qtde', 'Machados', 'all')
                compra = buscamachados[tecla1][0] + qtde
                UpdateNome('Machados', 'Qtde', compra, busca)
                print(f'Você comprou {qtde} {busca} por {custo} diamantes')
                sleep(1)

        elif tecla in '2':
            if lvferramentas >= 4:
                lvferramentas = 2
            else:
                lvferramentas = 1

            for i in range(0, lvferramentas):
                print(f'[{i}] {BDP.VaraPesca[i][0]} ({BDP.VaraPesca[i][1]} segundos) = {BDP.VaraPesca[i][2]} diamantes')
            print('[C] Voltar')
            tecla1 = 10
            while True:
                strtecla = str(input('Tecla: ')).strip().upper()
                if strtecla.isnumeric():
                    tecla1 = int(strtecla)
                    if tecla1 < 0 or tecla1 >= lvferramentas:
                        print('\033[31mErro:  \033[mOpção inválida, tente novamente')
                    else:
                        break
                else:
                    if strtecla in 'C':
                        break
                    print('\033[31mErro:  \033[mOpção inválida, tente novamente')
            if strtecla in 'C':
                pass
            else:
                while True:
                    maximo = (Diamante - 1) / BDP.VaraPesca[tecla1][2]
                    print(f'Compra Máxima de {trunc(maximo)} machados')
                    qtde = str(input(f'Quantidade de {BDP.VaraPesca[tecla1][0]}: '))
                    if qtde.isnumeric():
                        qtde = int(qtde)
                        custo = BDP.VaraPesca[tecla1][2] * qtde
                        if (Diamante - 1) >= custo or qtde == 0:
                            break
                        else:
                            print('\033[33mErro: \033[mDinheiro insuficiente.')
                    else:
                        print('\033[31mErro:  \033[mOpção inválida, tente novamente')

                busca = BDP.VaraPesca[tecla1][0]
                pagamento = Diamante - custo
                Update('Jogador', 'Diamante', pagamento, Diamante)
                buscamachados = Busca('Qtde', 'VaraPesca', 'all')
                compra = buscamachados[tecla1][0] + qtde
                UpdateNome('VaraPesca', 'Qtde', compra, busca)
                print(f'Você comprou {qtde} {busca} por {custo} diamantes')
                sleep(1)

        elif tecla in '3':
            MelhorarLoja(tecla2)


def lojapet(tecla2):
    while True:
        lvlojapet = Busca('Level', 'Lojas', 'all')
        print('Lojas de Pets')
        print('[0] Comprar Pets')
        print('[1] Melhorar Loja de Pets')
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
            lista = []
            precopet = Busca('Preco', 'Pets', 'all')
            print('Pets:')
            sleep(1)
            for posmapa in range(0, lvlojapet[2][0]):
                for pos, mobs in enumerate(BDP.mobs[posmapa]):
                    if mobs[0] in BDP.pets[posmapa]:
                        print(f'[{posmapa}] {BDP.mobs[posmapa][pos][0]} = {precopet[posmapa][0]} diamantes')
                        lista.append(str(posmapa))

            print('[C] Voltar')
            if len(lista) >= 1:
                while True:
                    tecla1 = str(input('Tecla: ')).strip().upper()
                    if tecla1 in lista or tecla1 in 'C':
                        break
                    else:
                        print('\033[31mErro:  \033[mOpção inválida, tente novamente')

                if tecla1 in 'C':
                    pass

                elif tecla1 in lista:
                    tecla1 = int(tecla1)
                    diamante = Busca('Diamante', 'Jogador', 'one')
                    qtdepet = Busca('Qtde', 'Pets', 'all')
                    qtdemorte = Busca('Morte', BDP.locais[tecla1], 'all')
                    if qtdemorte[tecla1][0] - 1 >= 2:
                        if qtdepet[tecla1][0] - 1 == 0:
                            if diamante[0] - 1 >= precopet[tecla1][0]:
                                ganhopet = qtdepet[tecla1][0] + 1
                                custo = diamante[0] - precopet[tecla1][0]
                                UpdateNome('Pets', 'Qtde', ganhopet, BDP.pets[tecla1][0])
                                Update('Jogador', 'Diamante', custo, diamante[0])
                                print(f'Você comprou 1 Pet {BDP.pets[tecla1][0]} por {precopet[tecla1][0]} diamantes')
                                sleep(3)
                            else:
                                print('\033[33mErro: \033[mDiamante insuficiente.')
                                sleep(1)
                        else:
                            print('Você já tem esse Pet')
                            sleep(2)
                    else:
                        print(f'Você precisa matar no mínimo 650 {BDP.pets[tecla1]}')
                        sleep(2)
                for i in lista:
                    lista.remove(i)
            else:
                print('Sem Pets')
                sleep(1)

        elif tecla in '1':
            MelhorarLoja(tecla2)


def lojamagia(tecla2):
    while True:
        lvlojamagia = Busca('Level', 'Lojas', 'all')
        lvlojamagia = lvlojamagia[3][0]
        print('Lojas de Magias')
        print('[0] Comprar Magias')
        print('[1] Melhorar Loja de Magias')
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
            Preco = Busca('Preco', 'Magias', 'all')
            lvmaximo = lvlojamagia
            lvmagia = Busca('Lv', 'Magias', 'all')
            if lvmaximo > 18:
                lvmaximo = 18
            for i in range(0, lvmaximo):
                Mana = Busca('Mana', 'Magias', 'all')
                Dano = Busca('Dano', 'Magias', 'all')
                print(f'[{i}] {BDP.magias[i][0]} Lv.{lvmagia[i][0]} ({Mana[i][0]} Mana) ({Dano[i][0]} Dano) ='
                      f' {Preco[i][0]} Diamantes')
            print('[C] Voltar')
            tecla1 = 0
            while True:
                strtecla = str(input('Tecla: ')).strip().upper()
                if strtecla.isnumeric():
                    tecla1 = int(strtecla)
                    if tecla1 < 0 or tecla1 >= lvlojamagia:
                        print('\033[31mErro:  \033[mOpção inválida, tente novamente')
                    else:
                        break
                else:
                    if strtecla in 'C':
                        break
                    print('\033[31mErro:  \033[mOpção inválida, tente novamente')
            if strtecla in 'C':
                pass
            else:
                lvjogador = Busca('Level', 'Jogador', 'one')
                lvminmagia = Busca('Lvmin', 'Magias', 'all')
                if lvjogador[0] >= lvminmagia[tecla1][0]:
                    Diamante = Busca('Diamante', 'Jogador', 'one')
                    Qtde = Busca('Qtde', 'Magias', 'all')
                    if (Qtde[tecla1][0] - 1) == 0:
                        if (Diamante[0] - 1) >= Preco[tecla1][0]:
                            busca = BDP.magias[tecla1][0]
                            pagamento = (Diamante[0] - 1) - Preco[tecla1][0]
                            Update('Jogador', 'Diamante', pagamento, Diamante[0])
                            buscamagia = Busca('*', 'Magias', 'all')
                            compra = buscamagia[tecla1][6] + 1
                            UpdateNome('Magias', 'Qtde', compra, buscamagia[tecla1][0])
                            print(f'Você comprou {1} magia de {busca} por {Preco[tecla1][0]} diamantes')
                            sleep(3)

                        else:
                            print('\033[33mErro: \033[mDiamante insuficiente.')
                            sleep(1)
                    else:
                        print('\033[33mErro: \033[mVocê já tem essa magia.')
                        sleep(1)
                else:
                    print(f'\033[33mErro: \033[mLevel insuficiente. Level Nescessário: {lvminmagia[tecla1][0]}')
                    sleep(2)

        elif tecla in '1':
            MelhorarLoja(tecla2)


def MelhorarLoja(tecla2):
    lvloja = Busca('Level', 'Lojas', 'all')
    lvloja = lvloja[tecla2][0]
    itens = Busca('*', 'Itens', 'all')
    QtdeMadeiras = itens[0][0] - 1
    QtdePedras = itens[0][1] - 1
    QtdePeixes = itens[0][2] - 1
    QtdeCouros = itens[0][3] - 1

    preco = Busca('*', 'Lojas', 'all')
    precomadeiras = preco[tecla2][2]
    precopedras = preco[tecla2][3]
    precopeixes = preco[tecla2][4]
    precocouros = preco[tecla2][5]

    print(f'Loja de {BDP.TipoLojas[tecla2]} Level: {lvloja}')
    print(f'[0] Melhorar Loja = {QtdeMadeiras}/{precomadeiras} Madeiras, {QtdePedras}/{precopedras} Pedras', end='')
    if tecla2 == 0:
        print(f', {QtdePeixes}/{precopeixes} Peixes')
    elif tecla2 == 3:
        print(f', {QtdeCouros}/{precocouros} Couros')
    else:
        print()
    print('[C] Voltar')
    while True:
        tecla1 = str(input('Tecla: ')).strip().upper()
        if tecla1 in '0C':
            break
        else:
            print('\033[31mErro:  \033[mOpção inválida, tente novamente')

    if tecla1 in 'C':
        pass

    elif tecla1 in '0':
        while True:
            if tecla2 == 0:
                if QtdePeixes >= precopeixes:
                    pass
                else:
                    print('\033[33mErro: \033[mPeixes insuficiente.')
                    sleep(2)
                    break

            if tecla2 == 3:
                if QtdeCouros >= precocouros:
                    pass
                else:
                    print('\033[33mErro: \033[mCouros insuficiente.')
                    sleep(2)
                    break

            if QtdeMadeiras >= precomadeiras:
                if QtdePedras >= precopedras:
                    customadeiras = QtdeMadeiras - precomadeiras
                    custopedras = QtdePedras - precopedras
                    Update('Itens', 'Madeiras', customadeiras, QtdeMadeiras)
                    Update('Itens', 'Pedras', custopedras, QtdePedras)

                    aumentomadeiras = precomadeiras + 20
                    aumentopedras = precopedras + 20
                    UpdateNome('Lojas', 'CustoMadeiras', aumentomadeiras, 'Poções')
                    UpdateNome('Lojas', 'CustoPedras', aumentopedras, 'Poções')

                    if tecla2 == 0:
                        custopeixes = QtdePeixes - precopeixes
                        Update('Itens', 'Peixes', custopeixes, QtdePeixes)
                        aumentopeixes = precopeixes + 20
                        UpdateNome('Lojas', 'CustoPeixes', aumentopeixes, BDP.TipoLojas[tecla2])

                    if tecla2 == 3:
                        custocouros = QtdeCouros - precocouros
                        Update('Itens', 'Couros', custocouros, QtdeCouros)
                        aumentocouros = precocouros + 20
                        UpdateNome('Lojas', 'CustoCouros', aumentocouros, BDP.TipoLojas[tecla2])

                    uplv = lvloja + 1
                    UpdateNome('Lojas', 'Level', uplv, BDP.TipoLojas[tecla2])
                    print(f'Up Loja de {BDP.TipoLojas[tecla2]} Lv.{uplv}')
                    sleep(2)
                else:
                    print('\033[33mErro: \033[mPedras insuficiente.')
                    sleep(2)
            else:
                print('\033[33mErro: \033[mMadeiras insuficiente.')
                sleep(2)
            break


def RecuperarHP():
    lista = []
    while True:
        vida = Busca('Vida', 'Jogador', 'one')
        HP = Busca('HP', 'Jogador', 'one')
        if vida[0] == HP[0]:
            print("HP cheio")
            sleep(1)
            break
        print('Usar qual poção:')
        for i in range(0, len(BDP.Loja)):
            qtdepot = Busca('*', 'Bolsa', 'all')
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
        Vida = Busca('Vida', 'Jogador', 'one')
        rec = Vida[0] + BDP.Loja[tecla3][2]
        if rec >= HP[0]:
            Update('Jogador', 'Vida', HP[0], Vida[0])

        else:
            Update('Jogador', 'Vida', rec, Vida[0])

        for i in lista:
            lista.remove(i)

        qtdepot = Busca('*', 'Bolsa', 'one')
        qtde = qtdepot[tecla3] - 1
        Update('Bolsa', busca, qtde, qtdepot[tecla3])
        HP = Busca('HP', 'Jogador', 'one')
        print(f'HP: {Vida[0]}/{HP[0]}')
        sleep(1)
        break


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


Connecte()
