from SQL import Busca, UpdateNome, Update
from time import sleep
from random import randint
from MortsMobs import mortemob
import BDP


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
