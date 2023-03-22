import requests
from bs4 import BeautifulSoup
from random import randint


# def gravarGinasios(int):

page = requests.get("https://pokemondb.net/ruby-sapphire/gymleaders-elitefour")
soup = BeautifulSoup(page.content, 'html.parser')
id = 17

for i in range(0, 5):
    ginasios = soup.find(id="elite4-{}".format(i+1)).text

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
    print(nome_lider)
    #print(lugar)
    # print(insignia)
    print(tipo_pokemon)
    print(pokemons_lider)

    # passo 1 criar as entradas pra treinador dos lideres do ginasio
    # passo 2 criar as entradas para os pokemons dos lideres dos ginasios
    # passo 3 criar os ginasios
    if (id == 17) or id == 20 or id == 22 or id == 23:
        sex = 'F'
    else:
        sex = 'M'

    cor_olhos = ['BLACK', 'BROWN', 'BLUE', 'GREEN']

    dia = randint(1, 31)
    mes = randint(1, 12)
    ano = randint(1980, 2005)

    if ("&" in nome_lider):
        nome_lider = nome_lider.split("&")
        for nome in nome_lider:
            print("('{}', '{}', '{}', '{}', 1.{}, '{}'),".format(nome.strip(),
                                                                 data, sex, cor_olhos[randint(0, len(cor_olhos)-1)], randint(50, 70), lugar))

    else:
        data = f'{mes}/{dia}/{ano}'
        imprimir treinadores
        print("('{}', '{}', '{}', '{}', 1.{}, '{}'),".format(nome_lider,
                                                             data, sex, cor_olhos[randint(0, len(cor_olhos)-1)], randint(50, 70), lugar))

    # imprimir pokemons
    # for pokemon in pokemons_lider:
    #     print("({}, {}, '{}'),".format(
    #         id, pokemon[0], pokemon[1]))

    # imprimir ginasios

    lugar = "Route 23"
    print("({}, '{}', '{}', '{}'),".format(
        id, insignia, lugar, tipo_pokemon))

    id = id + 1