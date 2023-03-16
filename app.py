from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# relacionamento evolucao
# id do pokemon anterior, id do pokemon seguinte, e o tipo (level or * STONE)
# fazer na vdd uma tabela

# amanha pensar na logica de evolucao pra um pokemon base ter ev anterior null
# uma ultima evolucao ter uma proxima ev null


def gravar(id, nome, tipo1, tipo2, habilidade, hp, attack, sp_atk,
           sp_def, speed, specie, altura, peso):
    f = open("pokedb_pokemons.txt", "a")
    f.writelines("VALUES ({}, '{}', '{}', '{}', '{}', {}, {}, {}, {}, {}, '{}', {}, {})\n".format(
        id, nome, tipo1, tipo2, habilidade, hp, attack, sp_atk,
        sp_def, speed, specie, altura, peso))
    f.close()


def gravar_evolucao(id_atual, id_anterior, id_seg, tipo_ev):
    f = open("pokedb_ev.txt", "a")
    f.writelines("VALUES ({}, {}, {}, {})\n".format(
        id_atual, id_anterior, id_seg, tipo_ev))
    f.close()


navegador = webdriver.Firefox(r'/usr/local/bin/')


navegador.get(
    'https://pokemondb.net/pokedex/all')


WebDriverWait(navegador, 100).until(
    EC.presence_of_element_located((By.TAG_NAME, 'tbody')))

bloco = navegador.find_element(By.TAG_NAME, 'tbody')
linhas = bloco.find_elements(By.TAG_NAME, 'tr')

navVoltou = False

for i in range(len(linhas)):

    if navVoltou:
        WebDriverWait(navegador, 100).until(
            EC.presence_of_element_located((By.TAG_NAME, 'tbody')))
        WebDriverWait(navegador, 100).until(
            EC.presence_of_element_located((By.TAG_NAME, 'tr')))
        bloco = navegador.find_element(By.TAG_NAME, 'tbody')
        navegador.implicitly_wait(10)
        linhas = bloco.find_elements(By.TAG_NAME, 'tr')

    WebDriverWait(navegador, 100).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, 'td')))
    col = linhas[i].find_elements(By.TAG_NAME, 'td')
    id = col[0].text

    if id == 494:
        break

    try:
        nome = (col[1].text).split('\n')
        nome = nome[1]
    except:
        nome = col[1].text

    print(nome)

    if not (("Alolan" in nome) or ("Mega" in nome) or ("Partner" in nome) or ("Galarian" in nome)):
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

        WebDriverWait(navegador, 100).until(
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

        WebDriverWait(navegador, 100).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, 'a')))

        habilidade = trs[5].find_element(By.CLASS_NAME, "text-muted")
        habilidade = habilidade.find_element(By.TAG_NAME, "a")
        habilidade = habilidade.text
        print(habilidade)

        lista_efetividade = []

        tabela_fraq = navegador.find_element(By.XPATH,
                                             "(//tr)[24]")

        WebDriverWait(navegador, 100).until(
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
            elif (el.text == "⅛"):
                lista_efetividade.append(1/8)

        id_ant = ""
        tipo_ev = ""

        try:
            evo_card = navegador.find_element(
                By.CLASS_NAME, 'infocard-list-evo')
            level_ev = evo_card.find_elements(
                By.CLASS_NAME, 'infocard-arrow')
            divs = evo_card.find_elements(By.TAG_NAME, 'div')

            for index, div in enumerate(divs):
                spans = div.find_elements(By.TAG_NAME, 'span')
                num = spans[2].find_element(By.TAG_NAME, 'small')
                num = num.text

                if (index == 0):
                    id_ant = "NULL"

                tipo_ev = ""

                num = num[1:]

                if (num == id and index != 0):

                    try:
                        id_ev = divs[index+1]
                        id_ev = id_ev.find_elements(By.TAG_NAME, 'small')
                        print("pego ar kkk", end="")
                        print(len(id_ev))
                        id_ev = id_ev[0].text

                    except:
                        id_ev = "NULL"

                    try:
                        tipo_ev = level_ev[index-1].text
                    except:
                        tipo_ev = "NULL"

                    break
                elif (num == id and index == 0):
                    try:
                        id_ant = "NULL"
                        id_ev = divs[index+1]
                        id_ev = id_ev.find_elements(By.TAG_NAME, 'small')
                        id_ev = id_ev[0].text

                    except:
                        id_ev = "NULL"
                        nivel_evolucao = "NULL"
                    break
                if (num != id):
                    id_ant = num
        except:
            id_ev = "NULL"
            tipo_ev = "NULL"

        if (tipo_ev != "NULL"):
            try:
                tipo_ev = tipo_ev.replace("(Level ", "")
                tipo_ev = tipo_ev[:-1]

            except:
                pass

        if id_ev != "NULL":
            id_ev = id_ev[1:]

        if tipo_ev == "":
            tipo_ev = "0"
        if "Stone" in tipo_ev:
            if len(tipo_ev > 20):
                onde = tipo_ev.find(",")
                tipo_ev = tipo_ev[:onde]
            tipo_ev = tipo_ev[4:]
            tipo_ev = tipo_ev.upper()
        elif "high" in tipo_ev:
            tipo_ev = tipo_ev[5:]
            tipo_ev = tipo_ev.upper()

        print("num: " + num)
        print("id_evo: "+id_ev)
        print("id_evo: "+id_ant)

        print("n.E: "+tipo_ev)

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
        gravar(id, nome, tipo1, tipo2, habilidade, hp, attack, sp_atk,
               sp_def, speed, specie, altura, peso)
        gravar_evolucao(id, id_ant, id_ev, tipo_ev)

        lista_efetividade = []
