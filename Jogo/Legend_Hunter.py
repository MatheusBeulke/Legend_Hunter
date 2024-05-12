from time import sleep
from math import trunc
from random import randint
import sqlite3
from pathlib import Path


class Jogador:
    def __init__(self):
        banco = sqlite3.connect('Banco_Dados.db')
        cursor = banco.cursor()
        self.nome = cursor.execute('SELECT Nome FROM Jogador').fetchone()[0]
        self.lv = cursor.execute('SELECT Level FROM Jogador').fetchone()[0]
        self.hp = cursor.execute('SELECT HP FROM Jogador').fetchone()[0]
        self.vida = cursor.execute('SELECT Vida FROM Jogador').fetchone()[0]
        self.mana = cursor.execute('SELECT Mana FROM Jogador').fetchone()[0]
        self.qtdemana = cursor.execute('SELECT QtdeMana FROM Jogador').fetchone()[0]
        self.qtdeexp = cursor.execute('SELECT QtdeExp FROM Jogador').fetchone()[0] - 1
        self.exp = cursor.execute('SELECT EXP FROM Jogador').fetchone()[0]
        self.dinheiro = cursor.execute('SELECT Dinheiro FROM Jogador').fetchone()[0] - 1
        self.diamante = cursor.execute('SELECT Diamante FROM Jogador').fetchone()[0] - 1
        self.pontos = cursor.execute('SELECT Pontos FROM Jogador').fetchone()[0] - 1


class Morte:
    def __init__(self):
        banco = sqlite3.connect('Banco_Dados.db')
        cursor = banco.cursor()
        self.mortejogador = cursor.execute('SELECT MorteJogador FROM Morte').fetchone()[0]  # 1 - Vivo
        self.tatack = cursor.execute('SELECT TAtack FROM Morte').fetchone()[0]
        self.tdefese = cursor.execute('SELECT TDefese FROM Morte').fetchone()[0]
        self.qtdemorte = cursor.execute('SELECT QtdeMorte FROM Morte').fetchone()[0] - 1
        self.mortepet = cursor.execute('SELECT MortePet FROM Morte').fetchone()[0]  # 2 - Morto


class Itens:
    def __init__(self, ind='0'):
        banco = sqlite3.connect('Banco_Dados.db')
        cursor = banco.cursor()
        self.nome = cursor.execute('SELECT Nome FROM Itens').fetchall()[int(ind)][0]
        self.qtde = cursor.execute('SELECT Qtde FROM Itens').fetchall()[int(ind)][0] - 1


class Mapas:
    def __init__(self, ind):
        banco = sqlite3.connect('Banco_Dados.db')
        cursor = banco.cursor()
        self.nome = cursor.execute('SELECT Nome FROM Mapa').fetchall()[ind][0]
        self.qtdemob = cursor.execute('SELECT QtdeMob FROM Mapa').fetchall()[ind][0]


class Mobs:
    def __init__(self, local, ind=0):
        banco = sqlite3.connect('Banco_Dados.db')
        cursor = banco.cursor()
        self.nome = cursor.execute('SELECT Nome FROM "' + str(local) + '"').fetchall()[ind][0]
        self.lv = cursor.execute('SELECT Level FROM "' + str(local) + '"').fetchall()[ind][0]
        self.hp = cursor.execute('SELECT HP FROM "' + str(local) + '"').fetchall()[ind][0]
        self.dano = cursor.execute('SELECT Dano FROM "' + str(local) + '"').fetchall()[ind][0]
        self.danoelementar = cursor.execute('SELECT DanoElementar FROM "' + str(local) + '"').fetchall()[ind][0]
        self.exp = cursor.execute('SELECT Exp FROM "' + str(local) + '"').fetchall()[ind][0]
        self.dinheiro = cursor.execute('SELECT Dinheiro FROM "' + str(local) + '"').fetchall()[ind][0]
        self.morte = cursor.execute('SELECT Morte FROM "' + str(local) + '"').fetchall()[ind][0] - 1


class Fragmentos:
    def __init__(self, ind=0):
        banco = sqlite3.connect('Banco_Dados.db')
        cursor = banco.cursor()
        self.nome = cursor.execute('SELECT Nome FROM Fragmentos').fetchall()[ind][0]
        self.nomec = cursor.execute('SELECT NomeC FROM Fragmentos').fetchall()[ind][0]
        self.qtde = cursor.execute('SELECT Qtde FROM Fragmentos').fetchall()[ind][0] - 1


class Atributos:
    def __init__(self):
        banco = sqlite3.connect('Banco_Dados.db')
        cursor = banco.cursor()
        self.defesa = cursor.execute('SELECT Defese FROM Atributos').fetchone()[0]
        self.atack = cursor.execute('SELECT Atack FROM Atributos').fetchone()[0]


class Skill:
    def __init__(self):
        banco = sqlite3.connect('Banco_Dados.db')
        cursor = banco.cursor()
        self.defesa = cursor.execute('SELECT Defese FROM Habilidades').fetchone()[0]
        self.tempodefesa = cursor.execute('SELECT TempoDefese FROM Habilidades').fetchone()[0]
        self.atack = cursor.execute('SELECT Atack FROM Habilidades').fetchone()[0]
        self.tempoatack = cursor.execute('SELECT TempoAtack FROM Habilidades').fetchone()[0]


class Pet:
    def __init__(self, ind=0):
        banco = sqlite3.connect('Banco_Dados.db')
        cursor = banco.cursor()
        self.nome = cursor.execute('SELECT Nome FROM Pets').fetchall()[ind][0]
        self.lv = cursor.execute('SELECT Level FROM Pets').fetchall()[ind][0]
        self.hp = cursor.execute('SELECT HP FROM Pets').fetchall()[ind][0]
        self.vida = cursor.execute('SELECT Vida FROM Pets').fetchall()[ind][0]
        self.dano = cursor.execute('SELECT Dano FROM Pets').fetchall()[ind][0]
        self.qtde = cursor.execute('SELECT Qtde FROM Pets').fetchall()[ind][0] - 1
        self.exp = cursor.execute('SELECT Exp FROM Pets').fetchall()[ind][0] - 1
        self.qtdeExp = cursor.execute('SELECT QtdeExp FROM Pets').fetchall()[ind][0]
        self.preco = cursor.execute('SELECT Preco FROM Pets').fetchall()[ind][0]
        self.id = cursor.execute('SELECT Id FROM Pets').fetchall()[ind][0]
        self.ind = cursor.execute('SELECT Ind FROM Pets').fetchall()[ind][0]


class PetJogador:
    def __init__(self):
        banco = sqlite3.connect('Banco_Dados.db')
        cursor = banco.cursor()
        self.nome = cursor.execute('SELECT Nome FROM PetsJogador').fetchone()[0]
        self.lv = cursor.execute('SELECT Level FROM PetsJogador').fetchone()[0]
        self.hp = cursor.execute('SELECT HP FROM PetsJogador').fetchone()[0]
        self.vida = cursor.execute('SELECT Vida FROM PetsJogador').fetchone()[0]
        self.dano = cursor.execute('SELECT Dano FROM PetsJogador').fetchone()[0]
        self.id = cursor.execute('SELECT id FROM PetsJogador').fetchone()[0]


class Lojas:
    def __init__(self, loja=0):
        banco = sqlite3.connect('Banco_Dados.db')
        cursor = banco.cursor()
        self.nome = cursor.execute('SELECT Nome FROM Lojas').fetchall()[loja][0]
        self.lv = cursor.execute('SELECT Level FROM Lojas').fetchall()[loja][0]
        self.customadeiras = cursor.execute('SELECT CustoMadeiras FROM Lojas').fetchall()[loja][0]
        self.custopedras = cursor.execute('SELECT CustoPedras FROM Lojas').fetchall()[loja][0]
        self.custopeixes = cursor.execute('SELECT CustoPeixes FROM Lojas').fetchall()[loja][0]
        self.custocouros = cursor.execute('SELECT CustoCouros FROM Lojas').fetchall()[loja][0]


class Picaretas:
    def __init__(self, ind=0):
        banco = sqlite3.connect('Banco_Dados.db')
        cursor = banco.cursor()
        self.nome = cursor.execute('SELECT Nome FROM Picaretas').fetchall()[ind][0]
        self.eficiencia = cursor.execute('SELECT Eficiencia FROM Picaretas').fetchall()[ind][0]
        self.preco = cursor.execute('SELECT Preco FROM Picaretas').fetchall()[ind][0]
        self.qtde = cursor.execute('SELECT Qtde FROM Picaretas').fetchall()[ind][0] - 1


class Machados:
    def __init__(self, ind=0):
        banco = sqlite3.connect('Banco_Dados.db')
        cursor = banco.cursor()
        self.nome = cursor.execute('SELECT Nome FROM Machados').fetchall()[ind][0]
        self.eficiencia = cursor.execute('SELECT Eficiencia FROM Machados').fetchall()[ind][0]
        self.preco = cursor.execute('SELECT Preco FROM Machados').fetchall()[ind][0]
        self.qtde = cursor.execute('SELECT Qtde FROM Machados').fetchall()[ind][0] - 1


class VaraPesca:
    def __init__(self, ind=0):
        banco = sqlite3.connect('Banco_Dados.db')
        cursor = banco.cursor()
        self.nome = cursor.execute('SELECT Nome FROM VaraPesca').fetchall()[ind][0]
        self.eficiencia = cursor.execute('SELECT Eficiencia FROM VaraPesca').fetchall()[ind][0]
        self.preco = cursor.execute('SELECT Preco FROM VaraPesca').fetchall()[ind][0]
        self.qtde = cursor.execute('SELECT Qtde FROM VaraPesca').fetchall()[ind][0] - 1


class Armas:
    def __init__(self, ind=0):
        banco = sqlite3.connect('Banco_Dados.db')
        cursor = banco.cursor()
        self.nome = cursor.execute('SELECT Nome FROM Armas').fetchall()[ind][0]
        self.lv = cursor.execute('SELECT Lv FROM Armas').fetchall()[ind][0]
        self.dano = cursor.execute('SELECT Dano FROM Armas').fetchall()[ind][0]
        self.preco = cursor.execute('SELECT Preco FROM Armas').fetchall()[ind][0]
        self.rec = cursor.execute('SELECT Rec FROM Armas').fetchall()[ind][0]
        self.atack = cursor.execute('SELECT Atack FROM Armas').fetchall()[ind][0]
        self.qtde = cursor.execute('SELECT Qtde FROM Armas').fetchall()[ind][0] - 1
        self.id = cursor.execute('SELECT Id FROM Armas').fetchall()[ind][0]


class ArmaJogador:
    def __init__(self):
        banco = sqlite3.connect('Banco_Dados.db')
        cursor = banco.cursor()
        self.nome = cursor.execute('SELECT Nome FROM EspadaJogador').fetchone()[0]
        self.lv = cursor.execute('SELECT Lv FROM EspadaJogador').fetchone()[0]
        self.dano = cursor.execute('SELECT Dano FROM EspadaJogador').fetchone()[0]
        self.rec = cursor.execute('SELECT Rec FROM EspadaJogador').fetchone()[0]
        self.atack = cursor.execute('SELECT Atack FROM EspadaJogador').fetchone()[0]
        self.id = cursor.execute('SELECT Id FROM EspadaJogador').fetchone()[0]


class Magias:
    def __init__(self, ind=0):
        banco = sqlite3.connect('Banco_Dados.db')
        cursor = banco.cursor()
        self.nome = cursor.execute('SELECT Nome FROM Magias').fetchall()[ind][0]
        self.lv = cursor.execute('SELECT Lv FROM Magias').fetchall()[ind][0]
        self.mana = cursor.execute('SELECT Mana FROM Magias').fetchall()[ind][0]
        self.dano = cursor.execute('SELECT Dano FROM Magias').fetchall()[ind][0]
        self.preco = cursor.execute('SELECT Preco FROM Magias').fetchall()[ind][0]
        self.lvmin = cursor.execute('SELECT Lvmin FROM Magias').fetchall()[ind][0]
        self.tempo = cursor.execute('SELECT tempo FROM Magias').fetchall()[ind][0]
        self.qtde = cursor.execute('SELECT Qtde FROM Magias').fetchall()[ind][0] - 1
        self.id = cursor.execute('SELECT Id FROM Magias').fetchall()[ind][0]


class MagiaJogador:
    def __init__(self):
        banco = sqlite3.connect('Banco_Dados.db')
        cursor = banco.cursor()
        self.nome = cursor.execute('SELECT Nome FROM MagiaJogador').fetchone()[0]
        self.lv = cursor.execute('SELECT Lv FROM MagiaJogador').fetchone()[0]
        self.mana = cursor.execute('SELECT Mana FROM MagiaJogador').fetchone()[0]
        self.dano = cursor.execute('SELECT Dano FROM MagiaJogador').fetchone()[0]
        self.tempo = cursor.execute('SELECT tempo FROM MagiaJogador').fetchone()[0]
        self.id = cursor.execute('SELECT Id FROM MagiaJogador').fetchone()[0]


class PocoesHP:
    def __init__(self, ind=0):
        banco = sqlite3.connect('Banco_Dados.db')
        cursor = banco.cursor()
        self.nome = cursor.execute('SELECT Nome FROM Bolsa').fetchall()[ind][0]
        self.rec = cursor.execute('SELECT Rec FROM Bolsa').fetchall()[ind][0]
        self.qtde = cursor.execute('SELECT Qtde FROM Bolsa').fetchall()[ind][0] - 1
        self.preco = cursor.execute('SELECT Preco FROM Bolsa').fetchall()[ind][0]


class PocoesMana:
    def __init__(self, ind=0):
        banco = sqlite3.connect('Banco_Dados.db')
        cursor = banco.cursor()
        self.nome = cursor.execute('SELECT Nome FROM PocaoMana').fetchall()[ind][0]
        self.rec = cursor.execute('SELECT Rec FROM PocaoMana').fetchall()[ind][0]
        self.qtde = cursor.execute('SELECT Qtde FROM PocaoMana').fetchall()[ind][0] - 1
        self.preco = cursor.execute('SELECT Preco FROM PocaoMana').fetchall()[ind][0]


class PocaoJogadorHP:
    def __init__(self):
        banco = sqlite3.connect('Banco_Dados.db')
        cursor = banco.cursor()
        self.nome = cursor.execute('SELECT Nome FROM PocaoJogador').fetchone()[0]
        self.uso = cursor.execute('SELECT uso FROM PocaoJogador').fetchone()[0]
        self.id = cursor.execute('SELECT Id FROM PocaoJogador').fetchone()[0]


class PocaoJogadorMana:
    def __init__(self):
        banco = sqlite3.connect('Banco_Dados.db')
        cursor = banco.cursor()
        self.nome = cursor.execute('SELECT Nome FROM PocaoJogadorMana').fetchone()[0]
        self.uso = cursor.execute('SELECT uso FROM PocaoJogadorMana').fetchone()[0]
        self.id = cursor.execute('SELECT Id FROM PocaoJogadorMana').fetchone()[0]


def linha(f):
    tamanho = len(f) + 4
    print('-' * tamanho)
    print(f'{f:^{tamanho}}')
    print('-' * tamanho)


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

    # Morte
    cursor.execute('CREATE TABLE Morte (Nome text, MorteJogador integer, TAtack integer, TDefese integer,'
                   ' QtdeMorte integer, MortePet integer)')

    cursor.execute("INSERT INTO Morte VALUES('" + nome + "', 1, 1, 1, 1, 1)")

    # Itens
    cursor.execute('CREATE TABLE Itens (Nome text, Qtde integer)')
    cursor.execute("INSERT INTO Itens VALUES('Madeiras', 1)")
    cursor.execute("INSERT INTO Itens VALUES('Pedras', 1)")
    cursor.execute("INSERT INTO Itens VALUES('Peixes', 1)")
    cursor.execute("INSERT INTO Itens VALUES('Couros', 1)")

    # Mapa
    cursor.execute('CREATE TABLE Mapa (Nome text, QtdeMob intege)')
    cursor.execute("INSERT INTO Mapa VALUES('Colina_Verde', 11)")
    cursor.execute("INSERT INTO Mapa VALUES('Deserto', 11)")
    cursor.execute("INSERT INTO Mapa VALUES('Caverna_de_Minerção', 10)")
    cursor.execute("INSERT INTO Mapa VALUES('Floresta_Sombria', 15)")
    cursor.execute("INSERT INTO Mapa VALUES('Polo_Norte', 8)")
    cursor.execute("INSERT INTO Mapa VALUES('Eletrico', 7)")
    cursor.execute("INSERT INTO Mapa VALUES('Vulcão', 6)")


    # MobsColinaVerde
    cursor.execute('CREATE TABLE Colina_Verde (Nome text, Level integer, HP integer, Dano integer,'
                   'DanoElementar integer, Exp integer, Dinheiro integer, Morte integer)')

    #                                                Nome,   Lv,  HP, D, DF, E, D, M
    cursor.execute("INSERT INTO Colina_Verde VALUES('Rats', 1, 12, 7 , 2, 5, 3, 1)")
    cursor.execute("INSERT INTO Colina_Verde VALUES('Crow', 15, 40, 25, 4, 17, 15, 1)")
    cursor.execute("INSERT INTO Colina_Verde VALUES('Wolf', 30, 70, 47, 6, 34, 29, 1)")
    cursor.execute("INSERT INTO Colina_Verde VALUES('Lizard', 45, 102, 71, 8, 53, 45, 1)")
    cursor.execute("INSERT INTO Colina_Verde VALUES('Slime', 60, 136, 97, 10, 74, 63, 1)")
    cursor.execute("INSERT INTO Colina_Verde VALUES('Assasin', 75, 172, 125, 12, 97, 83, 1)")
    cursor.execute("INSERT INTO Colina_Verde VALUES('Bear', 90, 210, 155, 14, 122, 105, 1)")
    cursor.execute("INSERT INTO Colina_Verde VALUES('Goblin', 105, 250, 187, 16, 149, 129, 1)")
    cursor.execute("INSERT INTO Colina_Verde VALUES('Minotaur', 120, 292, 221, 18, 178, 155, 1)")
    cursor.execute("INSERT INTO Colina_Verde VALUES('Peixes', 0, 0, 0, 0, 0, 0, 0)")
    cursor.execute("INSERT INTO Colina_Verde VALUES('Boss', 1, 800, 400, 100, 1000, 500, 1)")

    # Deserto
    cursor.execute('CREATE TABLE Deserto (Nome text, Level integer, HP integer, Dano integer,'
                   ' DanoElementar integer, Exp integer, Dinheiro integer, Morte integer)')

    #                                               Nome,    Lv,   HP,  D, DF   E,   D,  M
    cursor.execute("INSERT INTO Deserto VALUES('Scorpion', 135, 350, 300, 24, 230, 200, 1)")
    cursor.execute("INSERT INTO Deserto VALUES('Snake', 150, 378, 320, 26, 245, 212, 1)")
    cursor.execute("INSERT INTO Deserto VALUES('Worm', 165, 408, 342, 28, 262, 226, 1)")
    cursor.execute("INSERT INTO Deserto VALUES('Scarab', 180, 440, 366, 30, 281, 242, 1)")
    cursor.execute("INSERT INTO Deserto VALUES('Cactus', 195, 474, 392, 32, 302, 260, 1)")
    cursor.execute("INSERT INTO Deserto VALUES('Raptor', 210, 510, 420, 34, 325, 280, 1)")
    cursor.execute("INSERT INTO Deserto VALUES('Mummy', 225, 548, 450, 36, 350, 302, 1)")
    cursor.execute("INSERT INTO Deserto VALUES('Pharao', 240, 588, 482, 38, 377, 326, 1)")
    cursor.execute("INSERT INTO Deserto VALUES('Anubis', 255, 630, 516, 40, 406, 352, 1)")
    cursor.execute("INSERT INTO Deserto VALUES('Sandstone Golem', 270, 674, 552, 42, 437, 380, 1)")
    cursor.execute("INSERT INTO Deserto VALUES('Boss', 1, 1200, 900, 100, 1500, 1000, 1)")

    # Caverna de Minerção
    cursor.execute('CREATE TABLE Caverna_de_Minerção (Nome text, Level integer, HP integer, Dano integer,'
                   ' DanoElementar ingeter, Exp integer, Dinheiro integer, Morte integer)')

    #                                                       Nome,  Lv,  HP,  D, DF,  E,    D,  M
    cursor.execute("INSERT INTO Caverna_de_Minerção VALUES('Bat', 285, 700, 580, 44, 450, 400, 1)")
    cursor.execute("INSERT INTO Caverna_de_Minerção VALUES('Gigantula', 300, 728, 600, 46, 465, 412, 1)")
    cursor.execute("INSERT INTO Caverna_de_Minerção VALUES('Dwarf', 315, 758, 622, 48, 482, 426, 1)")
    cursor.execute("INSERT INTO Caverna_de_Minerção VALUES('Miner', 330, 790, 646, 50, 501, 442, 1)")
    cursor.execute("INSERT INTO Caverna_de_Minerção VALUES('Troll', 345, 824, 672, 52, 522, 460, 1)")
    cursor.execute("INSERT INTO Caverna_de_Minerção VALUES('Orc', 360, 850, 700, 54, 545, 480, 1)")
    cursor.execute("INSERT INTO Caverna_de_Minerção VALUES('Djinn', 375, 888, 730, 56, 570, 502, 1)")
    cursor.execute("INSERT INTO Caverna_de_Minerção VALUES('Ciclops', 390, 948, 762, 58, 597, 526, 1)")
    cursor.execute("INSERT INTO Caverna_de_Minerção VALUES('Pedras', 0, 0, 0, 0, 0, 0, 0)")
    cursor.execute("INSERT INTO Caverna_de_Minerção VALUES('Boss', 1, 1700, 1400, 100, 2000, 1500, 1)")

    # Floresta Sombria
    cursor.execute('CREATE TABLE Floresta_Sombria (Nome text, Level integer, HP integer, Dano integer,'
                   ' DanoElementar integer, Exp integer, Dinheiro integer, Morte integer)')

    #                                                       Nome,      Lv,   HP,  D, DF,  E,    D,  M
    cursor.execute("INSERT INTO Floresta_Sombria VALUES('Skeleton', 405, 986, 804, 60, 626, 549, 1)")
    cursor.execute("INSERT INTO Floresta_Sombria VALUES('Zombie', 420, 1014, 824, 62, 641, 561, 1)")
    cursor.execute("INSERT INTO Floresta_Sombria VALUES('Ghost', 435, 1044, 846, 64, 658, 575, 1)")
    cursor.execute("INSERT INTO Floresta_Sombria VALUES('Witch', 450, 1076, 870, 66, 677, 591, 1)")
    cursor.execute("INSERT INTO Floresta_Sombria VALUES('Lich', 465, 1110, 896, 68, 698, 609, 1)")
    cursor.execute("INSERT INTO Floresta_Sombria VALUES('Shandow', 480, 1146, 924, 70, 721, 629, 1)")
    cursor.execute("INSERT INTO Floresta_Sombria VALUES('Phanton Flame', 495, 1184, 954, 72, 746, 651, 1)")
    cursor.execute("INSERT INTO Floresta_Sombria VALUES('Phanton Fiend', 510, 1224, 986, 74, 773, 675, 1)")
    cursor.execute("INSERT INTO Floresta_Sombria VALUES('Skeleton Dragon', 525, 1266, 1020, 76, 802, 701, 1)")
    cursor.execute("INSERT INTO Floresta_Sombria VALUES('Gargoyle', 540, 1310, 1056, 78, 833, 729, 1)")
    cursor.execute("INSERT INTO Floresta_Sombria VALUES('Spectral Flame', 555, 1356, 1094, 80, 866, 759, 1)")
    cursor.execute("INSERT INTO Floresta_Sombria VALUES('Spcetral Fiend', 570, 1404, 1134, 82, 901, 791, 1)")
    cursor.execute("INSERT INTO Floresta_Sombria VALUES('Vampire', 585, 1454, 1176, 84, 938, 825, 1)")
    cursor.execute("INSERT INTO Floresta_Sombria VALUES('Madeira', 0, 0, 0, 0, 0, 0, 0)")
    cursor.execute("INSERT INTO Floresta_Sombria VALUES('Boss', 1, 2300, 1900, 100, 2500, 2000, 1)")

    # Icy
    cursor.execute('CREATE TABLE Polo_Norte (Nome text, Level integer, HP integer, Dano integer, DanoElementar integer,'
                   ' Exp integer, Dinheiro integer, Morte integer)')

    #                                            Nome,      Lv,   HP,   D,  DF    E,   D,  M
    cursor.execute("INSERT INTO Polo_Norte VALUES('Icy Flame', 600, 1500, 1200, 86, 970, 850, 1)")
    cursor.execute("INSERT INTO Polo_Norte VALUES('Snow Golem', 615, 1528, 1220, 88, 985, 862, 1)")
    cursor.execute("INSERT INTO Polo_Norte VALUES('Mammoth', 630, 1558, 1242, 90, 1002, 876, 1)")
    cursor.execute("INSERT INTO Polo_Norte VALUES('Yeti', 645, 1590, 1266, 92, 1021, 892, 1)")
    cursor.execute("INSERT INTO Polo_Norte VALUES('Icy Wizard', 660, 1624, 1292, 94, 1042, 910, 1)")
    cursor.execute("INSERT INTO Polo_Norte VALUES('Icy Dragon', 675, 1660, 1320, 96, 1065, 930, 1)")
    cursor.execute("INSERT INTO Polo_Norte VALUES('Icy Fiend', 690, 1698, 1350, 98, 1090, 952, 1)")
    cursor.execute("INSERT INTO Polo_Norte VALUES('Boss', 1, 3000, 2400, 100, 3000, 2500, 1)")

    # Eletrico
    cursor.execute('CREATE TABLE Eletrico (Nome text, Level integer, HP integer, Dano integer,'
                   'DanoElementar integer, Exp integer, Dinheiro integer, Morte integer)')

    #                                                  Nome,           Lv,  HP,   D,  DF,   E,  D,  M
    cursor.execute("INSERT INTO Eletrico VALUES('Electric Flame', 705, 1750, 1400, 100, 1150, 1000, 1)")
    cursor.execute("INSERT INTO Eletrico VALUES('Electric Golem', 720, 1778, 1420, 102, 1165, 1012, 1)")
    cursor.execute("INSERT INTO Eletrico VALUES('Electric Yeti', 735, 1808, 1442, 104, 1182, 1026, 1)")
    cursor.execute("INSERT INTO Eletrico VALUES('Electric Wizard', 750, 1840, 1466, 106, 1201, 1042, 1)")
    cursor.execute("INSERT INTO Eletrico VALUES('Electric Dragon', 765, 1874, 1492, 108, 1222, 1060, 1)")
    cursor.execute("INSERT INTO Eletrico VALUES('Electric Fiend', 780, 1910, 1520, 110, 1245, 1080, 1)")
    cursor.execute("INSERT INTO Eletrico VALUES('Boss', 1, 3800, 2900, 100, 3500, 3000, 1)")

    # Fogo
    cursor.execute('CREATE TABLE Vulcão (Nome text, Level integer, HP integer, Dano integer,'
                   'DanoElementar integer, Exp integer, Dinheiro integer, Morte integer)')

    #                                            Nome,   Lv,  HP,   D,    DF,  E,    D,    M
    cursor.execute("INSERT INTO Vulcão VALUES('Flame', 795, 1960, 1580, 112, 1270, 1100, 1)")
    cursor.execute("INSERT INTO Vulcão VALUES('Fire Golem', 810, 1988, 1600, 114, 1285, 1112, 1)")
    cursor.execute("INSERT INTO Vulcão VALUES('Wizard', 825, 2018, 1622, 116, 1302, 1126, 1)")
    cursor.execute("INSERT INTO Vulcão VALUES('Dragon', 840, 2050, 1646, 118, 1321, 1142, 1)")
    cursor.execute("INSERT INTO Vulcão VALUES('Demon', 855, 2084, 1672, 120, 1342, 1160, 1)")
    cursor.execute("INSERT INTO Vulcão VALUES('Boss', 1, 4700, 3400, 100, 4000, 3500, 1)")

    # Fragmentos
    cursor.execute('CREATE TABLE Fragmentos (NomeC integer, Nome text, Qtde integer)')
    cursor.execute("INSERT INTO Fragmentos VALUES('Fragmento de Hit', 'FragmentoHit', 1)")
    cursor.execute("INSERT INTO Fragmentos VALUES('Fragmento de Ar', 'FragmentoAr', 1)")
    cursor.execute("INSERT INTO Fragmentos VALUES('Fragmento de Psíquico', 'FragmentoPsiquico', 1)")
    cursor.execute("INSERT INTO Fragmentos VALUES('Fragmento de Alma', 'FragmentoAlma', 1)")
    cursor.execute("INSERT INTO Fragmentos VALUES('Fragmento de Gelo', 'FragmentoGelo', 1)")
    cursor.execute("INSERT INTO Fragmentos VALUES('Fragmento de Raio', 'FragmentoEletrico', 1)")
    cursor.execute("INSERT INTO Fragmentos VALUES('Fragmento de Fogo', 'FragmentoFire', 1)")

    # Atributos
    cursor.execute('CREATE TABLE Atributos (Defese integer, Atack integer )')
    cursor.execute("INSERT INTO Atributos VALUES(1, 4)")

    # Skill
    cursor.execute('CREATE TABLE Habilidades (Defese integer, TempoDefese integer, Atack integer, TempoAtack integer)')
    cursor.execute("INSERT INTO Habilidades VALUES(1, 60, 1, 60)")

    # Pet
    cursor.execute('CREATE TABLE Pets (Nome text, Level integer, HP integer, Vida integer, Dano integer, Qtde integer, '
                   'Exp integer, QtdeExp integer, Preco integer, Id integer, Ind integer)')
    cursor.execute("INSERT INTO Pets VALUES('Wolf', 1, 50, 50, 5, 1, 1, 100, 100, 0, 2)")
    cursor.execute("INSERT INTO Pets VALUES('Scorpion', 1, 330, 330, 25, 1, 1, 100, 200, 1, 0)")
    cursor.execute("INSERT INTO Pets VALUES('Troll', 1, 800, 800, 45, 1, 1, 100, 300, 2, 4)")
    cursor.execute("INSERT INTO Pets VALUES('Shandow', 1, 1126, 1126, 65, 1, 1, 100, 400, 3, 5)")
    cursor.execute("INSERT INTO Pets VALUES('Icy Dragon', 1, 1640, 1640, 85, 1, 1, 100, 500, 4, 5)")
    cursor.execute("INSERT INTO Pets VALUES('Electric Yeti', 1, 1780, 1780, 105, 1, 1, 100, 600, 5, 2)")
    cursor.execute("INSERT INTO Pets VALUES('Demon', 1, 1988, 1988, 125, 1, 1, 100, 700, 6, 4)")

    # PetsJogador
    cursor.execute('CREATE TABLE PetsJogador (Nome text, Level integer, HP integer, Vida integer, Dano integer,'
                   'id integer)')
    cursor.execute("INSERT INTO PetsJogador VALUES('vazio', 1, 1, 1, 1, 1)")

    # Lojas
    cursor.execute('CREATE TABLE Lojas (Nome text, Level integer, CustoMadeiras integer, CustoPedras integer,'
                   'CustoPeixes integer, CustoCouros integer)')
    cursor.execute('INSERT INTO Lojas VALUES("Poções", 1, 10, 20, 30, 0)')
    cursor.execute('INSERT INTO Lojas VALUES("Ferramentas", 1, 10, 30, 0, 0)')
    cursor.execute('INSERT INTO Lojas VALUES("Pets", 1, 20, 30, 0, 0)')
    cursor.execute('INSERT INTO Lojas VALUES("Magias", 1, 10, 20, 0, 20)')
    cursor.execute('INSERT INTO Lojas VALUES("Armas", 1, 20, 30, 0, 0)')

    # Picaretas
    cursor.execute('CREATE TABLE Picaretas (Nome text, Eficiencia integer, Preco integer, Qtde integer)')
    cursor.execute('INSERT INTO Picaretas VALUES("Picareta Inicial", 90, 50, 1)')
    cursor.execute('INSERT INTO Picaretas VALUES("Picareta de Ferro", 60, 100, 1)')
    cursor.execute('INSERT INTO Picaretas VALUES("Picareta de Titanio", 30, 150, 1)')
    cursor.execute('INSERT INTO Picaretas VALUES("Picareta dos Deuses", 15, 200, 1)')

    # Machados
    cursor.execute('CREATE TABLE Machados (Nome text, Eficiencia integer, Preco integer, Qtde integer)')
    cursor.execute('INSERT INTO Machados VALUES("Machado Inicial", 60, 20, 1)')
    cursor.execute('INSERT INTO Machados VALUES("Machado de Ferro", 40, 40, 1)')
    cursor.execute('INSERT INTO Machados VALUES("Machado de Titanio", 20, 60, 1)')
    cursor.execute('INSERT INTO Machados VALUES("Machado dos Deuses", 10, 80, 1)')

    # Vara de Pesca
    cursor.execute('CREATE TABLE VaraPesca (Nome text, Eficiencia integer, Preco integer, Qtde integer)')
    cursor.execute('INSERT INTO VaraPesca VALUES("Vara de Pesca", 40, 30, 1)')
    cursor.execute('INSERT INTO VaraPesca VALUES("Vara de Pesca com Comida", 20, 60, 1)')

    # Armas
    cursor.execute(
        'CREATE TABLE Armas (Nome text, Lv integer, Dano integer, Preco integer, Rec integer, Atack integer, '
        'Qtde integer, Id integer)')
    cursor.execute('INSERT INTO Armas VALUES("Espada Inicial", 1, 1, 50, 1, 1, 1, 0)')
    cursor.execute('INSERT INTO Armas VALUES("Espada Longa", 135, 8, 500, 8, 1, 1, 1)')  # scorpion
    cursor.execute('INSERT INTO Armas VALUES("Espada Dupla", 285, 26, 1500, 20, 1, 1, 2)')  # Bat
    cursor.execute('INSERT INTO Armas VALUES("Espada Sombria", 405, 40, 2000, 25, 1, 1, 3)')  # Skeleton
    cursor.execute('INSERT INTO Armas VALUES("Espada Icy", 600, 50, 3000, 34, 1, 1, 4)')  # Icy
    cursor.execute('INSERT INTO Armas VALUES("Espada Eletric", 705, 56, 3500, 36, 1, 1, 5)')  # Eletric
    cursor.execute('INSERT INTO Armas VALUES("Espada Fire", 795, 62, 40600, 40, 1, 1, 6)')  # Fire

    # EspadaJogador
    cursor.execute('CREATE TABLE EspadaJogador (Nome text, Lv integer, Dano integer, Rec integer, Atack integer, '
                   'Id integer)')
    cursor.execute("INSERT INTO EspadaJogador VALUES('vazio', 1, 1, 1, 1, 1)")

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

    # Poções
    cursor.execute('CREATE TABLE Bolsa (Nome text, Rec integer,Qtde integer, Preco integer)')

    cursor.execute("INSERT INTO Bolsa VALUES('PoçãoPequena', 20, 1, 50)")
    cursor.execute("INSERT INTO Bolsa VALUES('PoçãoMédia', 50, 1, 100)")
    cursor.execute("INSERT INTO Bolsa VALUES('PoçãoGrande', 100, 1, 200)")
    cursor.execute("INSERT INTO Bolsa VALUES('PoçãoGigante', 200, 1, 400)")
    cursor.execute("INSERT INTO Bolsa VALUES('HiperPoção', 400, 1, 800)")
    cursor.execute("INSERT INTO Bolsa VALUES('PoçãoMagica', 800, 1, 1600)")
    cursor.execute("INSERT INTO Bolsa VALUES('PoçãoCelestial', 1600, 1, 3200)")

    # Poções Mana
    cursor.execute('CREATE TABLE PocaoMana (Nome text, Rec integer, Qtde integer, Preco iteger)')

    cursor.execute("INSERT INTO PocaoMana VALUES('PoçãoPequena', 20, 1, 30)")
    cursor.execute("INSERT INTO PocaoMana VALUES('PoçãoMédia',  50, 1, 80)")
    cursor.execute("INSERT INTO PocaoMana VALUES('PoçãoGrande', 100, 1, 180)")
    cursor.execute("INSERT INTO PocaoMana VALUES('PoçãoGigante', 200, 1, 380)")
    cursor.execute("INSERT INTO PocaoMana VALUES('HiperPoção', 400, 1, 780)")
    cursor.execute("INSERT INTO PocaoMana VALUES('PoçãoMagica', 800, 1, 1580)")
    cursor.execute("INSERT INTO PocaoMana VALUES('PoçãoCelestial', 1600, 1, 3180)")

    # Poções Jogador
    cursor.execute('CREATE TABLE PocaoJogador (Nome text, uso integer, Id integer)')
    cursor.execute("INSERT INTO PocaoJogador VALUES('vazio', 1, 1)")

    cursor.execute('CREATE TABLE PocaoJogadorMana (Nome text, uso integer, Id integer)')
    cursor.execute("INSERT INTO PocaoJogadorMana VALUES('vazio', 1, 1)")

    banco.commit()
    inicio()


def inicio():
    while True:
        print('Funções de controle:')
        print('[A] Batalhar')
        print('[B] Informações')
        print('[C] Loja')
        print('[D] Centro de Treinamento')
        print('[E] Equipamentos')
        while True:
            tecla = str(input('Tecla: ')).upper().strip()
            if tecla in 'ABCDE':
                break
            else:
                print('\033[31mErro:  \033[mOpção inválida, tente novamente')

        if tecla in 'A':
            while True:
                linha('MAPA')
                for num in range(0, 7):
                    local = Mapas(num)
                    print(f'[{num}] {str(local.nome).replace('_', ' ')}')
                print('[C] Voltar')
                while True:
                    tecla1 = str(input('Tecla: ')).strip().upper()
                    if tecla1 in 'C':
                        break
                    elif 0 <= int(tecla1) < 7:
                        break
                    else:
                        print('\033[31mErro:  \033[mOpção inválida, tente novamente')

                if tecla1 in 'C':
                    break
                else:
                    tecla1 = int(tecla1)
                    locais = Mapas(tecla1).nome
                    Mapa(locais, tecla1)

        elif tecla in 'B':
            while True:
                linha('Informações')
                print('[0] Personagem')
                print('[1] Atributos')
                print('[2] Quantidade de mob matado')
                print('[C] Voltar')
                while True:
                    tecla1 = str(input('Tecla: ')).strip().upper()
                    if tecla1 in '012C':
                        break
                    else:
                        print('\033[31mErro:  \033[mOpção inválida, tente novamente')
                if tecla1 in 'C':
                    break

                elif tecla1 in '0':
                    jogador = Jogador()
                    morte = Morte()
                    print(f'Nome: {jogador.nome}')
                    print(f'Level: {jogador.lv}')
                    print(f'Exp: {jogador.qtdeexp}/{jogador.exp}')
                    print(f'Dinheiro: {jogador.dinheiro}')
                    print(f'Diamante: {jogador.diamante}')
                    print(f'Quantidade de Morte: {morte.qtdemorte}')
                    sleep(2)

                elif tecla1 in '1':
                    atributos()

                elif tecla1 in '2':
                    linha('Quantidade de Mobs Matados')
                    sleep(1)
                    Mortesmobs()

        elif tecla in 'C':
            linha('Lojas')
            while True:
                print('[0] Loja de Poções')
                print('[1] Loja de Ferramentas')
                print('[2] Loja de Pets')
                print('[3] Loja de Magias')
                print('[4] Loja de Armas')
                print('[C] Voltar')
                while True:
                    tecla2 = str(input('Tecla: ')).strip().upper()
                    if tecla2 in '01234C':
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

                elif tecla2 in '4':
                    lojaarmas(int(tecla2))

        elif tecla in 'D':
            habilidades()

        elif tecla in 'E':
            while True:
                linha('EQUIPAMENTOS')
                print('[0] Fragmentos')
                print('[1] Mochila')
                print('[2] Ferramentas')
                print('[3] Armas')
                print('[4] Pets')
                print('[5] Magias')
                print('[6] Poções')
                print('[C] Voltar')
                while True:
                    tecla1 = str(input('Tecla: ')).upper().strip()
                    if tecla1 in '0123456C':
                        break
                    else:
                        print('\033[31mErro:  \033[mOpção inválida, tente novamente')
                if tecla1 in 'C':
                    break

                elif tecla1 in '0':
                    linha('Quantidade de Fragmentos')
                    for num in range(0, 7):
                        fragmentos = Fragmentos(num)
                        if fragmentos.qtde >= 1:
                            print(f'{fragmentos.nomec} = {fragmentos.qtde}')
                    sleep(1)

                elif tecla1 in '1':
                    linha('Mochila')
                    for pos in range(0, 4):
                        items = Itens(pos)
                        if items.qtde > 0:
                            print(f'{items.nome} = {items.qtde}')
                            sleep(1)
                    sleep(2)

                elif tecla1 in '2':
                    linha('Ferramentas')
                    for pos in range(0, 4):
                        picaretas = Picaretas(pos)
                        if picaretas.qtde >= 1:
                            print(f'{picaretas.nome} = {picaretas.qtde}')
                            sleep(1)
                    sleep(1)

                    for pos in range(0, 4):
                        machados = Machados(pos)
                        if machados.qtde >= 1:
                            print(f'{machados.nome} = {machados.qtde}')
                            sleep(1)
                    sleep(1)

                    for pos in range(0, 2):
                        varapesca = VaraPesca(pos)
                        if varapesca.qtde >= 1:
                            print(f'{varapesca.nome} = {varapesca.qtde}')
                            sleep(1)
                    sleep(1)

                elif tecla1 in '3':
                    while True:
                        linha('Armas')
                        print('[0] Escolher Arma')
                        print('[1] Melhorar Arma')
                        print('[C] Voltar')
                        while True:
                            tecla2 = str(input('Tecla: ')).strip().upper()
                            if tecla2 in '01C':
                                break
                            else:
                                print('\033[31mErro:  \033[mOpção inválida, tente novamente')

                        if tecla2 in 'C':
                            break

                        lista = []
                        for pos in range(0, 7):
                            Espadas = Armas(pos)
                            fragmentos = Fragmentos(pos)
                            if Espadas.qtde >= 1:
                                lista.append(pos)
                                if tecla2 in '0':
                                    if len(lista) == 1:
                                        linha('Usar qual Espada durante a batalha')
                                    print(f'[{pos}] {Espadas.nome} Lv.{Espadas.lv} = ({Espadas.dano} Dano) '
                                          f'({Espadas.atack} Atack) ({Espadas.rec} Rec)')
                                    sleep(1)
                                elif tecla2 in '1':
                                    if len(lista) == 1:
                                        linha('Melhorar qual Espada')
                                    print(f'[{pos}] {Espadas.nome} Lv.{Espadas.lv} ({Espadas.dano} Dano)'
                                          f' ({Espadas.atack} Atack) ({Espadas.rec} Rec) = 1 '
                                          f'{fragmentos.nomec}')
                                    sleep(0.5)

                        if len(lista) >= 1:
                            print('[C] Voltar')
                            while True:
                                escolha = str(input('Tecla: ')).strip().upper()
                                if escolha.isnumeric():
                                    escolha = int(escolha)
                                    if escolha in lista:
                                        fragmentos = Fragmentos(escolha)
                                        if tecla2 in '1' and fragmentos.qtde >= 1:
                                            break
                                        elif tecla2 in '0':
                                            break
                                        else:
                                            print('\033[33mErro: \033[mFragmentos insuficiente.')
                                    else:
                                        print('\033[31mErro:  \033[mOpção inválida, tente novamente')
                                elif escolha in 'C':
                                    break
                                else:
                                    print('\033[31mErro:  \033[mOpção inválida, tente novamente')
                            if str(escolha) in 'C':
                                pass
                            else:
                                Espadas = Armas(escolha)
                                if tecla2 in '0':
                                    armajg = ArmaJogador()
                                    UpdateNome('EspadaJogador', 'Id', Espadas.id, armajg.nome)
                                    UpdateNome('EspadaJogador', 'Lv', Espadas.lv, armajg.nome)
                                    UpdateNome('EspadaJogador', 'Dano', Espadas.dano, armajg.nome)
                                    UpdateNome('EspadaJogador', 'Atack', Espadas.atack, armajg.nome)
                                    UpdateNome('EspadaJogador', 'Rec', Espadas.rec, armajg.nome)
                                    UpdateNome('EspadaJogador', 'Nome', Espadas.nome, armajg.nome)
                                    print(f'Você escolheu usar a {Espadas.nome}')
                                    sleep(2)

                                elif tecla2 in '1':
                                    fragmentos = Fragmentos(escolha)
                                    UpdateNome('Armas', 'Dano', Espadas.dano + 1, Espadas.nome)
                                    UpdateNome('Armas', 'Rec', Espadas.rec + 1, Espadas.nome)
                                    UpdateNome('Armas', 'Lv', Espadas.lv + 1, Espadas.nome)
                                    UpdateNome('Fragmentos', 'Qtde', fragmentos.qtde, fragmentos.nome)
                                    armaj = ArmaJogador()
                                    if armaj.nome not in 'vazio':
                                        UpdateNome('EspadaJogador', 'Dano', armaj.dano + 1, armaj.nome)
                                        UpdateNome('EspadaJogador', 'Rec', armaj.rec + 1, armaj.nome)
                                        UpdateNome('EspadaJogador', 'Lv', armaj.lv + 1, armaj.nome)
                                    linha('MELHORIA DA ESPADA')
                                    Espadas = Armas(escolha)
                                    print(f'Você melhorou a {Espadas.nome}: \ndano {Espadas.dano}'
                                          f'\natack {Espadas.atack} \nrec {Espadas.rec}')
                                    sleep(3)

                elif tecla1 in '4':
                    linha('Pets')
                    lista = []
                    for pos in range(0, 7):
                        pets = Pet(pos)
                        if pets.qtde == 1:
                            lista.append(pos)
                            if len(lista) == 1:
                                print('Usar qual Pet durante a batalha:')
                                sleep(1)
                            print(f'[{pos}] {pets.nome} (Lv.{pets.lv}) ({pets.vida}/{pets.hp}HP) ({pets.dano} Dano)')
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
                            petjg = PetJogador()
                            pets = Pet(escolha)
                            UpdateNome('PetsJogador', 'Id', pets.id, petjg.nome)
                            UpdateNome('PetsJogador', 'Level', pets.lv, petjg.nome)
                            UpdateNome('PetsJogador', 'HP', pets.hp, petjg.nome)
                            UpdateNome('PetsJogador', 'Vida', pets.vida, petjg.nome)
                            UpdateNome('PetsJogador', 'Dano', pets.dano, petjg.nome)
                            UpdateNome('PetsJogador', 'Nome', pets.nome, petjg.nome)
                            print(f'Você escolheu usar o Pet {pets.nome}')
                            sleep(2)
                    sleep(2)

                elif tecla1 in '5':
                    linha('Magias')
                    lista = []
                    for pos in range(0, 7):
                        magias = Magias(pos)
                        if magias.qtde == 1:
                            lista.append(pos)
                            if len(lista) == 1:
                                print('Usar qual Magia durante a batalha:')
                                sleep(1)
                            print(
                                f'[{pos}] {magias.nome} ({magias.dano - 10}-{magias.dano} dano)'
                                f' ({magias.mana} mana)')
                            sleep(1)

                    if len(lista) == 0:
                        sleep(2)
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
                            magiajg = MagiaJogador()
                            magias = Magias(escolha)
                            UpdateNome('MagiaJogador', 'Dano', magias.dano, magiajg.nome)
                            UpdateNome('MagiaJogador', 'Mana', magias.mana, magiajg.nome)
                            UpdateNome('MagiaJogador', 'Id', magias.id, magiajg.nome)
                            UpdateNome('MagiaJogador', 'Nome', magias.nome, magiajg.nome)
                            print(f'Você escolheu usar a magia {magias.nome}')
                            sleep(3)

                elif tecla1 in '6':
                    linha('Poções')
                    while True:
                        print('[0] Poções de Vida')
                        print('[1] Poções de Mana')
                        print('[C] Voltar')
                        while True:
                            tecla3 = str(input('Tecla: ')).strip().upper()
                            if tecla3 in '01C':
                                break
                            else:
                                print('\033[31mErro:  \033[mOpção inválida, tente novamente')
                        if tecla3 in 'C':
                            break
                        listapocao = []
                        for pos in range(0, 7):
                            if tecla3 in '0':
                                pocoes = PocoesHP(pos)
                                f = f'[{pos}] {pocoes.nome} (+{pocoes.rec}HP) = {pocoes.qtde}'
                            else:
                                pocoes = PocoesMana(pos)
                                f = f'[{pos}] {pocoes.nome} (+{pocoes.rec}Mana) = {pocoes.qtde}'
                            if pocoes.qtde > 0:
                                listapocao.append(str(pos))
                                if len(listapocao) == 1:
                                    print('Usar qual Poção durante a batalha:')
                                print(f)

                        if len(listapocao) > 0:
                            while True:
                                tecla4 = str(input('tecla: ')).strip().upper()
                                if tecla4 in listapocao:
                                    break
                                else:
                                    print('\033[31mErro:  \033[mOpção inválida, tente novamente')
                            jogador = Jogador()
                            if tecla3 in '0':
                                Barra = jogador.hp
                                f = 'Vida'
                                fron = 'PocaoJogador'
                                pocaojg = PocaoJogadorHP()
                                pocoes = PocoesHP(int(tecla4))
                            else:
                                Barra = jogador.qtdemana
                                f = 'Mana'
                                fron = 'PocaoJogadorMana'
                                pocaojg = PocaoJogadorMana()
                                pocoes = PocoesMana(int(tecla4))

                            while True:
                                strtecla = str(input(f'Usar a poção quando a {f} estiver menor ou igual a: '))
                                if strtecla.isnumeric():
                                    recquando = int(strtecla)
                                    if Barra >= recquando >= 0:
                                        tecla4 = int(tecla4)
                                        break
                                    else:
                                        print('\033[31mErro:  \033[mOpção inválida, tente novamente')
                                else:
                                    print('\033[31mErro:  \033[mOpção inválida, tente novamente')

                            pot = pocoes.nome
                            UpdateNome(fron, 'uso', recquando, pocaojg.nome)
                            UpdateNome(fron, 'Id', tecla4, pocaojg.nome)
                            UpdateNome(fron, 'Nome', pot, pocaojg.nome)
                            print(
                                F'Você usará a {pot} quando sua {f} estiver menor ou igual a {recquando}/{Barra}')
                            sleep(3)


def Mapa(locais, tecla1):
    while True:
        linha('Mobs')
        mapa = Mapas(tecla1)
        boss = randint(1, 100)
        if boss <= 2:
            maxi = mapa.qtdemob
            for num in range(0, maxi):
                mob = Mobs(locais, num)
                print(f'[{num}] {mob.nome}')
        else:
            maxi = mapa.qtdemob - 1
            for num in range(0, maxi):
                mob = Mobs(locais, num)
                print(f'[{num}] {mob.nome}')

        print('[C] Voltar')
        while True:
            tecla2 = str(input('Tecla: ')).strip().upper()
            if tecla2 in '':
                print('\033[31mErro:  \033[mOpção inválida, tente novamente')

            elif tecla2 in 'C':
                break

            elif 0 <= int(tecla2) < maxi:
                break
            else:
                print('\033[31mErro:  \033[mOpção inválida, tente novamente')

        if tecla2 in 'C':
            break

        tecla2 = int(tecla2)
        mobs = Mobs(locais, tecla2)

        if mobs.nome not in ['Madeira', 'Pedras', 'Peixes']:
            pass
        else:
            coletaitens(locais, tecla2)
            break
        print(f'Você encontrou um(a): {mobs.nome}')
        sleep(3)
        print('-=' * 20)
        HPanimal, Danoanimal = infobatalha(locais, tecla1, tecla2)
        print(f'Mob: {mobs.nome} Lv.{mobs.lv:.0f} \nHP: {HPanimal} \nDano: {Danoanimal}'
              f' \nDinheiro: {mobs.dinheiro} \nExp: {mobs.exp}')
        print('-=' * 20)
        sleep(3)

        atributo = Atributos()
        Espada = ArmaJogador()
        pet = PetJogador()
        magia = MagiaJogador()
        skill = Skill()
        jogador = Jogador()
        if Espada.id == tecla1 and Espada.nome not in 'vazio':
            atack = atributo.atack + skill.atack + Espada.atack + Espada.dano
        else:
            atack = atributo.atack + skill.atack

        print(f'Jogador: {jogador.nome} Lv.{jogador.lv}\nHP: {jogador.vida}/{jogador.hp} \nMana: {jogador.mana}/'
              f'{jogador.qtdemana} \nDano: {atack - 4}-{atack}\nDefesa: {atributo.defesa + skill.defesa}')
        if Espada.nome not in 'vazio' and tecla1 == Espada.id:
            print(f'Rec: {Espada.rec}')

        if pet.nome not in 'vazio' and tecla1 == pet.id:
            print(f'Pet: {pet.nome} ({pet.vida}/{pet.hp}HP) ({pet.dano} Dano)')
            sleep(1)

        if magia.nome not in 'vazio' and tecla1 == magia.id:
            print(f'Magia: ({magia.dano - 10}-{magia.dano} Dano) ({magia.mana} Mana)')
            sleep(1)

        print('-=' * 20)
        sleep(3)
        while True:
            print('[0] Atacar')
            print('[1] Recuar')
            tecla3 = str(input('Tecla: ')).strip()
            if tecla3 in '01':
                break
            else:
                print('\033[31mErro:  \033[mOpção inválida, tente novamente')
        if tecla3 in '1':
            pass
        elif tecla3 in '0':
            if mobs.nome in 'Boss':
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
            for v in range(1, atacar + 1):
                if v > 1:
                    print(f'Você encontrou outro(a) {mobs.nome}')
                    sleep(2)
                HPanimal, Danoanimal = infobatalha(locais, tecla1, tecla2)
                batalha(locais, tecla1, tecla2, HPanimal, Danoanimal, atack)
                morte = Morte()
                if morte.mortejogador == 2:
                    UpdateNome('Morte', 'MorteJogador', 1, jogador.nome)
                    break


def infobatalha(locais, tecla1, tecla2):
    mobs = Mobs(locais, tecla2)
    jogador = Jogador()
    atributo = Atributos()
    skill = Skill()
    fragmentos = Fragmentos(tecla1)

    diferencaelementar = mobs.danoelementar - fragmentos.qtde
    if diferencaelementar < 0:
        diferencaelementar = 0
    diferencalv = mobs.lv - jogador.lv

    defesa = atributo.defesa + skill.defesa
    HPanimal = mobs.hp
    Danoanimal = mobs.dano + diferencaelementar - defesa
    if jogador.lv >= mobs.lv or diferencalv <= 0:
        if mobs.nome in 'Boss':
            Danoanimal = mobs.dano + diferencaelementar - defesa - (jogador.lv - 1)
        pass
    else:
        HPanimal = mobs.hp + diferencalv
        Danoanimal = mobs.dano + diferencalv + diferencaelementar - defesa

    if Danoanimal < 0:
        Danoanimal = 0

    return HPanimal, Danoanimal


def batalha(locais, tecla1, tecla2, HPanimal, Danoanimal, atack):
    mobs = Mobs(locais, tecla2)
    Espada = ArmaJogador()
    Vidaanimal = HPanimal
    while True:
        jogador = Jogador()
        # Jogador ataca Mob
        jogadoratack = randint(atack - 4, atack)
        print('-=' * 10)
        print(f'{jogador.nome}: \033[31m{jogadoratack}\033[m de atack')
        HPanimal -= jogadoratack
        sleep(1)

        if Espada.nome not in 'vazio':
            if jogador.vida + Espada.rec <= jogador.hp:
                vidajogador = jogador.vida + Espada.rec
                UpdateNome('Jogador', 'Vida', vidajogador, jogador.nome)
                print(f'{jogador.nome} recuperou +{Espada.rec} de vida: {vidajogador}/{jogador.hp}')
            sleep(1)

        if HPanimal <= 0:
            print('-=' * 10)
            print(f'{jogador.nome} matou um(a): {mobs.nome}')
            sleep(2)
            mortemob(locais, tecla1, tecla2)
            break
        print(f'{mobs.nome}: {HPanimal}/{Vidaanimal}HP')
        # Jogador usa Mana
        PotManaJg = PocaoJogadorMana()
        PotMana = PocoesMana(PotManaJg.id)
        if PotMana.qtde > 0 and jogador.mana <= PotManaJg.uso:
            print(f'{jogador.nome} usou uma {PotManaJg.nome} (+{PotMana.rec} Mana)')
            sleep(2)
            jogador = Jogador()
            if PotManaJg.uso + jogador.mana >= jogador.qtdemana:
                UpdateNome('Jogador', 'Mana', jogador.qtdemana, jogador.nome)
            else:
                UpdateNome('Jogador', 'Mana', jogador.mana + PotMana.rec, jogador.nome)
            UpdateNome('PocaoMana', 'Qtde', PotMana.qtde, PotMana.nome)
            jogador = Jogador()
            print(f'{jogador.nome}: {jogador.mana}/{jogador.qtdemana} Mana')
            PotMana = PocoesMana(PotManaJg.id)
            print(f'Quantidade de {PotManaJg.nome}: {PotMana.qtde}')
            sleep(2)

        # Jogador usa Magia
        magia = MagiaJogador()
        if magia.tempo == 1 and magia.nome not in 'vazio':
            if magia.id == tecla1:
                chancemagia = randint(magia.dano - 10, magia.dano)
                customana = magia.mana
            else:
                chancemagia = customana = 0

            if jogador.mana >= customana:
                print(f'{jogador.nome}: \033[31m{chancemagia}\033[m de atack (magia)')
                sleep(2)
                HPanimal -= chancemagia
                Update('Jogador', 'Mana', jogador.mana - customana, jogador.mana)
                UpdateNome('MagiaJogador', 'Tempo', magia.tempo + 1, magia.nome)
                jogador = Jogador()
                print(f'{jogador.nome}: {jogador.mana}/{jogador.qtdemana} Mana')
                sleep(3)

                if HPanimal <= 0:
                    print('-=' * 10)
                    print(f'{jogador.nome} matou um(a): {mobs.nome}')
                    sleep(2)
                    mortemob(locais, tecla1, tecla2)
                    break

                print(f'{mobs.nome}: {HPanimal}/{Vidaanimal}HP')

        elif magia.nome in '':
            pass
        else:
            if magia.tempo == 2:
                UpdateNome('MagiaJogador', 'Tempo', magia.tempo + 1, magia.nome)
            else:
                UpdateNome('MagiaJogador', 'Tempo', 1, magia.nome)

        print('-=' * 10)
        sleep(5)

        # Mob atack Jogador
        jogador = Jogador()
        vidajogador = jogador.vida - Danoanimal
        Update('Jogador', 'Vida', vidajogador, jogador.vida)
        print('{}: \033[32m{}\033[m de atack'.format(mobs.nome, Danoanimal))
        sleep(1)
        morte = Morte()
        if vidajogador <= 0:
            print('-=' * 10)
            print(f'{mobs.nome} matou {jogador.nome}')
            sleep(5)
            mortejogador()
            break
        print(f'{jogador.nome}: {vidajogador}/{jogador.hp} HP')
        sleep(1)

        # Jogador usa Pot
        PotHPjg = PocaoJogadorHP()
        PotHP = PocoesHP(PotHPjg.id)
        jogador = Jogador()
        if PotHP.qtde > 0 and vidajogador <= PotHPjg.uso:
            if jogador.vida + PotHP.rec >= jogador.hp:
                UpdateNome('Jogador', 'Vida', jogador.hp, jogador.nome)

            else:
                UpdateNome('Jogador', 'Vida', jogador.vida + PotHP.rec, jogador.nome)

            UpdateNome('Bolsa', 'Qtde', PotHP.qtde, PotHP.nome)
            print(f'{jogador.nome} usou uma {PotHPjg.nome} (+{PotHP.rec} Vida)')
            sleep(4)
            jogador = Jogador()
            print(f'{jogador.nome}: {jogador.vida}/{jogador.hp} HP')
            PotHP = PocoesHP(PotHPjg.id)
            print(f'Quantidade de {PotHPjg.nome}: {PotHP.qtde}')
            sleep(2)

        print('-=' * 10)
        sleep(5)

        # Pet atack Mob
        pets = PetJogador()
        if pets.nome in 'vazio' or morte.mortepet == 2:
            pass
        else:
            if pets.id == tecla1:
                Danopet = pets.dano
            else:
                Danopet = 0
            HPanimal -= Danopet
            print(f'Pet ({pets.nome}): \033[32m{Danopet}\033[m de atack')
            sleep(1)
            if HPanimal <= 0:
                print('-=' * 10)
                print(f'{pets.nome} matou um(a): {mobs.nome}')
                sleep(2)
                mortemob(locais, tecla1, tecla2)
                break
            print(f'{mobs.nome}: {HPanimal}/{Vidaanimal}HP')
            print('-=' * 10)
            sleep(5)

            # Mob atack Pet
            vidapet = pets.vida - Danoanimal
            Update('PetsJogador', 'Vida', vidapet, pets.vida)
            print(f'{mobs.nome}: \033[32m{Danoanimal}\033[m de atack')
            sleep(1)
            if vidapet <= 0:
                print(f'{mobs.nome} matou Pet ({pets.nome})')
                Update('Morte', 'MortePet', 2, morte.mortepet)
                UpdateNome('PetsJogador', 'Vida', pets.hp, pets.nome)

            else:
                print(f'Pet ({pets.nome}): {vidapet}/{pets.hp}')
            sleep(5)


def mortejogador():
    jogador = Jogador()
    skill = Skill()
    morte = Morte()
    if morte.qtdemorte % 2 == 0:
        Update('Habilidades', 'TempoDefese', 600 + skill.tempodefesa, skill.tempodefesa)
        Update('Morte', 'TDefese', morte.tdefese + 600, morte.tdefese + 1)
        print('Você perdeu 10 minutos (600 segundos) na habilidade de defesa')
        sleep(2)
    else:
        Update('Habilidades', 'TempoAtack', skill.tempoatack + 600, skill.tempoatack)
        Update('Morte', 'TAtack', morte.tatack + 600, morte.tatack + 1)
        print('Você perdeu 10 minutos (600 segundos) na habilidade de atack')
        sleep(2)
    UpdateNome('Morte', 'MorteJogador', 2, jogador.nome)
    Update('Morte', 'MortePet', 1, morte.mortepet)
    Update('Morte', 'QtdeMorte', morte.qtdemorte + 2, morte.qtdemorte + 1)
    Update('Jogador', 'Vida', jogador.hp, jogador.vida)


def mortemob(locais, tecla1, tecla2):
    jogador = Jogador()
    mobs = Mobs(locais, tecla2)

    UpdateNome(locais, 'Morte', mobs.morte + 2, mobs.nome)
    UpdateNome('Jogador', 'Dinheiro', jogador.dinheiro + mobs.dinheiro + 1, jogador.nome)
    UpdateNome('Jogador', 'QtdeExp', jogador.qtdeexp + mobs.exp + 1, jogador.nome)
    jogador = Jogador()
    print(f'{jogador.nome} ganhou {mobs.dinheiro} moedas')
    print(f'{jogador.nome} tem {jogador.dinheiro} moedas')
    sleep(5)
    print(f'{jogador.nome} ganhou {mobs.exp} experiências')
    print(f'{jogador.nome} tem {jogador.qtdeexp}/{jogador.exp} experiência')
    sleep(5)

    # Drop Fragmentos
    if mobs.nome in 'Bear':
        chancecouro = randint(1, 100)
        if chancecouro <= 25:
            couros = Itens(ind='3')
            UpdateNome('Itens', 'Qtde', couros.qtde + 2, couros.nome)
            print(f'{jogador.nome} ganhou 1 couro')
            sleep(3)
    chancedrop = randint(1, 100)
    if chancedrop <= 5:
        fragmentos = Fragmentos(tecla1)
        print(f'{jogador.nome} ganhou 1 {fragmentos.nomec}')
        UpdateNome('Fragmentos', 'Qtde', fragmentos.qtde + 2, fragmentos.nome)
        sleep(3)
    print('-=' * 10)
    LevelAnimal(locais, tecla2)
    LvJogador()
    pets = PetJogador()
    if pets.nome in 'vazio':
        pass
    else:
        LvPet(locais, tecla2)


def LvJogador():
    while True:
        jogador = Jogador()
        if jogador.qtdeexp >= jogador.exp:
            Update('Jogador', 'Level', jogador.lv + 1, jogador.lv)
            UpdateNome('Jogador', 'EXP', jogador.exp * 2, jogador.nome)
            Update('Jogador', 'HP', jogador.hp + 10, jogador.hp)
            Update('Jogador', 'QtdeMana', jogador.mana + 10, jogador.qtdemana)
            jogador = Jogador()
            Update('Jogador', 'Vida', jogador.hp, jogador.vida)
            Update('Jogador', 'Mana', jogador.qtdemana, jogador.mana)
            UpdateNome('Jogador', 'Diamante', jogador.diamante + jogador.lv + 1, jogador.nome)
            UpdateNome('Jogador', 'Pontos', jogador.pontos + 2, jogador.nome)
            print(f'Up Lv.{jogador.lv}')
            sleep(1)
            print(f'Você ganhou {jogador.lv} diamantes')
            print('Você ganhou 1 ponto de atributos')
            sleep(1)
        else:
            break


def LevelAnimal(locais, tecla2):
    mobs = Mobs(locais, tecla2)
    if mobs.morte % 50 == 0:
        LvAnimal = mobs.morte / 50
        LvAnimal += mobs.lv
    else:
        LvAnimal = 0
    while True:
        if LvAnimal > mobs.lv:
            if LvAnimal > mobs.lv + 10:
                pass
            else:
                UpdateNome(locais, 'level', LvAnimal, mobs.nome)
                UpdateNome(locais, 'HP', mobs.hp + 1, mobs.nome)
                UpdateNome(locais, 'Dano', mobs.dano + 1, mobs.nome)
                UpdateNome(locais, 'Exp', mobs.exp + 1, mobs.nome)
                UpdateNome(locais, 'Dinheiro', mobs.dinheiro + 1, mobs.nome)
        break


def LvPet(locais, tecla2):
    petjogador = PetJogador()
    pet = Pet(petjogador.id)
    mobs = Mobs(locais, tecla2)
    UpdateNome('Pets', 'Exp', pet.exp + mobs.exp + 1, pet.nome)
    while True:
        if pet.exp >= pet.qtdeExp:
            UpdateNome('Pets', 'Level', pet.lv + 1, pet.nome)
            print(f'Pet Up Lv.{pet.lv + 1}')
        else:
            break
    pet = Pet(petjogador.id)
    print(f'Pet ganhou {mobs.exp} exp')
    print(f'Pet tem {pet.exp}/{pet.qtdeExp} exp')
    sleep(2)


def atributos():
    while True:
        atributo = Atributos()
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
            print(f'Atack: {atributo.atack}')
            print(f'Defesa: {atributo.defesa}')

        elif tecla in '1':
            jogador = Jogador()
            print(f'Quantidade de pontos: {jogador.pontos}')
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
            elif jogador.pontos >= 1:
                UpdateNome('Jogador', 'Pontos', jogador.pontos, jogador.nome)

                # atack
                if tecla1 in '0':
                    Update('Atributos', 'Atack', atributo.atack + 1, atributo.atack + 1)

                # defesa
                elif tecla1 in '1':
                    Update('Atributos', 'Defese', atributo.defesa + 1, atributo.defesa + 1)
            else:
                print('\033[33mErro: \033[mPontos insuficiente.')


def habilidades():
    while True:
        skill = Skill()
        print('[0] Mostrar Habilidades')
        print('[1] Treinar Habilidades')
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
            morte = Morte()
            print(f'Atacak: {skill.atack}')
            print(f'Defesa: {skill.defesa}')
            sleep(2)
            print(f'Tempo Perdido de Atack: {morte.tatack - 1} segundos')
            print(f'Tempo Perdido de Defesa: {morte.tdefese - 1} segundos')
            sleep(2)

        elif tecla in '1':
            print('Treinar:')
            print(f'[0] Atack = {skill.tempoatack} segundos')
            print(f'[1] Defesa = {skill.tempodefesa} segundos')
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
                print('Treinando Atack...')
                skill = Skill()
                for i in range(skill.tempoatack, -1, -1):
                    skill = Skill()
                    print(f'\r{skill.tempoatack}', end='')
                    Update('Habilidades', 'TempoAtack', skill.tempoatack - 1, skill.tempoatack)
                    sleep(1)
                Update('Habilidades', 'Atack', skill.atack + 1, skill.atack)
                skill = Skill()
                Update('Habilidades', 'TempoAtack', skill.atack * 60, skill.atack)
                print('\nVocê upou sua habilidade de atack')

            elif tecla1 in '1':
                print('Treinando Defesa...')
                skill = Skill()
                for i in range(skill.tempodefesa, -1, -1):
                    skill = Skill()
                    print(f'\r{skill.tempodefesa}', end='')
                    Update('Habilidades', 'TempoDefese', skill.tempodefesa - 1, skill.tempodefesa)
                    sleep(1)
                Update('Habilidades', 'Defese', skill.defesa + 1, skill.defesa)
                skill = Skill()
                Update('Habilidades', 'TempoDefese', skill.defesa * 60, skill.defesa)
                print('\nVocê upou sua habilidade de defese')


def coletaitens(locais, tecla2):
    mobs = Mobs(locais, tecla2)
    if mobs.nome in 'Madeira':
        lista = []
        print("Usar qual Machado:")
        for pos in range(0, 4):
            machados = Machados(pos)
            if machados.qtde > 0:
                print(f'[{pos}] {machados.nome} ({machados.eficiencia} segundos)')
                lista.append(str(pos))
        if not lista:
            print('Você não tem um machado')
            sleep(2)
        else:
            print('[C] Voltar')
            while True:
                tecla3 = str(input('Tecla: ')).strip().upper()
                if tecla3 in lista or tecla3 in 'C':
                    break
                else:
                    print('\033[31mErro:  \033[mOpção inválida, tente novamente')

            if tecla3 in 'C':
                pass

            else:
                machados = Machados(int(tecla3))
                while True:
                    print('Cortando Madeiras...')
                    for t in range(machados.eficiencia, -1, -1):
                        print(f'\r{t}', end='')
                        sleep(1)
                    print()
                    madeiras = Itens(ind='0')
                    UpdateNome('Itens', 'Qtde', madeiras.qtde + 2, madeiras.nome)
                    print('Você coletou 1 madeira')
                    sleep(1)

    elif mobs.nome in 'Pedras':
        lista = []
        print("Usar qual Picareta:")
        for pos in range(0, 4):
            picaretas = Picaretas(pos)
            if picaretas.qtde > 0:
                print(f'[{pos}] {picaretas.nome} ({picaretas.eficiencia} segundos)')
                lista.append(str(pos))

        if not lista:
            print('Você não tem uma picareta')
            sleep(2)
        else:
            print('[C] Voltar')
            while True:
                tecla3 = str(input('Tecla: ')).strip().upper()
                if tecla3 in lista or tecla3 in 'C':
                    break
                else:
                    print('\033[31mErro:  \033[mOpção inválida, tente novamente')
            if tecla3 in 'C':
                pass
            else:
                picaretas = Picaretas(int(tecla3))
                while True:
                    print('Minerando Pedras...')
                    for t in range(picaretas.eficiencia, -1, -1):
                        print(f'\r{t}', end='')
                        sleep(1)
                    print()
                    pedras = Itens(ind='1')
                    UpdateNome('Itens', 'Qtde', pedras.qtde + 2, pedras.nome)
                    print('Você coletou 1 pedra')
                    sleep(1)

    elif mobs.nome in 'Peixes':
        lista = []
        print("Usar qual Vara de Pesca:")
        for pos in range(0, 2):
            varapesca = VaraPesca(pos)
            if varapesca.qtde > 0:
                print(f'[{pos}] {varapesca.nome} ({varapesca.eficiencia} segundos)')
                lista.append(str(pos))

        if not lista:
            print('Você não tem uma Vara de Pesca')
            sleep(2)
        else:
            print('[C] Voltar')
            while True:
                tecla3 = str(input('Tecla: ')).strip().upper()
                if tecla3 in lista or tecla3 in 'C':
                    break
                else:
                    print('\033[31mErro:  \033[mOpção inválida, tente novamente')

            if tecla3 in 'C':
                pass

            else:
                varapesca = VaraPesca(int(tecla3))
                while True:
                    print('Pescando...')
                    for p in range(varapesca.eficiencia, -1, -1):
                        print(f'\r{p}', end='')
                        sleep(1)
                    print()
                    peixes = Itens(ind='2')
                    UpdateNome('Itens', 'Qtde', peixes.qtde + 2, peixes.nome)
                    print('Você coletou 1 peixe')
                    sleep(1)


def lojapot(Tipo):
    while True:
        lojas = Lojas(Tipo)
        linha('Loja de Poções')
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
            while True:
                print('[0] Poções de Vida')
                print('[1] Poções de Mana')
                print('[C] Voltar')
                while True:
                    tecla1 = str(input('Tecla: ')).strip().upper()
                    if tecla1 in '01C':
                        break
                    else:
                        print('\033[31mErro:  \033[mOpção inválida, tente novamente')
                if tecla1 in 'C':
                    break

                lvmaximo = lojas.lv
                if lvmaximo > 7:
                    lvmaximo = 7
                for i in range(0, lvmaximo):
                    if tecla1 in '0':
                        Pot = PocoesHP(i)
                        print(f'[{i}] {Pot.nome} (+{Pot.rec}HP) = {Pot.preco} moedas')
                    elif tecla1 in '1':
                        Pot = PocoesMana(i)
                        print(f'[{i}] {Pot.nome} (+{Pot.rec}Mana) = {Pot.preco} moedas')

                print('[C] Voltar')
                tecla2 = 10
                while True:
                    strtecla = str(input('Tecla: ')).strip().upper()
                    if strtecla.isnumeric():
                        tecla2 = int(strtecla)
                        if tecla2 < 0 or tecla2 >= lvmaximo:
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
                    jogador = Jogador()
                    while True:
                        if tecla1 in '0':
                            Pot = PocoesHP(tecla2)
                            maximo = jogador.dinheiro / Pot.preco
                        else:
                            Pot = PocoesMana(tecla2)
                            maximo = jogador.dinheiro / Pot.preco

                        print(f'Compra Máxima de {trunc(maximo)} poções')
                        qtde = str(input(f'Quantidade de {Pot.nome}: '))
                        if qtde.isnumeric():
                            qtde = int(qtde)
                            if tecla1 in '0':
                                pot = PocoesHP(tecla2)
                                custo = pot.preco * qtde
                                fron = 'Bolsa'
                            else:
                                pot = PocoesMana(tecla2)
                                custo = pot.preco * qtde
                                fron = 'PocaoMana'
                            if jogador.dinheiro >= custo or qtde == 0:
                                break
                            else:
                                print('\033[33mErro: \033[mMoedas insuficiente.')
                        else:
                            print('\033[31mErro:  \033[mOpção inválida, tente novamente')
                    UpdateNome('Jogador', 'Dinheiro', jogador.dinheiro - custo + 1, jogador.nome)
                    UpdateNome(fron, 'Qtde', pot.qtde + qtde + 1, pot.nome)
                    print(f'Você comprou {qtde} {pot.nome} por {custo} moedas')

        if tecla in '1':
            MelhorarLoja(Tipo)


def lojaferramentas(tecla2):
    while True:
        lojas = Lojas(tecla2)
        jogador = Jogador()
        linha('Loja de Ferramentas')
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
        tecla1 = 0
        if tecla in 'C':
            break
        elif tecla in '0':
            lvferramentas = lojas.lv
            if lojas.lv >= 4:
                lvferramentas = 4

            for i in range(0, lvferramentas):
                picaretas = Picaretas(i)
                print(f'[{i}] {picaretas.nome} ({picaretas.eficiencia} segundos) = {picaretas.preco} diamantes')
            print('[C] Voltar')
            while True:
                strtecla = str(input('Tecla: ')).strip().upper()
                if strtecla.isnumeric():
                    tecla1 = int(strtecla)
                    if tecla1 < 0 or tecla1 >= lvferramentas:
                        print('\033[31mErro:  \033[mOpção inválida, tente novamente')
                    else:
                        picareta = Picaretas(tecla1)
                        if picareta.qtde == 0:
                            break
                        else:
                            print('Você já tem essa Picareta')
                else:
                    if strtecla in 'C':
                        break
                    print('\033[31mErro:  \033[mOpção inválida, tente novamente')
            if strtecla in 'C':
                pass
            else:
                picareta = Picaretas(tecla1)
                if jogador.diamante >= picareta.preco:
                    UpdateNome('Jogador', 'Diamante', jogador.diamante - picareta.preco + 1, jogador.nome)
                    UpdateNome('Picaretas', 'Qtde', picareta.qtde + 2, picareta.nome)
                    print(f'Você comprou 1 {picareta.nome} por {picareta.preco} diamantes')
                    sleep(1)
                else:
                    print('\033[33mErro: \033[mDinheiro insuficiente.')

        elif tecla in '1':
            lvferramentas = lojas.lv
            if lvferramentas >= 4:
                lvferramentas = 4

            for i in range(0, lvferramentas):
                machados = Machados(i)
                print(f'[{i}] {machados.nome} ({machados.eficiencia} segundos) = {machados.preco} diamantes')
            print('[C] Voltar')
            while True:
                strtecla = str(input('Tecla: ')).strip().upper()
                if strtecla.isnumeric():
                    tecla1 = int(strtecla)
                    if tecla1 < 0 or tecla1 >= lvferramentas:
                        print('\033[31mErro:  \033[mOpção inválida, tente novamente')
                    else:
                        machados = Machados(tecla1)
                        if machados.qtde == 0:
                            break
                        else:
                            print('Você já tem esse machado')
                else:
                    if strtecla in 'C':
                        break
                    print('\033[31mErro:  \033[mOpção inválida, tente novamente')
            if strtecla in 'C':
                pass
            else:
                machados = Machados(tecla1)
                if jogador.diamante >= machados.preco:
                    UpdateNome('Jogador', 'Diamante', jogador.diamante - machados.preco + 1, jogador.nome)
                    UpdateNome('Machados', 'Qtde', machados.qtde + 2, machados.nome)
                    print(f'Você comprou 1 {machados.nome} por {machados.preco} diamantes')
                    sleep(1)
                else:
                    print('\033[33mErro: \033[mDinheiro insuficiente.')

        elif tecla in '2':
            lvferramentas = lojas.lv
            if lvferramentas >= 4:
                lvferramentas = 2
            else:
                lvferramentas = 1

            for i in range(0, lvferramentas):
                varapesca = VaraPesca(i)
                print(f'[{i}] {varapesca.nome} ({varapesca.eficiencia} segundos) = {varapesca.preco} diamantes')
            print('[C] Voltar')
            while True:
                strtecla = str(input('Tecla: ')).strip().upper()
                if strtecla.isnumeric():
                    tecla1 = int(strtecla)
                    if tecla1 < 0 or tecla1 >= lvferramentas:
                        print('\033[31mErro:  \033[mOpção inválida, tente novamente')
                    else:
                        varapesca = VaraPesca(tecla1)
                        if varapesca.qtde == 0:
                            break
                        else:
                            print('Você já tem essa vara de pesca')
                else:
                    if strtecla in 'C':
                        break
                    print('\033[31mErro:  \033[mOpção inválida, tente novamente')
            if strtecla in 'C':
                pass
            else:
                varapesca = VaraPesca(tecla1)
                if jogador.diamante >= varapesca.preco:
                    UpdateNome('Jogador', 'Diamante', jogador.diamante - varapesca.preco + 1, jogador.nome)
                    UpdateNome('VaraPesca', 'Qtde', varapesca.qtde + 2, varapesca.nome)
                    print(f'Você comprou 1 {varapesca.nome} por {varapesca.preco} diamantes')
                    sleep(1)
                else:
                    print('\033[33mErro: \033[mDiamante insuficiente.')

        elif tecla in '3':
            MelhorarLoja(tecla2)


def lojapet(tecla2):
    while True:
        lojas = Lojas(tecla2)
        linha('Lojas de Pets')
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
            print('Pets:')
            sleep(1)
            lvmaximo = lojas.lv
            if lvmaximo > 5:
                lvmaximo = 5
            for posmapa in range(0, lvmaximo):
                pet = Pet(posmapa)
                print(f'[{posmapa}] {pet.nome} = {pet.preco} diamantes')
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
                else:
                    tecla1 = int(tecla1)
                    mapa = Mapas(tecla1)
                    jogador = Jogador()
                    pet = Pet(tecla1)
                    mobs = Mobs(mapa.nome, pet.ind)
                    if mobs.morte >= 650:
                        if pet.qtde == 0:
                            if jogador.diamante >= pet.preco:
                                UpdateNome('Pets', 'Qtde', pet.qtde + 2, pet.qtde)
                                UpdateNome('Jogador', 'Diamante', jogador.diamante - pet.preco + 1, jogador.nome)
                                print(f'Você comprou 1 Pet {pet.nome} por {pet.preco} diamantes')
                                sleep(3)
                            else:
                                print('\033[33mErro: \033[mDiamante insuficiente.')
                                sleep(1)
                        else:
                            print('Você já tem esse Pet')
                            sleep(2)
                    else:
                        print(f'Você precisa matar no mínimo 650 {pet.nome}')
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
        linha('Lojas de Magias')
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
            lojas = Lojas(tecla2)
            lvmaximo = lojas.lv
            if lvmaximo > 18:
                lvmaximo = 18
            for i in range(0, lvmaximo):
                magia = Magias(i)
                print(f'[{i}] {magia.nome} Lv.{magia.lv} ({magia.mana} Mana) ({magia.dano - 10}-{magia.dano}'
                      f' Dano) = {magia.preco} Diamantes')
            print('[C] Voltar')
            tecla1 = 0
            while True:
                strtecla = str(input('Tecla: ')).strip().upper()
                if strtecla.isnumeric():
                    tecla1 = int(strtecla)
                    if 0 <= tecla1 < lojas.lv:
                        break
                    else:
                        print('\033[31mErro:  \033[mOpção inválida, tente novamente')
                else:
                    if strtecla in 'C':
                        break
                    print('\033[31mErro:  \033[mOpção inválida, tente novamente')
            if strtecla in 'C':
                pass
            else:
                jogador = Jogador()
                magia = Magias(tecla1)
                if jogador.lv >= magia.lvmin:
                    if magia.qtde == 0:
                        if jogador.diamante >= magia.preco:
                            UpdateNome('Jogador', 'Diamante', jogador.diamante - magia.preco + 1, jogador.nome)
                            UpdateNome('Magias', 'Qtde', magia.qtde + 2, magia.nome)
                            print(f'Você comprou 1 magia de {magia.nome} por {magia.preco} diamantes')
                            sleep(3)
                        else:
                            print('\033[33mErro: \033[mDiamante insuficiente.')
                            sleep(1)
                    else:
                        print('\033[33mErro: \033[mVocê já tem essa magia.')
                        sleep(1)
                else:
                    print(f'\033[33mErro: \033[mLevel insuficiente. Level Nescessário: {magia.lvmin}')
                    sleep(2)
        elif tecla in '1':
            MelhorarLoja(tecla2)


def lojaarmas(tecla2):
    while True:
        linha('Lojas de Armas')
        print('[0] Comprar Armas')
        print('[1] Melhorar Loja de Armas')
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
            lojas = Lojas(tecla2)
            lvmaximo = lojas.lv
            if lvmaximo > 6:
                lvmaximo = 6
            for e in range(0, lvmaximo):
                Espada = Armas(e)
                print(f'[{e}] {Espada.nome} Lv.{Espada.lv} = ({Espada.dano} Dano) ({Espada.atack} Atack) '
                      f'({Espada.rec} Rec) {Espada.preco} moedas')

            print('[C] Voltar')
            tecla1 = 0
            while True:
                strtecla = str(input('Tecla: ')).strip().upper()
                if strtecla.isnumeric():
                    tecla1 = int(strtecla)
                    if tecla1 < 0 or tecla1 >= lojas.lv:
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
                Espada = Armas(tecla1)
                jogador = Jogador()
                if jogador.lv >= Espada.lv:
                    if Espada.qtde == 0:
                        if jogador.dinheiro >= Espada.preco:
                            UpdateNome('Jogador', 'Dinheiro', jogador.dinheiro - Espada.preco + 1, jogador.nome)
                            UpdateNome('Armas', 'Qtde', Espada.qtde + 2, Espada.nome)
                            print(f'Você comprou 1 {Espada.nome} por {Espada.preco} moedas')
                            sleep(3)
                        else:
                            print('\033[33mErro: \033[mMoedas insuficiente.')
                            sleep(1)
                    else:
                        print('\033[33mErro: \033[mVocê já tem essa espada.')
                        sleep(1)
                else:
                    print(f'\033[33mErro: \033[mLevel insuficiente. Level Nescessário: {Espada.lv}')
                    sleep(2)
        elif tecla in '1':
            MelhorarLoja(tecla2)


def MelhorarLoja(tecla2):
    lojas = Lojas(tecla2)
    madeiras = Itens(ind='0')
    pedras = Itens(ind='1')
    peixes = Itens(ind='2')
    couros = Itens(ind='3')
    print(f'Loja de {lojas.nome} Level: {lojas.lv}')
    print(f'[0] Melhorar Loja = {madeiras.qtde}/{lojas.customadeiras} Madeiras, {pedras.qtde}/'
          f'{lojas.custopedras} Pedras', end='')
    if tecla2 == 0:
        print(f', {peixes.qtde}/{lojas.custopeixes} Peixes')
    elif tecla2 == 3:
        print(f', {couros.qtde}/{lojas.custocouros} Couros')
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
                if peixes.qtde >= lojas.custopeixes:
                    pass
                else:
                    print('\033[33mErro: \033[mPeixes insuficiente.')
                    sleep(2)
                    break
            if tecla2 == 3:
                if couros.qtde >= lojas.custocouros:
                    pass
                else:
                    print('\033[33mErro: \033[mCouros insuficiente.')
                    sleep(2)
                    break

            if madeiras.qtde >= lojas.customadeiras:
                if pedras.qtde >= lojas.custopedras:
                    UpdateNome('Itens', 'Qtde', madeiras.qtde - lojas.customadeiras + 1, madeiras.nome)
                    UpdateNome('Itens', 'Qtde', pedras.qtde - lojas.custopedras + 1, pedras.nome)
                    UpdateNome('Lojas', 'CustoMadeiras', lojas.customadeiras + 20, lojas.nome)
                    UpdateNome('Lojas', 'CustoPedras', lojas.custopedras + 20, lojas.nome)

                    if tecla2 == 0:
                        UpdateNome('Itens', 'Qtde', peixes.qtde - lojas.custopeixes + 1, peixes.nome)
                        UpdateNome('Lojas', 'CustoPeixes', lojas.custopeixes + 20, lojas.nome)

                    if tecla2 == 3:
                        UpdateNome('Itens', 'Qtde', couros.qtde - lojas.custocouros + 1, couros.nome)
                        UpdateNome('Lojas', 'CustoCouros', lojas.custocouros + 20, lojas.nome)

                    UpdateNome('Lojas', 'Level', lojas.lv + 1, lojas.nome)
                    print(f'Up Loja de {lojas.nome} Lv.{lojas.lv + 1}')
                    sleep(2)
                else:
                    print('\033[33mErro: \033[mPedras insuficiente.')
                    sleep(2)
            else:
                print('\033[33mErro: \033[mMadeiras insuficiente.')
                sleep(2)
            break


def Mortesmobs():
    for num in range(0, 7):
        mapas = Mapas(num)
        for pos in range(0, mapas.qtdemob):
            kill = Mobs(mapas.nome, pos)
            if kill.nome in ['Peixes', 'Pedras', 'Madeiras']:
                pass
            else:
                if kill.morte > 0:
                    print(f'{kill.nome} = {kill.morte}')


Connecte()
