import requests
from bs4 import BeautifulSoup

for indie in range(1, 4):
    page = requests.get(
        "https://pokemondb.net/move/generation/{}".format(indie))
    soup = BeautifulSoup(page.content, 'html.parser')

    tabelas = soup.find_all("tbody")

    for i in range(len(tabelas)):
        tr = tabelas[i].find_all("tr")
        for linha in tr:
            tds = linha.find_all("td")
            mov = tds[0].text.replace("'", "''")
            tipo = tds[1].text.replace("'", "''")
            cat = tds[2]
            cat = cat.get('data-sort-value').upper().replace("'", "''")
            power = tds[3].text.replace("'", "''")
            accuracity = tds[4].text.replace("'", "''")
            pp = tds[5].text.replace("'", "''")
            effect = tds[6].text.replace("'", "''")

            if power == '—':
                power = "NULL"
            elif power == "∞":
                power = '-1'
            if accuracity == '—':
                accuracity = 'NULL'
            elif accuracity == '∞':
                accuracity = "-1"
            if effect == '—':
                effect = "NULL"
            if pp == "—":
                pp = "NULL"

            print(
                f"('{mov}', '{tipo}', '{cat}', {power}, {accuracity}, {pp}, {indie}, '{effect}'),")
