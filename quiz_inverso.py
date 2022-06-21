from selenium.webdriver import Firefox
from time import sleep
from pprint import pprint


def net_links(browser, elemento):
    """
    :param browser: navegador escolhido
    :param elemento: webelement ex: [aside, main, body, ul, li]
    :return: O dicionário RESULTADO completo
    AnCORAS: Uma lista que armazena as ancoras
    """
    resultado = {}
    webelement = browser.find_element_by_tag_name(elemento)  # colocando o ASIDE em uma varivel e
    sleep(1)

    ancoras = webelement.find_elements_by_tag_name('a')  # Colocando as ancoras 'a' em uma lista
    sleep(2)

    for ancora in ancoras:  # Definindo as keys e os values do Resultado{}
        resultado[ancora.text] = ancora.get_attribute('href')
    return resultado


# Abertura do navegador e URl
browser = Firefox()
browser.get('https://selenium.dunossauro.live/aula_04.html')

exercicios = net_links(browser, 'main')
aulas = net_links(browser, 'aside')


pprint(aulas)
browser.get(exercicios['Exercício 3'])  # Entrando no exercicio 3