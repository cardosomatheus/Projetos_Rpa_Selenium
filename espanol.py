from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import pyautogui
import os
import shutil
"""
Esse script tem como objetivo capturar todas as urls do site que contem um pdf e baixar os arquivos.
Para os 3 Tipos de links existe uma forma de baixar o arquivo.
(1) - Ao iniciar ná URl, basta apenas encontrar o ID= dowload e baixar o arquivo.
(2) - Encontrar o Elemento Link_text= 'descargar' e clicar, voce será direcionado para o pdf e executar o mesmo processo 
 da opção nº1
(3) - Colocar todos as URLs na lista = 'lista_links_download' e repetir o processo da 1º Opção
"""
lista_links_download = []
links_lista_removidos = ['https://www.minjus.gob.pe/tribunal-de-transparencia-y-acceso-a-la-informacion-publica/',
                         'https://www.minjus.gob.pe/ttaip-organizacion/',
                         'https://www.minjus.gob.pe/salas-ttaip/',
                         'https://www.minjus.gob.pe/ttaip-normatividad/',
                         'https://www.minjus.gob.pe/resoluciones-ttaip/',
                         'https://www.minjus.gob.pe/procedimiento-de-acceso-a-la-informacion-publica/',
                         'https://www.minjus.gob.pe/procedimiento-de-apelacion-contra-sancion-por-infraccion-a-las-normas-de-transparencia-y-acceso/',
                         'https://www.minjus.gob.pe/ttaip-secretaria-tecnica/',
                         'https://www.minjus.gob.pe/ttaip-peventos-recientes/',
                         'https://www.minjus.gob.pe/ttaip-material-informativo/']
pasta_download = r'C:/Users/mathe/Downloads'
download_final = r'C:\Users\mathe\download_final'


def links_site(elementoweb_classe, elementoweb_tagname):
    """
    :param elementoweb_classe: Um parametro classe será passado nesse local
    :param elementoweb_tagname: Um parametro tagname será passado e se tranformara em uma lista de parametros.
    O parametro que virou lista, é um parametro que contem links de pdf
    :return:
    """
    post_content = fox.find_element_by_class_name(elementoweb_classe)
    ancoras = post_content.find_elements_by_tag_name(elementoweb_tagname)
    for ancora in ancoras:
        print(ancora.text, ancora.get_attribute('href'))
        link_href = ancora.get_attribute('href')
        print('*' * 10)
        if link_href not in links_lista_removidos:
            lista_links_download.append(link_href)


def click_download(elementoweb_id):
    """
    :param elementoweb_id: Um parametro ID será passado nesse local para baixar o PDF
    :return: Retorna o pdf baixado
    """
    localizador = (By.ID, elementoweb_id)
    wdw.until(presence_of_element_located(localizador))
    fox.find_element(*localizador).click()
    sleep(5)
    pyautogui.press(['enter'])


def descargar_download(elementoweb_linktext):
    """
    :param elementoweb_linktext: Paeametro que contem o local para baixar oarquivo através do link_text
    :return: Após localizar o link_text, a função "click_download()" é iniciada.
    """
    descargar = fox.find_element_by_link_text(elementoweb_linktext)
    link_href = descargar.get_attribute('href')
    fox.get(link_href)
    click_download('download')


#   Inicialização do Projeto
options = webdriver.FirefoxOptions()
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
options.set_preference("browser.download.dir", pasta_download)
fox = webdriver.Firefox(options=options)
fox.get('https://www.minjus.gob.pe/resoluciones-ttaip/')
wdw = WebDriverWait(fox, 10)
alerta = Alert(fox)

# Encontrando todas as urls  e colocando da lista "lista_links_download"
links_site(elementoweb_classe='post-content', elementoweb_tagname='a')

arq_pasta_final = os.listdir(download_final)

for link in lista_links_download:
    arq_pasta_download = os.listdir(pasta_download)
    fox.get(link)
    wdw = WebDriverWait(fox, 10)

    #   (1) - Opção
    if 'www.minjus.gob.pe/wp-content' in link:
        nome_arq = link[53:]
        print(nome_arq)
        if nome_arq not in arq_pasta_download:
            if nome_arq not in arq_pasta_final:
                click_download(elementoweb_id='download')
                print(f'O download do PDF deu certo')
        else:
            continue

    #   (2) - Opção
    elif 'https://www.gob.pe/institucion/minjus/' in link:
        descargar_download(elementoweb_linktext='Descargar')

    #   (3) - Opção
    elif 'https://www.minjus.gob.pe/resoluciones' in link:
        links_site(elementoweb_classe='post-content', elementoweb_tagname='a')

    for arq in arq_pasta_download:
        if arq not in arq_pasta_final:
            origem = f'{pasta_download}/{arq}'
            destino = f'{download_final}/{arq}'
            shutil.move(origem, destino)
            sleep(2)
            print(f'o arquivo: {arq} foi movido com sucesso para a pasta: download_final')
        else:
            continue

print('projeto finalizado com sucesso')
