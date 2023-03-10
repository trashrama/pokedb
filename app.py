from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def gravar(id, nome, alolan, tipo1, tipo2, habilidade, hp, attack, sp_atk,
           sp_def, speed, specie, altura, peso, id_ev, level):
    f = open("pokedb_pokemons.txt", "a")
    f.writelines('VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})\n'.format(
        id, nome, alolan, tipo1, tipo2, habilidade, hp, attack, sp_atk,
        sp_def, speed, specie, altura, peso, id_ev, level))
    f.close()


def gravarFraquezas(id, normal, fogo, agua, eletr, grama, gelo, lut, ven, terr, voador, psi, inseto, roc, fant, drag, somb, aco, fada):
    f = open("pokedb_fraquezas.txt", "a")
    f.writelines('VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})\n'.format(
        id, normal, fogo, agua, eletr, grama, gelo, lut, ven, terr, voador, psi, inseto, roc, fant, drag, somb, aco, fada))
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

navVoltou = False

for i in range(len(linhas)):

    if navVoltou:
        WebDriverWait(navegador, 10).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, 'tr')))
        bloco = navegador.find_element(By.TAG_NAME, 'tbody')
        linhas = bloco.find_elements(By.TAG_NAME, 'tr')

    col = linhas[i].find_elements(By.TAG_NAME, 'td')
    id = col[0].text

    alolan = False

    try:
        nome = (col[1].text).split('\n')
        nome = nome[1]
    except:
        nome = col[1].text

    print(nome)

    if ("Alolan" in nome):
        alolan = True

    tipos = col[2].text
    tipos = tipos.split("\n")

    total = col[3].text
    hp = col[4].text
    attack = col[5].text
    sp_atk = col[6].text
    sp_def = col[7].text
    speed = col[8].text

    # novo codigo
    link = col[1].find_element(By.TAG_NAME, 'a')

    link.click()

    navegador.implicitly_wait(10)

    WebDriverWait(navegador, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "(//div[@class='grid-col span-md-6 span-lg-4'])[1]")))

    bloc = navegador.find_element(
        By.XPATH, "(//div[@class='grid-col span-md-6 span-lg-4'])[1]")

    table_aleatoria = bloc.find_element(By.CLASS_NAME, 'vitals-table')
    tabela_especies = table_aleatoria.find_element(By.XPATH, '(//tr)[3]')
    trs = table_aleatoria.find_elements(By.TAG_NAME, 'td')
    print(len(trs))

    specie = trs[2].text.replace("Pokémon", "")
    specie = specie[:-1]
    print(specie)
    altura = trs[3].text
    print(altura)

    altura = altura[:altura.find("(") - 3]

    peso = trs[4].text
    peso = peso[:peso.find("(")-4]

    WebDriverWait(navegador, 10).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, 'a')))

    habilidade = trs[5].find_element(By.CLASS_NAME, "text-muted")
    habilidade = habilidade.find_element(By.TAG_NAME, "a")
    habilidade = habilidade.text
    print(habilidade)

    lista_efetividade = []

    tabela_fraq = navegador.find_element(By.XPATH,
                                         "(//tr)[24]")

    WebDriverWait(navegador, 10).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, 'td')))
    el_tbfq = tabela_fraq.find_elements(By.TAG_NAME, 'td')

    for el in el_tbfq:
        print(el.text)
        if ((el.text) == "" or (el.text == "0")):
            lista_efetividade.append(0)
        elif (el.text == "½"):
            lista_efetividade.append(1/2)
        elif (el.text == "¼"):
            lista_efetividade.append(1/4)
        elif (el.text == "2"):
            lista_efetividade.append(2)
        elif (el.text == "4"):
            lista_efetividade.append(4)
        elif (el.text == "⅛	"):
            lista_efetividade.append(1/8)
    tabela_fraq = navegador.find_element(By.XPATH,
                                         "(//tr)[26]")
    el_tbfq = tabela_fraq.find_elements(By.TAG_NAME, 'td')

    for el in el_tbfq:
        print(el.text)
        if ((el.text) == "" or (el.text == "0")):
            lista_efetividade.append(0)
        elif (el.text == "½"):
            lista_efetividade.append(1/2)
        elif (el.text == "¼"):
            lista_efetividade.append(1/4)
        elif (el.text == "2"):
            lista_efetividade.append(2)
        elif (el.text == "4"):
            lista_efetividade.append(4)

    try:
        evo_card = navegador.find_element(By.CLASS_NAME, 'infocard-list-evo')
        level_ev = evo_card.find_elements(
            By.CLASS_NAME, 'infocard-arrow')
        divs = evo_card.find_elements(By.TAG_NAME, 'div')

        for index, div in enumerate(divs):
            spans = div.find_elements(By.TAG_NAME, 'span')
            num = spans[2].find_element(By.TAG_NAME, 'small')
            num = num.text

            level = "NULL"
            id_ev = ""

            num = num[1:]

            if (num == id and index != 0):

                try:
                    id_ev = divs[index+1]
                    id_ev = id_ev.find_elements(By.TAG_NAME, 'small')
                    id_ev = id_ev[0].text
                except:
                    id_ev = "NULL"

                try:
                    level = level_ev[index-1].text
                except:
                    level = "NULL"

                break
            elif (num == id and index == 0):
                try:
                    id_ev = divs[index+1]
                    id_ev = id_ev.find_elements(By.TAG_NAME, 'small')
                    id_ev = id_ev[0].text
                except:
                    id_ev = "NULL"
                    nivel_evolucao = "NULL"
                break
    except:
        id_ev = "NULL"
        level = "NULL"

    if (level != "NULL"):
        if not (level.isnumeric()):
            level = level[level.find("("):level.find(")")]
            level = level.upper()
        level = level[level.find(" ")+1: -1]

    if id_ev != "NULL":
        id_ev = id_ev[1:]

    print("num: " + num)
    print("id_evo: "+id_ev)
    print("n.E: "+level)


# nivel q vai evoluir

    print(lista_efetividade)
    navVoltou = True
    navegador.back()

    tipo1 = tipos[0]

    try:
        tipo2 = tipos[1]
    except:
        tipo2 = "NULL"

    print(habilidade)
    print(alolan)
    gravar(id, nome, alolan, tipo1, tipo2, habilidade, hp, attack, sp_atk,
           sp_def, speed, specie, altura, peso, id_ev, level)

    gravarFraquezas(id, lista_efetividade[0], lista_efetividade[1], lista_efetividade[2], lista_efetividade[3], lista_efetividade[4], lista_efetividade[5], lista_efetividade[6],
                    lista_efetividade[7], lista_efetividade[8], lista_efetividade[9], lista_efetividade[10], lista_efetividade[11], lista_efetividade[12], lista_efetividade[13], lista_efetividade[14], lista_efetividade[15], lista_efetividade[16], lista_efetividade[17])

    lista_efetividade = []
