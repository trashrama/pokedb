import requests
from bs4 import BeautifulSoup


def gravarItems(nome, categoria, efeito):

    f = open("items.txt", "a")

    if efeito == "NULL":
        f.writelines("('{}', '{}', {}),\n ".format(
            nome, categoria, efeito))
    else:
        f.writelines("('{}', '{}', '{}'),\n ".format(
            nome, categoria, efeito))

    f.close()


def gravarItemsChave(nome, efeito):

    f = open("itemsChave.txt", "a")

    if efeito == "NULL":
        f.writelines("('{}', {}),\n".format(nome, efeito))
    else:
        f.writelines("('{}', '{}'),\n".format(nome, efeito))

    f.close()


page = requests.get("https://pokemondb.net/item/all")
page2 = requests.get("https://pokemondb.net/item/type/key")

otherSoup = BeautifulSoup(page2.content, 'html.parser')
soup = BeautifulSoup(page.content, 'html.parser')

tabela = soup.find("table")
linhas = tabela.find_all("tr")

tabela2 = otherSoup.find("table")
linhas2 = otherSoup.find_all("tr")

for i in range(1, len(linhas)):
    aux = linhas[i].find_all("td")
    nome_item = (aux[0].text).replace("\n", "").replace("'", "''")
    nome_item = nome_item[1:]
    categoria = (aux[1].text).replace("\n", "").replace("'", "''")
    efeito = (aux[2].text).replace("\n", "").replace("'", "''")

    if not (categoria):
        categoria = "Others"
    if not efeito:
        efeito = "NULL"
    gravarItems(nome_item, categoria, efeito)

for i in range(1, len(linhas2)):
    aux = linhas2[i].find_all("td")
    nome_item = (aux[0].text).replace("\n", "").replace("'", "''")
    print(nome_item)
    nome_item = nome_item[1:]
    efeito = (aux[1].text).replace("\n", "").replace("'", "''")
    if not efeito:
        efeito = "NULL"
    gravarItemsChave(nome_item, efeito)
