from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def gravarFraquezas(tipo, atk, defesa):

    f = open("pokedb_stats_{}_.txt".format(tipo), "a")
    f.writelines('-- {}\n'.format(tipo))

    f.write('VALUES (')
    for i, item in enumerate(atk):
        if (i == len(atk)):
            f.writelines("{})".format(item))
        f.write("{}, ".format(item))
    f.write('VALUES (')

    for i, item in enumerate(defesa):
        if (i == len(defesa)):
            f.writelines("{})".format(item))
        f.write("{}, ".format(item))

    f.close()


def bayCity(el, ini, fim, pulo=1):
    lista = []
    for i in range(ini, fim, pulo):
        if ((el[i].text) == ""):
            lista.append(1)
        elif (el[i].text == "½"):
            lista.append(1/2)
        elif (el[i].text == "¼"):
            lista.append(1/4)
        elif (el[i].text == "2"):
            lista.append(2)
        elif (el[i].text == "0"):
            lista.append(0)

    # atk
    if (fim == 324 and pulo != 1):
        return lista, ini + 1

    # def
    else:
        aux = fim
        ini = fim
        fim = aux+18
        return lista, ini, fim


navegador = webdriver.Chrome("chromedriver")
navegador.get("https://pokemondb.net/type/")

tabela = navegador.find_element(By.CLASS_NAME, "type-table")

WebDriverWait(navegador, 10).until(
    EC.presence_of_all_elements_located((By.TAG_NAME, 'td')))

el = tabela.find_elements(By.TAG_NAME, "td")

ini_def = 0
fim_def = 18

ini_atk = 0
fim_atk = 324
pulo_atk = 18
i = 0

aux = 0


normal_def, ini_def, fim_def = bayCity(el, ini_def, fim_def)
normal_atk, ini_atk = bayCity(el, ini_atk, fim_atk, pulo_atk)


fogo_def, ini_def, fim_def = bayCity(el, ini_def, fim_def)
fogo_atk, ini_atk = bayCity(el, ini_atk, fim_atk, pulo_atk)
print(fogo_atk)

agua_def, ini_def, fim_def = bayCity(el, ini_def, fim_def)
agua_atk, ini_atk = bayCity(el, ini_atk, fim_atk, pulo_atk)

eletrico_def, ini_def, fim_def = bayCity(el, ini_def, fim_def)
eletrico_atk, ini_atk = bayCity(el, ini_atk, fim_atk, pulo_atk)

grama_def, ini_def, fim_def = bayCity(el, ini_def, fim_def)
grama_atk, ini_atk = bayCity(el, ini_atk, fim_atk, pulo_atk)

print(ini_def, fim_atk)

gelo_def, ini_def, fim_def = bayCity(el, ini_def, fim_def)
gelo_atk, ini_atk = bayCity(el, ini_atk, fim_atk, pulo_atk)

lutador_def, ini_def, fim_def = bayCity(el, ini_def, fim_def)
lutador_atk, ini_atk = bayCity(el, ini_atk, fim_atk, pulo_atk)

venenoso_def, ini_def, fim_def = bayCity(el, ini_def, fim_def)
venenoso_atk, ini_atk = bayCity(el, ini_atk, fim_atk, pulo_atk)

terra_def, ini_def, fim_def = bayCity(el, ini_def, fim_def)
terra_atk, ini_atk = bayCity(el, ini_atk, fim_atk, pulo_atk)

voador_def, ini_def, fim_def = bayCity(el, ini_def, fim_def)
voador_atk, ini_atk = bayCity(el, ini_atk, fim_atk, pulo_atk)

psiquico_def, ini_def, fim_def = bayCity(el, ini_def, fim_def)
psiquico_atk, ini_atk = bayCity(el, ini_atk, fim_atk, pulo_atk)

inseto_def, ini_def, fim_def = bayCity(el, ini_def, fim_def)
inseto_atk, ini_atk = bayCity(el, ini_atk, fim_atk, pulo_atk)

pedra_def, ini_def, fim_def = bayCity(el, ini_def, fim_def)
pedra_atk, ini_atk = bayCity(el, ini_atk, fim_atk, pulo_atk)

fantasma_def, ini_def, fim_def = bayCity(el, ini_def, fim_def)
fantasma_atk, ini_atk = bayCity(el, ini_atk, fim_atk, pulo_atk)

dragao_def, ini_def, fim_def = bayCity(el, ini_def, fim_def)
dragao_atk, ini_atk = bayCity(el, ini_atk, fim_atk, pulo_atk)

noturno_def, ini_def, fim_def = bayCity(el, ini_def, fim_def)
noturno_atk, ini_atk = bayCity(el, ini_atk, fim_atk, pulo_atk)

aco_def, ini_def, fim_def = bayCity(el, ini_def, fim_def)
aco_atk, ini_atk = bayCity(el, ini_atk, fim_atk, pulo_atk)

fada_def, ini_def, fim_def = bayCity(el, ini_def, fim_def)
fada_atk, ini_atk = bayCity(el, ini_atk, fim_atk, pulo_atk)

gravarFraquezas('normal', normal_atk, normal_def)
gravarFraquezas('fogo', fogo_atk, fogo_def)
gravarFraquezas('agua', agua_atk, agua_def)
gravarFraquezas('eletrico', eletrico_atk, eletrico_def)
gravarFraquezas('grama', grama_atk, grama_def)
gravarFraquezas('gelo', gelo_atk, gelo_def)
gravarFraquezas('lutador', lutador_atk, lutador_def)
gravarFraquezas('venenoso', venenoso_atk, venenoso_def)
gravarFraquezas('terra', terra_atk, terra_def)
gravarFraquezas('voador', voador_atk, voador_def)
gravarFraquezas('psiquico', psiquico_atk, psiquico_def)
gravarFraquezas('inseto', inseto_atk, inseto_def)
gravarFraquezas('pedra', pedra_atk, pedra_def)
gravarFraquezas('fantasma', fantasma_atk, fantasma_def)
gravarFraquezas('dragao', dragao_atk, dragao_def)
gravarFraquezas('noturno', noturno_atk, noturno_def)
gravarFraquezas('aco', aco_atk, aco_def)
gravarFraquezas('fada', fada_atk, fada_def)
