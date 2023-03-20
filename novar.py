from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def gravarFraquezas(nome, atk, defesa):

    f = open("pokedb_stats_fraqatq.txt", "a")
    f1 = open("pokedb_stats_fraqdef.txt", "a")

    lista_tipos = ['Normal',
                   'Fire',
                   'Water',
                   'Electric',
                   'Grass',
                   'Ice',
                   'Fighting',
                   'Poison',
                   'Ground',
                   'Flying',
                   'Psychic',
                   'Bug',
                   'Rock',
                   'Ghost',
                   'Dragon',
                   'Dark',
                   'Steel',
                   'Fairy']

    for i in range(len(lista_tipos)):
        print(lista_tipos[i], nome)
        if (lista_tipos[i] == nome):
            tipo = i+1
            break

    f.writelines("('{}', {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}),\n".format(tipo,
                 atk[0], atk[1], atk[2], atk[3], atk[4], atk[5], atk[6], atk[7], atk[8], atk[9], atk[10], atk[11], atk[12], atk[13], atk[14], atk[15], atk[16], atk[17]))

    f1.writelines("('{}', {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}),\n".format(tipo, defesa[0], defesa[1], defesa[2], defesa[3], defesa[
                  4], defesa[5], defesa[6], defesa[7], defesa[8], defesa[9], defesa[10], defesa[11], defesa[12], defesa[13], defesa[14], defesa[15], defesa[16], defesa[17]))

    f.close()
    f1.close()


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

gravarFraquezas('Normal', normal_atk, normal_def)
gravarFraquezas('Fire', fogo_atk, fogo_def)
gravarFraquezas('Water', agua_atk, agua_def)
gravarFraquezas('Electric', eletrico_atk, eletrico_def)
gravarFraquezas('Grass', grama_atk, grama_def)
gravarFraquezas('Ice', gelo_atk, gelo_def)
gravarFraquezas('Fighting', lutador_atk, lutador_def)
gravarFraquezas('Poison', venenoso_atk, venenoso_def)
gravarFraquezas('Ground', terra_atk, terra_def)
gravarFraquezas('Flying', voador_atk, voador_def)
gravarFraquezas('Psychic', psiquico_atk, psiquico_def)
gravarFraquezas('Bug', inseto_atk, inseto_def)
gravarFraquezas('Rock', pedra_atk, pedra_def)
gravarFraquezas('Ghost', fantasma_atk, fantasma_def)
gravarFraquezas('Dragon', dragao_atk, dragao_def)
gravarFraquezas('Dark', noturno_atk, noturno_def)
gravarFraquezas('Steel', aco_atk, aco_def)
gravarFraquezas('Fairy', fada_atk, fada_def)
