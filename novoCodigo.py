import requests
from bs4 import BeautifulSoup

for i in range(1, 151):

    page = requests.get("https://pokemondb.net/pokedex/{}".format(i))
    soup = BeautifulSoup(page.content, 'html.parser')

    regiao = "Kanto"
    # nome do pokemon

    nome = soup.find("h1").text
    print(nome)

    tabela = soup.find_all('table', class_="vitals-table")
    linhas_info = tabela[0].find_all('tr')

    # id do pokemon
    id_pokemon = linhas_info[0].find("strong").text
    # tipo do pokemon
    tipos = linhas_info[1].find_all('a')
    for tipo in tipos:
        print(tipo.text)
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
        nivel_ev = cards.find_all(class_="infocard infocard-arrow")

        for i in range(len(total_ev)):
            num = total_ev[i].find("small").text
            num = num.replace("#", "")

            if (i == 0):
                id_ant = "NULL"

            if (num == id_pokemon and i != 0):
                try:
                    id_ev = total_ev[i+1].find("small").text
                    id_ev = id_ev.replace("#", "")
                except:
                    id_ev = "NULL"
                try:
                    tipo_ev = nivel_ev[i-1].text
                except:
                    tipo_ev = "NULL"
                break

            elif (num == id_pokemon and i == 0):
                try:
                    id_ant = "NULL"
                    id_ev = total_ev[i+1].find("small").text
                except:
                    id_ev = "NULL"
                    nivel_evolucao = "NULL"
                break
            if (num != id):
                id_ant = num
    except:
        id_ev = "NULL"
        id_ant = "NULL"

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
