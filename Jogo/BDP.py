# Jogador
mortejogador = 0
mortepet = 0
perdaexp = 0
qtdemorte = 1

# Fragmentos
Fragmentos = ['Fragmento de Hit', 'Fragmento de Ar', 'Fragmento de Psíquico', 'Fragmento de Alma', 'Fragmento de Gelo',
              'Fragmento de Choque', 'Fragmento de Fogo']
fragmentos = ['FragmentoHit', 'FragmentoAr', 'FragmentoPsíquico', 'FragmentoAlma', 'FragmentoGelo',
              'FragmentoEletrico', 'FragmentoFogo']

# Loja
TipoLojas = ['Poções', 'Ferramentas', 'Pets', 'Magias']

Loja = [['PoçãoPequena', 50, 20, 10, '0'], ['PoçãoMédia', 100, 50, 0, '1'], ['PoçãoGrande', 200, 100, 0, '2'],
        ['PoçãoGigante', 400, 200, 0, '3'], ['HiperPoção', 800, 400, 0, '4'], ['PoçãoMagica', 1600, 800, 0, '5']]

# Mapa
nmapa = ['0', '1', '2', '3', '4', '5', '6']
mapa = ['Colina Verde', 'Deserto', 'Caverna de Mineração', 'Floresta Sombria', 'Polo Norte', 'Eletrico', 'Vulcão']
locais = ['MobsColinaVerde', 'MobsDeserto', 'MobsCavernaMinerção', 'MobsFlorestaSombria', 'MobsIcy', 'MobsElectric',
          'MobsFire']

# nome, lv, vida, dano, exp, dinheiro, morte
nmobs = [['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
         ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
         ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'],
         ['0', '1', '2', '3', '4', '5', '6', '7'], ['0', '1', '2', '3', '4', '5', '6'], ['0', '1', '2', '3', '4', '5']]

mobs = [
    [['Rats', 1], ['Crow', 15], ['Wolf', 30], ['Lizard', 45], ['Slime', 60], ['Assasin', 75], ['Bear', 90],
     ['Goblin', 105], ['Minutaur', 120], ['Peixes'], ['Boss']],

    [['Scorpion', 135], ['Snake', 150], ['Worm', 165], ['Scarab', 180], ['Cactus Soldier', 195],
     ['Raptor', 210], ['Mummy', 225], ['Pharaó', 240], ['Anubis', 255], ['Sandstone Golem', 270], ['Boss']],

    [['Bat', 285], ['Gigantula', 300], ['Dwarf', 315], ['Miner', 330], ['Troll', 345], ['Orc', 360], ['Djinn', 375],
     ['Ciclops', 390], ['Pedras'], ['Boss']],

    [['Skeleton', 405, 986, 804, 626, 549, 0], ['Zombie', 420, 1014, 824, 641, 561, 0],
     ['Ghost', 435], ['Witch', 450], ['Lich', 465], ['Shandow', 480], ['Phanton Flame', 495],
     ['Phanton Fiend', 510], ['Skeleton Dragon', 525], ['Gargoyle', 540], ['Spectral Flame', 555],
     ['Spectral Fiend', 570], ['Vampire', 585], ['Madeiras'], ['Boss']],

    [['Icy Flame', 600], ['Snow Golem', 615], ['Mammoth', 630], ['Yeti', 645], ['Icy Wizard', 660],
     ['Icy Dragon', 675], ['Icy Fiend', 690], ['Boss']],

    [['Electric Flame', 705], ['Electric Golem', 720], ['Electric Yeti', 735], ['Electric Wizard', 750],
     ['Electric Dragon', 765], ['Electric Fiend', 780], ['Boss']],

    [['Flame', 795], ['Fire Golem', 810], ['Wizard', 825], ['Dragon', 840], ['Demon', 855], ['Boss']],
        ]

# Ferramentas
# Picaretas
Picaretas = [['Picareta Inicial', 90, 50], ['Picareta de Ferro', 60, 100], ['Picareta de Titanio', 30, 150],
             ['Picareta dos Deuses', 15, 200]]

# Machados
Machados = [['Machado Inicial', 60, 20], ['Machado de Ferro', 40, 40], ['Machado de Titanio', 20, 60],
            ['Machado dos Deuses', 10, 80]]

# VaraPesca
VaraPesca = [['Vara de Pesca', 40, 30], ['Vara de Pesca com Comida', 20, 60]]

# Itens
Itens = ['Madeiras', 'Pedras', 'Peixes', 'Couros']

# Pets
npets = ['0', '1', '2', '3', '4', '5', '6']
pets = [['Wolf', 1], ['Scorpion', 1], ['Troll', 1], ['Shandow', 1], ['Icy Dragon', 1], ['Electric Yeti', 1],
        ['Demon', 1]]

# Magias
magias = [['Hit', 1], ['Hit', 2], ['Hit', 3], ['Ar', 1], ['Ar', 2], ['Ar', 3], ['Psiquico', 1], ['Psiquico', 2],
          ['Psiquico', 3], ['Alma', 1], ['Alma', 2], ['Alma', 3], ['Gelo', 1], ['Gelo', 2], ['Gelo', 3],
          ['Eletrico', 1], ['Eletrico', 2], ['Eletrico', 3], ['Fogo', 1], ['Fogo', 2], ['Fogo', 3]]
