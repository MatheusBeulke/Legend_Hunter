import BDP
from time import sleep
import Batalha
import sqlite3
import Lojas
import Infobatalha
from random import randint


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