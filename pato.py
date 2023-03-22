import requests
from bs4 import BeautifulSoup
lista_banidos = [133, 290, 366, 281, 61, 44, 79, 236, 265]
lista_semEv = [45, 62, 80, 106, 107, 199, 133, 134, 135, 136,
               182, 186, 196, 197, 237, 291, 292, 367, 368, 282, 362]


def gravar(id, nome, tipo1, tipo2, habilidade, hp, attack, sp_atk,
           sp_def, speed, bufunfa, specie, altura, peso, cidade):

    lista_tipos = ['Normal',
                   'Fire',
                   'Water',
                   'Electric',
                   'Grass',
                   'Ice',
                   'Fighting',
                   'Poison',
                   'Ground',
                   'Flying',
                   'Psychic',
                   'Bug',
                   'Rock',
                   'Ghost',
                   'Dragon',
                   'Dark',
                   'Steel',
                   'Fairy']

    f = open("funky_pokemons.txt", "a")

    for i in range(len(lista_tipos)):
        if (lista_tipos[i] == tipo1):
            tipo1_id = i+1
            break
    for i in range(len(lista_tipos)):
        if (lista_tipos[i] == tipo2):
            tipo2_id = i+1
            break

    if tipo2 != "NULL":
        f.writelines("('{}', '{}', '{}', '{}', {}, {}, {}, {}, {}, {}, '{}', {}, {}),\n".format(
            nome, tipo1, tipo2, habilidade, hp, attack, sp_atk,
            sp_def, speed, bufunfa, specie, altura, peso))
    else:
        f.writelines("('{}', '{}', NULL, '{}', {}, {}, {}, {}, {}, {}, '{}', {}, {}),\n".format(
            nome, tipo1, habilidade, hp, attack, sp_atk,
            sp_def, speed, bufunfa, specie, altura, peso))
    f.close()


def gravarLugares(id_pokemon, jogo, lugares, cidade):
    f = open("funky_lugares.txt", "a")

    lista_lugares = [
        'Route 1',
        'Route 2',
        'Route 3',
        'Route 4',
        'Route 5',
        'Route 6',
        'Route 7',
        'Route 8',
        'Route 9',
        'Route 10',
        'Route 11',
        'Route 12',
        'Route 13',
        'Route 14',
        'Route 15',
        'Route 16',
        'Route 17',
        'Route 18',
        'Route 19',
        'Route 20',
        'Route 21',
        'Route 22',
        'Route 23',
        'Route 24',
        'Route 25',
        'Route 26',
        'Route 27',
        'Route 28',
        'Berry Forest',
        'Bond Bridge',
        'Canyon Entrance',
        'Cape Brink',
        'Celadon City',
        'Cerulean Cave',
        'Cerulean City',
        'Cinnabar Island',
        'Diglett''s Cave',
        'Dotted Hole',
        'Five Island',
        'Five Isle Meadow',
        'Four Island',
        'Fuchsia City',
        'Green Path',
        'Icefall Cave',
        'Indigo Plateau',
        'Kindle Road',
        'Lavender Town',
        'Lost Cave',
        'Memorial Pillar',
        'Mt. Ember',
        'Mt. Moon',
        'Navel Rock',
        'One Island',
        'Outcast Island',
        'Pallet Town',
        'Pattern Bush',
        'Pewter City',
        'Pokémon Mansion',
        'Pokémon Tower',
        'Power Plant',
        'Resort Gorgeous',
        'Roaming Kanto',
        'Rock Tunnel',
        'Rocket Hideout',
        'Rocket Warehouse',
        'Ruin Valley',
        'Safari Zone''s Kanto',
                     'Saffron City',
                     'Seafoam Islands',
                     'Sevault Canyon',
                     'Seven Island',
                     'Silph Co.',
                     'Six Island',
                     'SS Anne',
                     'Tanoby Ruins',
                     'Three Island',
                     'Three Isle Path',
                     'Three Isle Port',
                     'Tohjo Falls',
                     'Trainer Tower',
                     'Treasure Beach',
                     'Two Island',
                     'Underground Path 5-6',
                     'Underground Path 7-8',
                     'Vermilion City',
                     'Victory Road''s Kanto',
                     'Viridian City',
                     'Viridian Forest',
                     'Water Labyrinth',
                     'Water Path',
                     'Route 29',
                     'Route 30',
                     'Route 31',
                     'Route 32',
                     'Route 33',
                     'Route 34',
                     'Route 35',
                     'Route 36',
                     'Route 37',
                     'Route 38',
                     'Route 39',
                     'Route 40',
                     'Route 41',
                     'Route 42',
                     'Route 43',
                     'Route 44',
                     'Route 45',
                     'Route 46',
                     'Route 47',
                     'Route 48',
                     'Azalea Town',
                     'Battle Frontier''s Johto',
                     'Bell Tower',
                     'Bellchime Trail',
                     'Blackthorn City',
                     'Burned Tower',
                     'Cherrygrove City',
                     'Cianwood City',
                     'Cliff Cave',
                     'Cliff Edge Gate',
                     'Dark Cave',
                     'Dragon''s Den',
                     'Ecruteak City',
                     'Embedded Tower',
                     'Frontier Access',
                     'Glitter Lighthouse',
                     'Goldenrod City',
                     'Goldenrod Radio Tower',
                     'Goldenrod Underground',
                     'Ice Path',
                     'Ilex Forest',
                     'Lake of Rage',
                     'Mahogany Town',
                     'Mt. Mortar',
                     'Mt. Silver',
                     'National Park',
                     'New Bark Town',
                     'Olivine City',
                     'Pokéathlon Dome',
                     'Roaming Johto',
                     'Ruins of Alph',
                     'Safari Zone Gate',
                     'Sinjoh Ruins',
                     'Slowpoke Well',
                     'Sprout Tower',
                     'SS Aqua',
                     'Team Rocket HQ',
                     'Tin Tower',
                     'Union Cave',
                     'Violet City',
                     'Whirl Islands',
                     'Route 101',
                     'Route 102',
                     'Route 103',
                     'Route 104',
                     'Route 105',
                     'Route 106',
                     'Route 107',
                     'Route 108',
                     'Route 109',
                     'Route 110',
                     'Route 111',
                     'Route 112',
                     'Route 113',
                     'Route 114',
                     'Route 115',
                     'Route 116',
                     'Route 117',
                     'Route 118',
                     'Route 119',
                     'Route 120',
                     'Route 121',
                     'Route 122',
                     'Route 123',
                     'Route 124',
                     'Route 125',
                     'Route 126',
                     'Route 127',
                     'Route 128',
                     'Route 129',
                     'Route 130',
                     'Route 131',
                     'Route 132',
                     'Route 133',
                     'Route 134',
                     'Abandoned Ship',
                     'Altering Cave',
                     'Artisan Cave',
                     'Hoenn''s Battle Frontier',
                     'Battle Resort',
                     'Battle Tower',
                     'Birth Island',
                     'Cave of Origin',
                     'Desert Underpass',
                     'Dewford Town',
                     'Ever Grande City',
                     'Fallarbor Town',
                     'Faraway Island',
                     'Fiery Path',
                     'Fortree City',
                     'Granite Cave',
                     'Jagged Pass',
                     'Lavaridge Town',
                     'Lilycove City',
                     'Littleroot Town',
                     'Marine Cave',
                     'Mauville City',
                     'Meteor Falls',
                     'Mirage Island',
                     'Mirage Spots',
                     'Mirage Tower',
                     'Mossdeep City',
                     'Mt. Chimney',
                     'Mt. Pyre',
                     'New Mauville',
                     'Oldale Town',
                     'Pacifidlog Town',
                     'Petalburg City',
                     'Petalburg Woods',
                     'Roaming Hoenn',
                     'Rustboro City',
                     'Rusturf Tunnel',
                     'Hoenn''s Safari Zone',
                     'Scorched Slab',
                     'Sea Mauville',
                     'Seafloor Cavern',
                     'Sealed Chamber',
                     'Shoal Cave',
                     'Sky Pillar',
                     'Slateport City',
                     'Sootopolis City',
                     'Southern Island',
                     'SS Tidal',
                     'Team Magma/Aqua Hideout',
                     'Terra Cave',
                     'Trainer Hill',
                     'Verdanturf Town',
                     'Hoenn''s Victory Road']

    try:
        lugares = lugares.split(",")
        print(lugares)
        primeiro = True
        for i in range(len(lugares)):
            if (lugares[i])[0] == " ":
                lugares[i] = (lugares[i])[1:]

            if ("Route" in lugares[0] and len(lugares) > 1):
                if primeiro:
                    primeiro = False
                else:
                    if len(lugares[i]) <= 2:
                        lugares[i] = "Route " + lugares[i]
            if "Trade/migrate" in lugares[i] or "Evolve" in lugares[i]:
                pass
            else:

                for j in range(len(lista_lugares)):
                    if (lugares[i] == lista_lugares[j]):
                        id_lugar = j
                    else:
                        teste = "{}''s {}".format(cidade, lugares[i])
                        if (teste == lista_lugares[j]):
                            id_lugar = j
                f.writelines("({}, '{}', {}),\n".format(
                    id_pokemon, jogo.upper().replace("'", "''"), id_lugar+1))

    except:
        if (lugares[i])[0] == " ":
            lugares[i] = (lugares[i])[1:]
        if "Trade/migrate" in lugares[i] or "Evolve" in lugares[i]:
            pass
        else:
            for j in range(len(lista_lugares)):
                if (lugares[i] == lista_lugares[j]):
                    id_lugar = j
                    f.writelines("({}, '{}', {}),\n".format(
                        id_pokemon, jogo.upper().replace("'", "''"), id_lugar+1))
    f.close()


def gravarEvo(id_pokemon, id_prox, tipo):
    f = open("funky_evolucoes.txt", "a")

    if ('Stone' in tipo and ',' in tipo):
        tipo = tipo.split(",")
        tipo = tipo[0]

    if not (id_prox == 'NULL' and tipo == 'NULL' or id_pokemon == id_prox):
        try:
            if (int(id_prox) < 387):
                f.writelines("({}, {}, '{}'),\n".format(
                    id_pokemon, id_prox, tipo.replace("(", "").replace(")", "")))
        except:
            f.writelines("({}, {}, '{}'),\n".format(
                id_pokemon, id_prox, tipo.replace("(", "").replace(")", "")))
    f.close()


for i in range(1, 387):

    page = requests.get("https://pokemondb.net/pokedex/{}".format(i))
    soup = BeautifulSoup(page.content, 'html.parser')

    if (i < 152):
        cidade = 'KANTO'
    elif (i >= 152 and i < 252):
        cidade = 'JOHTO'
    else:
        cidade = 'HOENN'

    # nome do pokemon

    nome = (soup.find("h1").text).replace("'", "''")
    print(nome)

    tabela = soup.find_all('table', class_="vitals-table")
    linhas_info = tabela[0].find_all('tr')

    # id do pokemon
    id_pokemon = linhas_info[0].find("strong").text
    # tipo do pokemon
    tipos = linhas_info[1].find_all('a')
    if (len(tipos) == 2):
        tipo1 = tipos[0].text
        tipo2 = tipos[1].text
    else:
        tipo1 = tipos[0].text
        tipo2 = "NULL"

    # especie
    especie = linhas_info[2].find("td").text.replace(" Pokémon", "")
    print(especie)
    # altura
    altura = linhas_info[3].find("td").text
    altura = altura[:altura.find("m")-1]
    print(altura)
    # peso
    peso = linhas_info[4].find("td").text
    peso = peso[:peso.find("k")-1]
    # habilidades
    hab = linhas_info[5].find("a").text
    print(hab)

    # status
    linhas_stats = tabela[3].find_all("tr")
    status = []

    for i in range(len(linhas_stats)-1):
        item = linhas_stats[i].find(class_="cell-num").text
        status.append(item)

    # evolucoes
    id_ant = ""
    id_ev = ""
    tipo_ev = ""

    broken = 0
    if (id_pokemon not in lista_banidos):
        try:
            cards = soup.find(class_="infocard-list-evo")
            total_ev = cards.find_all("div")
            try:
                spansdivididos = soup.find(class_='infocard-evo-split')
            except:
                print("Não tem spans.")
            nivel_ev = cards.find_all(class_="infocard-arrow")

            for i in range(len(total_ev)):
                num = total_ev[i].find('span', class_="infocard-lg-data")
                num = num.find("small").text
                num = num.replace("#", "")

                if (num == id_pokemon and i != 0):
                    try:
                        id_ev = total_ev[i+1].find('span',
                                                   {'class': ["infocard-lg-data", 'text-muted']})
                        id_ev = id_ev.find("small").text.replace("#", "")
                        broken = i
                    except:
                        id_ev = 'NULL'
                    try:

                        tipo_ev = nivel_ev[i].text
                    except:
                        tipo_ev = "NULL"
                        break
                elif (num == id_pokemon and i == 0):
                    try:
                        id_ev = total_ev[i +
                                         1].find('span', {'class': ["infocard-lg-data", 'text-muted']})
                        id_ev = total_ev[i +
                                         1].find("small").text.replace("#", "")

                    except:
                        id_ev = "NULL"
                    try:
                        tipo_ev = nivel_ev[i].text
                    except:
                        tipo_ev = "NULL"
                        break
        except:
            id_ev = "NULL"
            id_ant = "NULL"
            tipo_ev = "NULL"

    try:
        if (int(id_ev) in lista_semEv) or (int(id_ev) == int(id_pokemon)):
            id_ev = 'NULL'
            # cards = soup.find(class_="infocard-list-evo")

            # nivel_ev = cards.find_all(class_="infocard-arrow")

            # tipo_ev = nivel_ev[broken-1].text
            tipo_ev = "NULL"
    except:
        pass
    id_ev = id_ev.replace("\n", "")

    print("num: " + id_pokemon)
    print("id_evo: "+id_ev)
    print("n.E: "+tipo_ev)

    string = soup.find(
        text=lambda text: text and 'Where to find' in text).parent
    proximo = string.find_next_sibling()

    jogo1 = ""
    jogo2 = ""
    jogo3 = ""

    onde_encontrar = proximo.find_all("tr")

    # if (len(jogos) == 2):
    #     for i in range(0, 2):
    #         find = onde_encontrar[i].find_all("td")
    #         if (i == 0):
    #             jogo1, jogo2 = find[0].text, find[0].text
    #         else:
    #             jogo3 = find[0].text
    # else:
    #     find = onde_encontrar[i].find_all("td")
    #     jogo1, jogo2, jogo3 = find[0].text, find[0].text, find[0].text

    print("onde encontrar red: " + jogo1)
    print("onde encontrar blue: " + jogo2)
    print("onde encontrar yellow: " + jogo3)

    # gravar(id_pokemon, nome, tipo1, tipo2, hab,
    #        status[0], status[1], status[2], status[3], status[4], status[5], especie, altura, peso, cidade)

    if (int(id_pokemon) < 152):

        for i in range(len(onde_encontrar)):

            jogos = onde_encontrar[i].find('th')
            jogos = jogos.find_all()

            for jogo in jogos:
                if jogo.text == 'Red':
                    pos_red = i
                elif jogo.text == 'Blue':
                    pos_blue = i
                elif jogo.text == 'Yellow':
                    pos_yellow = i

        cidade_red = onde_encontrar[pos_red].find('td').text
        cidade_blue = onde_encontrar[pos_blue].find('td').text
        cidade_yellow = onde_encontrar[pos_yellow].find('td').text

        print(cidade_red, cidade_blue, cidade_yellow)

        gravarLugares(id_pokemon, "Red", cidade_red, cidade)
        gravarLugares(id_pokemon, "Blue", cidade_blue, cidade)
        gravarLugares(id_pokemon, "Yellow", cidade_yellow, cidade)
    elif (int(id_pokemon) >= 152 and int(id_pokemon) < 252):

        for i in range(len(onde_encontrar)):

            jogos = onde_encontrar[i].find('th')
            jogos = jogos.find_all()

            for jogo in jogos:
                if jogo.text == 'Gold':
                    pos_gold = i
                elif jogo.text == 'Silver':
                    pos_silver = i
                elif jogo.text == 'Crystal':
                    pos_crystal = i

        cidade_gold = onde_encontrar[pos_gold].find('td').text
        cidade_silver = onde_encontrar[pos_silver].find('td').text
        cidade_crystal = onde_encontrar[pos_crystal].find('td').text

        gravarLugares(id_pokemon, "Gold", cidade_gold, cidade)
        gravarLugares(id_pokemon, "Silver", cidade_silver, cidade)
        gravarLugares(id_pokemon, "Crystal", cidade_crystal, cidade)
    else:

        for i in range(len(onde_encontrar)):

            jogos = onde_encontrar[i].find('th')
            jogos = jogos.find_all()

            for jogo in jogos:
                if jogo.text == 'Ruby':
                    pos_ruby = i
                elif jogo.text == 'Sapphire':
                    pos_sapp = i
                elif jogo.text == 'Emerald':
                    pos_em = i

        cidade_ruby = onde_encontrar[pos_ruby].find('td').text
        cidade_sap = onde_encontrar[pos_sapp].find('td').text
        cidade_em = onde_encontrar[pos_em].find('td').text

        gravarLugares(id_pokemon, "Ruby", cidade_ruby, cidade)
        gravarLugares(id_pokemon, "Sapphire", cidade_sap, cidade)
        gravarLugares(id_pokemon, "Emerald", cidade_em, cidade)

    # gravarEvo(id_pokemon, id_ev.replace("#", '').replace(
    #     "use ", ""), tipo_ev.replace("use ", ""))
