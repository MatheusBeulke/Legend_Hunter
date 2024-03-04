# Jogador
level = {'Lv': 1, 'qtdeexp': 0, 'exp': 100}
jogador = {'HP': 100, 'vida': 100, 'pontos': 1}
atributos = {'atack': 4, 'defesa': 1}
habilidades = {'atack': 1, 'tempoatack': 60, 'defesa': 1, 'tempodefesa': 60}
dinheiro = 0
diamante = 0

mortejogador = 0
perdaexp = 0

Fragmentos = ['Fragmento de Hit', 'Fragmento de Ar', 'Fragmento de Psíquico', 'Fragmento de Alma', 'Fragmento de Gelo',
              'Fragmento de Choque', 'Fragmento de Fogo']

Loja = [['PoçãoPequena', 50, 20, 10, '0'], ['PoçãoMédia', 100, 50, 0, '1'], ['PoçãoGrande', 200, 100, 0, '2'],
        ['PoçãoGigante', 400, 200, 0, '3'], ['HiperPoção', 800, 400, 0, '4'], ['PoçãoMagica', 1600, 800, 0, '5']]

# Mapa
nmapa = ['0', '1', '2', '3', '4', '5', '6']
mapa = ['Colina Verde', 'Deserto', 'Caverna de Mineração', 'Floresta Sombria', 'Polo Norte', 'Eletrico', 'Vulcão']
mapamob = []

# nome, lv, vida, dano, exp, dinheiro, morte
# Colina Verde

nmobscolinaverde = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
mobscolinaverde = [['Rats', 1, 12, 7, 5, 3, 0], ['Crow', 15, 40, 25, 17, 15, 0], ['Wolf', 30, 70, 47, 34, 29, 0],
                   ['Lizard', 45, 102, 71, 53, 45, 0], ['Slime', 60, 136, 97, 74, 63, 0],
                   ['Assasin', 75, 172, 125, 97, 83, 0], ['Bear', 90, 210, 155, 122, 105, 0],
                   ['Goblin', 105, 250, 187, 129, 0], ['Minutaur', 120, 292, 265, 209, 183, 1]]

# Deserto
nmobsdeserto = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
mobsdeseto = [['Scorpion', 135, 350, 300, 230, 200, 0], ['Snake', 150, 378, 320, 245, 212, 0],
              ['Worm', 165, 408, 342, 262, 226, 0], ['Scarab', 180, 440, 366, 281, 242, 0],
              ['Cactus Soldier', 195, 474, 392, 302, 260, 0], ['Raptor', 210, 510, 420, 325, 280, 0],
              ['Mummy', 225, 548, 450, 350, 302, 0], ['Pharaó', 240, 588, 482, 377, 326, 0],
              ['Anubis', 255, 630, 516, 406, 352, 0], ['Sandstone Golem', 270, 674, 552, 437, 380, 0]]

# Caverna de mineração
nmobscavernaminer = ['0', '1', '2', '3', '4', '5', '6', '7']
mobscarvenaminer = [['Bat', 285, 700, 580, 450, 400, 0], ['Gigantula', 300, 728, 600, 456, 412, 0],
                    ['Dwarf', 315, 758, 622, 482, 426, 0], ['Miner', 330, 790, 646, 501, 442, 0],
                    ['Troll', 345, 824, 672, 522, 460, 0], ['Orc', 360, 850, 700, 545, 480, 0],
                    ['Djinn', 375, 888, 730, 570, 502, 0], ['Ciclops', 390, 948, 762, 597, 526, 0]]

# Floresta sombria
nmobsflorestasombria = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
mobsflorestasombria = [['Skeleton', 405, 986, 804, 626, 549, 0], ['Zombie', 420, 1014, 824, 641, 561, 0],
                       ['Ghost', 435], ['Witch', 450], ['Lich', 465], ['Shandow', 480], ['Phanton Flame', 495],
                       ['Phanton Fiend', 510], ['Skeleton Dragon', 525], ['Gargoyle', 540], ['Spectral Flame', 555],
                       ['Spectral Fiend', 570], ['Vampire', 585]]

# Icy
nmobsicy = ['0', '1', '2', '3', '4', '5', '6']
mobsicy = [['Icy Flame', 600], ['Snow Golem', 615], ['Mammoth', 630], ['Yeti', 645], ['Icy Wizard', 660],
           ['Icy Dragon', 675], ['Icy Fiend', 690]]

# Electric
nmobselectric = ['0', '1', '2', '3', '4', '5']
mobselectric = [['Electric Flame', 705], ['Electric Golem', 720], ['Electric Yeti', 735], ['Electric Wizard', 750],
                ['Electric Dragon', 765], ['Electric Fiend', 780]]

# Fire
nmobsfire = ['0', '1', '2', '3', '4']
mobsfire = [['Flame', 795], ['Fire Golem', 810], ['Wizard', 825], ['Dragon', 840], ['Demon', 855]]
