
import requests
from bs4 import BeautifulSoup

habilidadesSite = requests.get(
    "https://pokemondb.net/ability/")

soup = BeautifulSoup(habilidadesSite.content, 'html.parser')
tabelas = soup.find("tbody")
tr = tabelas.find_all("tr")

for linha in tr:
    tds = linha.find_all('td')
    hab = tds[0].text.replace("'", "''")
    desc = tds[2].text
    desc = desc.replace("'", "''")
    print(f"('{hab}', '{desc}'),")
