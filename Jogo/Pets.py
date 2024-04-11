import BDP
import sqlite3


def Busca(Select, From, Tipo):
    banco = sqlite3.connect('Banco_Dados.db')
    cursor = banco.cursor()
    if Select in '*':
        cursor.execute('SELECT * FROM "' + str(From) + '"')
        busca = cursor.fetchall()
        return busca

    cursor.execute(f'SELECT {Select} FROM {From}')
    if Tipo in 'one':
        busca = cursor.fetchone()
        return busca
    elif Tipo in 'all':
        busca = cursor.fetchall()
        return busca


def UpdateNome(update, Set, Igual, Where):
    banco = sqlite3.connect('Banco_Dados.db')
    cursor = banco.cursor()

    cursor.execute(
        "UPDATE '" + str(update) + "' SET '" + str(Set) + "' = '" + str(Igual) + "' WHERE Nome = '" + str(Where) + "'")
    banco.commit()


def Pets():
    for posmapa in range(0, 7):
        for pos, mobs in enumerate(BDP.mobs[posmapa]):
            if mobs[0] in BDP.pets[posmapa]:
                qtdemorte = Busca('Morte', BDP.locais[posmapa], 'all')
                qtdepet = Busca('Qtde', 'Pets', 'all')
                if qtdemorte[pos][0] - 1 >= 0 and qtdepet[posmapa][0] - 1 == 0:
                    ganhpet = qtdepet[posmapa][0] + 1
                    UpdateNome('Pets', 'Qtde', ganhpet, BDP.pets[posmapa][0])
                    qtdepet = Busca('Qtde', 'Pets', 'all')
                    print(f'Parabéns você ganhou {qtdepet[posmapa][0] - 1} Pet {BDP.pets[posmapa][0]}')
