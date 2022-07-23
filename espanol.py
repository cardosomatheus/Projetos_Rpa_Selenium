from selenium.webdriver import Firefox
from time import sleep
import pyautogui

#   Inicialização
fox = Firefox()
fox.get('https://www.minjus.gob.pe/resoluciones-ttaip/')
sleep(1.5)

# Buscando todas as Href (link dos PDF) da 1ª PARTE.
post_content = fox.find_element_by_class_name('post-content')
ul = post_content.find_element_by_tag_name('ul')
lis = ul.find_elements_by_tag_name('li')
lista_links = []
for li in lis:
    ancoras = li.find_elements_by_tag_name('a')
    print(ancoras)
    for ancora in ancoras:
        print(ancora.get_attribute('href'))
        link = ancora.get_attribute('href')
        lista_links.append(link)

#   Acessando cada link da 1ª parte e baixando o arquivo
#   Existem dois sites para baixar os arquivos, por isso a condicional.
for link in lista_links:
    fox.get(link)
    sleep(3)

#   1º Modelo e mais utilizado
    if 'www.minjus.gob.pe/wp-content' in link:
        fox.find_element_by_id('download').click()
        sleep(2)
        pyautogui.press(['enter'])
        print('deu bom')
#   2º Modelo
    else:
        print('esperando')
        cs_elemtent = fox.find_element_by_link_text('Descargar')
        link_href = cs_elemtent.get_attribute('href')
        fox.get(link_href)
        sleep(2)
        fox.find_element_by_id('download').click()
        sleep(3)
        pyautogui.press(['enter'])
        sleep(3)
    sleep(3)

print('fim da primeira parte')
