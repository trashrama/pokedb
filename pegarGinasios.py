import requests
from bs4 import BeautifulSoup
from random import randint


# def gravarGinasios(int):

page = requests.get("https://pokemondb.net/red-blue/gymleaders-elitefour")
soup = BeautifulSoup(page.content, 'html.parser')
id = 1

for i in range(8):
    ginasios = soup.find(id="gym-{}".format(i+1)).text
    id_ginasio = ginasios[ginasios.find("#")+1]
    lugar = ginasios[ginasios.find(",")+2:]
    ginasios = soup.find_all('div', {'class': 'infocard-list-trainer-pkmn'})
    nome_lider = ginasios[i].find('span', {'class': 'ent-name'}).text

    smalls = ginasios[i].find_all('small')
    small = smalls[0].text
    insignia = small[:small.find("Badge")+5]
    tipo_pokemon = (small[small.find("Badge")+6:]
                    ).replace("type Pokémon", "").strip()
    pokemons_lider = []

    for i in range(1, len(smalls)):
        if "#" in smalls[i].text:
            idpoke = smalls[i].text.replace("#", "")
        if "Level" in smalls[i].text:
            pokemons_lider.append([idpoke, smalls[i].text.replace("#", "")])
    # print("termino")
    # print(id)
    # print(nome_lider)
    # print(lugar)
    # print(insignia)
    # print(tipo_pokemon)
    # print(pokemons_lider)

    # passo 1 criar as entradas pra treinador dos lideres do ginasio
    # passo 2 criar as entradas para os pokemons dos lideres dos ginasios
    # passo 3 criar os ginasios
    if (id == 2) or id == 4 or id == 6:
        sex = 'F'
    else:
        sex = 'M'

    cor_olhos = ['BLACK', 'BROWN', 'BLUE', 'GREEN']

    # imprimir treinadores
    # print("('{}', '{}', '{}', '{}', {}, '{}'),".format(nome_lider,
    #       '1/01/1999', sex, cor_olhos[randint(0, len(cor_olhos)-1)], '1.70', lugar))

    # imprimir pokemons
    # for pokemon in pokemons_lider:
    #     print("({}, {}, '{}'),".format(
    #         id, pokemon[0], pokemon[1]))

    # imprimir ginasios
    print("({}, '{}', '{}', '{}'),".format(id, insignia, lugar, tipo_pokemon))

    id = id + 1
# lista de coisas:
# incrementar a lista de lugares de kanto
#

# codigo pra pegar os lugares restantes

lugares = [(0, 'National Park'),
           (1, 'Mt. Moon'),
           (2, 'Union Cave'),
           (3, 'Mt. Mortar'),
           (4, 'Route 12'),
           (5, 'Route 15'),
           (6, 'Pewter City'),
           (7, 'Pallet Town'),
           (8, 'Underground Path 5-6'),
           (9, 'Slowpoke Well'),
           (10, 'Route 23'),
           (11, 'Cerulean City'),
           (12, 'Route 2'),
           (13, 'Celadon City'),
           (14, 'Route 24'),
           (15, 'Viridian City'),
           (16, 'Dark Cave'),
           (17, 'Great Marsh'),
           (18, 'Mt. Silver'),
           (19, 'Power Plant'),
           (20, 'Route 4'),
           (21, '210'),
           (22, 'Viridian Forest'),
           (23, 'Tohjo Falls'),
           (24, 'Oreburgh City'),
           (25, 'Route 209'),
           (26, 'Vermilion City'),
           (27, 'Route 14'),
           (28, 'Cinnabar Island'),
           (29, 'Victory Road'),
           (30, 'Pokémon Tower'),
           (31, 'Route 6'),
           (32, 'Ice Path'),
           (33, 'Route 20'),
           (34, 'Route 18'),
           (35, 'Route 1'),
           (36, 'Whirl Islands'),
           (37, 'Route 22'),
           (38, 'Route 11'),
           (39, 'Safari Zone'),
           (40, 'Route 8'),
           (41, 'Seafoam Islands'),
           (42, 'Route 19'),
           (43, 'Diglett''s Cave'),
           (44, 'Pokémon Mansion'),
           (45, 'Rock Tunnel'),
           (46, 'Route 7'),
           (47, 'Route 9'),
           (48, 'Route 10'),
           (49, 'Route 3'),
           (50, 'Route 17'),
           (51, 'Cerulean Cave'),
           (52, 'Fuchsia City'),
           (53, 'Route 21'),
           (54, 'Route 16'),
           (55, 'Route 25'),
           (56, 'Route 28'),
           (57, 'Route 13'),
           (58, 'Route 5'),
           ]

page = requests.get(
    "https://bulbapedia.bulbagarden.net/wiki/Category:Red,_Blue_and_Yellow_locations")
soup = BeautifulSoup(page.content, 'html.parser')
tabela = soup.find('div', {'class': 'mw-content-ltr'})

items = tabela.find_all('a')
i = 59
for item in items:
    item = item.text
    if ("Kanto" in item and 'Route' in item and 'Underground' in item and 'Victory' in item):
        print(i, item)
        i = i+1
