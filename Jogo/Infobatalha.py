import SQL


def escolhapet(lista):
    while True:
        escolha = str(input('Tecla: ')).strip().upper()
        if escolha < lista or escolha in 'C':
            break
        else:
            print('\033[31mErro:  \033[mOpção inválida, tente novamente')

    if escolha in 'C':
        pass
    else:
        pet = lista[int(escolha)]
        HP = Busca('HP', 'PETS')
        print(pet)


Pets()


def infobatalha(locais, tecla1, tecla2):
    indanimal = int(tecla2)
    nomeanimal = SQL.Busca('Nome', locais, 'all')
    nomeanimal = nomeanimal[indanimal][0]

    lvanimal = SQL.Busca('Level', locais, 'all')
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

