import requests
from bs4 import BeautifulSoup


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

    f = open("pokedb_pokemons.txt", "a")

    for i in range(len(lista_tipos)):
        if (lista_tipos[i] == tipo1):
            tipo1_id = i+1
            break
    for i in range(len(lista_tipos)):
        if (lista_tipos[i] == tipo2):
            tipo2_id = i+1
            break

    if tipo2 != "NULL":
        f.writelines("('{}', '{}', '{}', '{}', {}, {}, {}, {}, {}, {}, '{}', {}, {}, '{}'),\n".format(
            nome, tipo1, tipo2, habilidade, hp, attack, sp_atk,
            sp_def, speed, bufunfa, specie, altura, peso, cidade))
    else:
        f.writelines("('{}', '{}', NULL, '{}', {}, {}, {}, {}, {}, {}, '{}', {}, {}, '{}'),\n".format(
            nome, tipo1, habilidade, hp, attack, sp_atk,
            sp_def, speed, bufunfa, specie, altura, peso, cidade))
    f.close()


def gravarLugares(id_pokemon, jogo, lugares):
    f = open("pokedb_lugares.txt", "a")

    lista_lugares = ['National Park', 'Mt. Moon', 'Union Cave', 'Mt. Mortar', 'Route 12', 'Route 15', 'Pewter City', 'Pallet Town', 'Underground Path 5-6', 'Slowpoke Well', 'Route 23', 'Cerulean City', 'Route 2', 'Celadon City', 'Route 24', 'Viridian City', 'Dark Cave', 'Great Marsh', 'Mt. Silver', 'Power Plant', 'Route 4', '210', 'Viridian Forest', 'Tohjo Falls', 'Oreburgh City', 'Route 209', 'Vermilion City', 'Route 14',
                     'Cinnabar Island', 'Victory Road', 'Pokémon Tower', 'Route 6', 'Ice Path', 'Route 20', 'Route 18', 'Route 1', 'Whirl Islands', 'Route 22', 'Route 11', 'Safari Zone', 'Route 8', 'Seafoam Islands', 'Route 19', "Diglett's Cave", 'Pokémon Mansion', 'Rock Tunnel', 'Route 7', 'Route 9', 'Route 10', 'Route 3', 'Route 17', 'Cerulean Cave', 'Fuchsia City', 'Route 21', 'Route 16', 'Route 25', 'Route 28', 'Route 13', 'Route 5']

    try:
        lugares = lugares.split(",")
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
                f.writelines("({}, '{}', {}),\n".format(
                    id_pokemon, jogo.upper().replace("'", "''"), id_lugar))

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
                id_pokemon, jogo.upper().replace("'", "''"), id_lugar))

    f.close()


def gravarEvo(id_pokemon, id_prox, tipo):
    f = open("pokedb_evolucoes.txt", "a")
    if not (id_prox == 'NULL' and tipo == 'NULL' or id_pokemon == id_prox):
        try:
            if (int(id_prox) < 151):
                f.writelines("({}, {}, '{}'),\n".format(
                    id_pokemon, id_prox, tipo.replace("(", "").replace(")", "")))
        except:
            f.writelines("({}, {}, '{}'),\n".format(
                id_pokemon, id_prox, tipo.replace("(", "").replace(")", "")))
    f.close()


for i in range(1, 379):

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

    try:
        cards = soup.find(class_="infocard-list-evo")
        total_ev = cards.find_all("div")
        try:
            spansdivididos = soup.find(class_='infocard-evo-split')
            print(spansdivididos)
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
                except:
                    id_ev = 'NULL'
                try:
                    tipo_ev = nivel_ev[i].text
                    print(tipo_ev)
                except:
                    tipo_ev = "NULL"
                    break
            elif (num == id_pokemon and i == 0):
                try:
                    id_ev = total_ev[i +
                                     1].find('span', {'class': ["infocard-lg-data", 'text-muted']}).text()
                    id_ev = total_ev[i+1].find("small").text.replace("#", "")
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

    print("num: " + id_pokemon)
    print("id_evo: "+id_ev)
    print("n.E: "+tipo_ev)

    string = soup.find(
        text=lambda text: text and 'Where to find' in text).parent
    proximo = string.find_next_sibling()

    onde_encontrar = proximo.find_all("tr")

    jogos = onde_encontrar[0].find_all("th")
    jogos = jogos[0].find_all("span")

    red = ""
    blue = ""
    yellow = ""

    if (len(jogos) == 2):
        for i in range(0, 2):
            find = onde_encontrar[i].find_all("td")
            if (i == 0):
                red, blue = find[0].text, find[0].text
            else:
                yellow = find[0].text
    else:
        find = onde_encontrar[i].find_all("td")
        red, blue, yellow = find[0].text, find[0].text, find[0].text

    print("onde encontrar red: " + red)
    print("onde encontrar blue: " + blue)
    print("onde encontrar yellow: " + yellow)

    print("num: " + id_pokemon)
    print("id_evo: "+id_ev)
    print("id_evo: "+id_ant)
    print("n.E: "+tipo_ev)

    string = soup.find(
        text=lambda text: text and 'Where to find' in text).parent
    proximo = string.find_next_sibling()

    onde_encontrar = proximo.find_all("tr")

    jogos = onde_encontrar[0].find_all("th")
    jogos = jogos[0].find_all("span")

    red = ""
    blue = ""
    yellow = ""

    if (len(jogos) == 2):
        for i in range(0, 2):
            find = onde_encontrar[i].find_all("td")
            if (i == 0):
                red, blue = find[0].text, find[0].text
            else:
                yellow = find[0].text
    else:
        find = onde_encontrar[i].find_all("td")
        red, blue, yellow = find[0].text, find[0].text, find[0].text

    print("onde encontrar red: " + red)
    print("onde encontrar blue: " + blue)
    print("onde encontrar yellow: " + yellow)

    gravar(id_pokemon, nome, tipo1, tipo2, hab,
           status[0], status[1], status[2], status[3], status[4], status[5], especie, altura, peso, cidade)

    gravarLugares(id_pokemon, "Red", red)
    gravarLugares(id_pokemon, "Blue", blue)
    gravarLugares(id_pokemon, "Yellow", yellow)

    gravarEvo(id_pokemon, id_ev.replace("#", '').replace(
        "use ", ""), tipo_ev.replace("use ", ""))
