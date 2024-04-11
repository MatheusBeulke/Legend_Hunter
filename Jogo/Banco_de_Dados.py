import sqlite3
from Inicio import inicio


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

    #                                                 Nome,   Lv,  HP, D, DF, E, D, M
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



Connecte()
