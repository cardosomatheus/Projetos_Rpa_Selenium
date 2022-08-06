from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from functools import partial
from selenium.webdriver.common.by import By


def espera_elemento(by, elemento, webdriver):
    """ Procura o elemento desejado e mostra a localização da classe"""
    f'Tentando encontrar BY: {by},  Element: {elemento}'
    if webdriver.find_element(by, elemento):
        print(f'Selenium Localizado, local: {webdriver.find_element(by, elemento)}')
        return True
    return False


fox = Firefox()
#   ----------Abertura da pagina ----------
wdw = WebDriverWait(fox, 10)
fox.get('http://selenium.dunossauro.live/exercicio_09.html')

#   ---------- Busca da classe  ----------
busca_elemento = partial(espera_elemento, By.CLASS_NAME, 'selenium')
wdw.until(busca_elemento)
fox.find_element(By.CLASS_NAME, 'selenium')


