import requests
from bs4 import BeautifulSoup

lista = []
page = requests.get("https://deetlist.com/dragoncity/all-dragons/")

soup = BeautifulSoup(page.content, "html.parser")

resposta = soup.find_all("div", attrs={"class": "drag"})

for resp in resposta:
    lista.append(resp.text)

for nome in lista:

    page2 = requests.get(
        f'https://deetlist.com/dragoncity/dragon/{nome.replace(" Dragon", "")}')

    soup2 = BeautifulSoup(page2.content, "html.parser")

    print(nome)
    bolds = soup2.find("div", id="self_bio")
    bolds = bolds.find_all("b")
    print(bolds)
    raridade = bolds[0].text
    tipo = bolds[1].text

    print(f'{nome} {raridade} {tipo}')
