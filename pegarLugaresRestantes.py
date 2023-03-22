import requests
from bs4 import BeautifulSoup

# codigo pra pegar os lugares restantes

lugares = []
sites = ["kanto",
         "johto", "hoenn"]

cont = 0

for i in range(len(sites)):
    page = requests.get(
        "https://pokemondb.net/location/")
    soup = BeautifulSoup(page.content, 'html.parser')
    tabela = soup.find(id=f"loc-{sites[i]}")
    tabela = tabela.find('div', {'class': 'grid-row'})

    if i == 0:
        regiao = 'Kanto'
    elif i == 1:
        regiao = 'Johto'
    else:
        regiao = 'Hoenn'
    items = tabela.find_all()

    for j in range(0, len(items)):
        item = items[j].text
        item = item.replace("'", "''").replace("\n", "")
        if item != "" and len(item) < 30:
            for i in range(len(lugares)):

                if lugares[i][1] == item:
                    lugares[i][1] = "{}''s {}".format(
                        lugares[i][1], lugares[i][2])
                    item = "{}''s {}".format(
                        regiao, item)

            lugares.append([cont, item, regiao])
            cont = cont+1

    for lugar in lugares:
        print(f"'{lugar[1]}',")
        # print("({}, '{}', '{}'),".format(lugar[0], lugar[1], lugar[2]))
