#https://pokemondb.net/type/
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

navegador = webdriver.Chrome('chromedriver')

navegador.get(
    'https://pokemondb.net/pokedex/all')
