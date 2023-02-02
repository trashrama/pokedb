from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def gravar(id, nome, total, hp, attack, sp_attack, sp_def, speed):
    f = open("pokedb_pokemons.txt", "a")
    f.writelines('({}, {}, {}, {}, {}, {}, {}, {})\n'.format(
        id, nome, total, hp, attack, sp_attack, sp_def, speed))
    f.close()


def gravar_dois(nome, tipo):
    f = open("pokedb_types.txt", "a")
    f.writelines('({}, {})\n'.format(nome, tipo))
    f.close()


navegador = webdriver.Chrome('chromedriver')

navegador.get(
    'https://pokemondb.net/pokedex/all')


WebDriverWait(navegador, 10).until(
    EC.presence_of_all_elements_located((By.TAG_NAME, 'tr')))
bloco = navegador.find_element(By.TAG_NAME, 'tbody')
linhas = bloco.find_elements(By.TAG_NAME, 'tr')

for i in range(len(linhas)):

    col = linhas[i].find_elements(By.TAG_NAME, 'td')
    id = col[0].text

    try:
        nome = (col[1].text).split('\n')
        nome = nome[1]
    except:
        nome = col[1].text

    print(nome)

    tipos = col[2].text
    tipos = tipos.split("\n")

    total = col[3].text
    hp = col[4].text
    attack = col[5].text
    sp_atk = col[6].text
    sp_def = col[7].text
    speed = col[8].text

    gravar(id, nome, total, hp, attack, sp_atk, sp_def, speed)

    for tipo in tipos:
        gravar_dois(nome, tipo)
