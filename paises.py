# Bibliotecas ultilizadas
from selenium import webdriver
from selenium.webdriver.common.by import By


def inicializar_url(url_site):
    """
    :param url_site: Url de cada seleção
    :return: ira entrar na Url de cada seleção e iniciar a função informacoes_paises()
    """
    firefox.get(url_site)


def informacoes_paises(div_xpath, parametro):
    """
    :param div_xpath: Tagname: Div e o seu XPATH
    :param parametro: Parametro P dentro da xpath_div
    :return:Retorna a dict_nome_pais com todas as informações para tratamento e ser mandada para o banco de dados
    """
    xpath_div = firefox.find_element(By.XPATH, div_xpath)
    parametros = xpath_div.find_elements(By.TAG_NAME, parametro)

    if len(parametros) == 9:
        """
        se a quantidades de parametros: P for igual  a 9:
            O codigo irá pegar as informaçoes de acordo com os xpaths abaixo e mostrar na tela
        """
        nome_pais = firefox.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div/div/p[1]')
        capital_pais = firefox.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div/div/p[2]')
        area_pais = firefox.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div/div/p[3]')
        populacao_pais = firefox.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div/div/p[4]')
        governo_pais = firefox.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div/div/p[5]')
        hino_nacional_pais = firefox.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div/div/p[6]')
        idiomas_pais = firefox.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div/div/p[7]')
        moeda_pais = firefox.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div/div/p[8]')

        print('***' * 10)
        print(len(parametros))
        print(nome_pais.text)
        print(capital_pais.text)
        print(area_pais.text)
        print(populacao_pais.text)
        print(governo_pais.text)
        print(hino_nacional_pais.text)
        print(idiomas_pais.text)
        print(moeda_pais.text)
        print('***' * 10)
        dict_nome_pais[nome_pais.text[7:]] = {capital_pais.text[10:], area_pais.text[7:], populacao_pais.text[12:],
                                              governo_pais.text[10:], hino_nacional_pais.text[16:],
                                              idiomas_pais.text[19:], moeda_pais.text[8:]}

    elif len(parametros) > 9:
        """
        se a quantidades de parametros: P for maior que 9:
            O codigo irá pegar as informaçoes de acordo com os xpaths abaixo e mostrar na tela
        """
        nome_pais = firefox.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div/div/p[1]')
        capital_pais = firefox.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div/div/p[2]')
        area_pais = firefox.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div/div/p[3]')
        populacao_pais = firefox.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div/div/p[4]')
        governo_pais = firefox.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div/div/p[5]')
        hino_nacional_pais = firefox.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div/div/p[7]')
        idiomas_pais = firefox.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div/div/p[8]')
        moeda_pais = firefox.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div/div/p[9]')

        print('***' * 10)
        print(len(parametros))
        print(nome_pais.text)
        print(capital_pais.text)
        print(area_pais.text)
        print(populacao_pais.text)
        print(governo_pais.text)
        print(hino_nacional_pais.text)
        print(idiomas_pais.text)
        print(moeda_pais.text)
        print('***' * 10)
        dict_nome_pais[nome_pais.text[7:]] = {capital_pais.text[10:], area_pais.text[7:], populacao_pais.text[12:],
                                              governo_pais.text[10:], hino_nacional_pais.text[16:],
                                              idiomas_pais.text[19:], moeda_pais.text[8:]}


#   Lista e dicionarios
dict_nome_pais = {}
links_paises = []

#   No site principal iremos pegar todos os links da lita de paises para a extração das informações
firefox = webdriver.Firefox()
inicializar_url('https://www.sport-histoire.fr/pt/Geografia/Paises_por_ordem_alfabetica.php')
tbody_tabela = firefox.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div[1]/div/table/tbody')
parametros_ancoras = tbody_tabela.find_elements(By.TAG_NAME, 'a')

for ancora in parametros_ancoras:
    # para cada link da tabela adicione este link na lista links_paises
    print(ancora.text, ancora.get_attribute('href'))
    print('**' * 15)
    links_paises.append(ancora.get_attribute('href'))

for link in links_paises:
    """
    -   Para cada link  em links_paises
    -   A função inicializar_url acessa o site do pais que tem as informações desejadas.
    -   A função informacoes_paises pega as informações da melhor forma
    """
    inicializar_url(link)
    informacoes_paises('/html/body/div/div[2]/div[2]/div/div', 'p')

#   FIM
firefox.quit()
print(dict_nome_pais)
