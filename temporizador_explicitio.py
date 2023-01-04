from functools import partial
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# --------------- Função usadas no código ---------------
def espera_elemento(by, elemento):
    """ Procura o elemento desejado"""
    f'Tentando encontrar BY: {by},  Element: {elemento}'
    if fox.find_element(by, elemento):
        return True
    return False


#  --------------- Carregando a pagina ---------------
url = 'http://selenium.dunossauro.live/aula_09_a.html'
fox = Firefox()
wdw = WebDriverWait(fox, 10, poll_frequency=1)
fox.get(url)

#   --------------- fazendo uma parciação dos elemetos ---------------
esperar_botao = partial(espera_elemento,
                        By.CSS_SELECTOR, 'button')

#   --------------- Aguardando o carregamento o botão e clicando nele ---------------
wdw.until(esperar_botao, 'button')
fox.find_element_by_css_selector('button').click()

#   --------------- Confirmando sucesso do carregamento ---------------
wdw.until(partial(espera_elemento, By.ID, 'finished'))
sucesso = fox.find_element_by_css_selector('#finished')
assert sucesso.text == 'Carregamento concluído'
