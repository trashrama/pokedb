import requests
from bs4 import BeautifulSoup

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
                if not ("#" in total_ev[i+1].find("small").text or id == 102 or id == 104 or id == 109 or id == 79 or id == 123 or id == 133):
                    id_ev = total_ev[i+2].find("small").text
                    id_ev = id_ev.replace("#", "")
                else:
                    id_ev = total_ev[i+1].find("small").text
                    id_ev = id_ev.replace("#", "")
            except:
                id_ev = "NULL"
            try:
                if modoDoido:
                    tipo_ev = nivel_ev[i-1].text.replace("#", "")
                else:
                    tipo_ev = nivel_ev[i].text.replace("#", "")
            except:
                tipo_ev = "NULL"
            break

        elif (num == id_pokemon and i == 0):
            try:
                id_ant = "NULL"
                id_ev = total_ev[i+1].find("small").text.replace("#", "")
            except:
                id_ev = "NULL"
            try:
                tipo_ev = nivel_ev[i].text
            except:
                tipo_ev = "NULL"
            break
        if (num != id):
            id_ant = num
except:
    id_ev = "NULL"
    id_ant = "NULL"
    tipo_ev = "NULL"

for i in range(105, 152):

    page = requests.get("https://pokemondb.net/pokedex/{}".format(i))
    soup = BeautifulSoup(page.content, 'html.parser')

    cards = soup.find(class_="infocard-list-evo")
    elementos = cards.find_all('span')
    for i in range(len(elementos)):

        if 'infocard-evo-split' in elementos[i]['class']:
            print(elementos[i].text)
