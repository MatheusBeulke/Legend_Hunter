from time import sleep
import BDP
import Mapa
import Atributos
import Habilidades
import Lojas
import sqlite3
import MortsMobs


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
                    print(f'Dinheiro: {int(dinheiro[0])}')

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

