from selenium.webdriver import Firefox
from urllib.parse import urlparse

# --------------- Função usadas no código ---------------


def preencher_formulario(nome, email, senha, telefone):
    """
    Preenchimento automatico do formulário
    """
    firefox.find_element_by_name('nome').send_keys(nome)
    firefox.find_element_by_name('email').send_keys(email)
    firefox.find_element_by_name('senha').send_keys(senha)
    firefox.find_element_by_name('telefone').send_keys(telefone)
    firefox.find_element_by_id('btn').click()


# --------------- Inicialização do Projeto  ---------------
firefox = Firefox()
firefox.get('http://selenium.dunossauro.live/exercicio_04.html')
firefox.implicitly_wait(3)
formulario_estruturado = {'nome': 'matheus',
                          'email': 'dtsquad@gmail.com',
                          'senha': 'q1w2e3',
                          'telefone': '912345678'}

# --------------- Preenchimento do formulário  ---------------
preencher_formulario(**formulario_estruturado)
url_query = urlparse(firefox.current_url).query.split('&')

# --------------- Tratamento  formulário  ---------------
tratamento_result = firefox.find_element_by_tag_name('textarea').text.replace('@', '%40')\
    . \
    replace(':', '=').replace('\'', '')

resultado_tratado = tratamento_result.replace(' ', '').replace('{', '').replace('}', '')\
    .split(',')

# --------------- Visualização e validação do resultado final ---------------
print(f'url {url_query[0:4]}')
print(f'resultado {resultado_tratado}')

assert resultado_tratado == url_query[0:4]

firefox.quit()
print('preenchimento do formulário e Validação através da url completa')
