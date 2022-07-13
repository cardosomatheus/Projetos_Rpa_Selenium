from functools import partial
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class EsperarElementoNaoAtivo:
    """
        Class EsperarElementoNaoAtivo visá encontrar o elemento que não pode ser clicado e aguardar o load da pagina
    até se possivel a ação do click.
    Locator recebe o BY e o ELEMENT de busca, ex.(By.CSS_SELECTOR, 'button'), ex.(By.ID, 'finished')

        Com a Def __call__ Tranformamos os elementos com o BY e ELEMENT com valores iguais em um lista e
    colocamos umaa condicional no 1º item para saber se o elemento e 'unclick', retornamos 'True' ou 'False' para a resposta
    """
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, webdriver):
        elementos = fox.find_elements(*self.locator)
        if elementos:
            return 'unclick' in elementos[0].get_attribute('class')
        return False


def espera_elemento(by, elemento, webdriver):
    """ Faz  busca do BY e ELEMENT desejado e retorna 'True' ou 'False' para a resposta """
    f'Tentando encontrar BY: {by},  Element: {elemento}'
    if webdriver.find_elements(by, elemento):
        return True
    return False


#  Carregando a pagina
url = 'http://selenium.dunossauro.live/aula_09.html'
fox = Firefox()
wdw = WebDriverWait(fox, 10, poll_frequency=1)
fox.get(url)

#   fazendo uma parciação da variavel 'esperar_botao'
locator = (By.CSS_SELECTOR, 'button')
esperar_botao = partial(EsperarElementoNaoAtivo(locator))

#   Aguardando o carregamento do botão que o valor é 'unclick' e clicando nele.
wdw.until_not(esperar_botao)
fox.find_element_by_css_selector('button').click()

#   Confirmando sucesso do carregamento
wdw.until(partial(espera_elemento, By.ID, 'finished'))

sucesso = fox.find_element_by_css_selector('#finished')
assert sucesso.text == 'Carregamento concluído'
