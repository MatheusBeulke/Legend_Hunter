from math import trunc
import BDP
import sqlite3
from time import sleep
from versaoteste import Busca


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
