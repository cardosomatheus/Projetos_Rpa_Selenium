from selenium.webdriver import Firefox
from time import sleep
import pyautogui


fox = Firefox()
fox.get('https://www.minjus.gob.pe/resoluciones-ttaip/')
sleep(1.5)
#    Buscando todas as Href (link dos PDF)
post_content = fox.find_element_by_class_name('post-content')
ul = post_content.find_element_by_tag_name('ul')
lis = ul.find_elements_by_tag_name('li')
for li in lis:
    ancoras = li.find_elements_by_tag_name('a')
    print(ancoras)
    for ancora in ancoras:
        print(ancora.get_attribute('href'))
        link = ancora.get_attribute('href')
        fox.get(link)
        sleep(2)
        fox.find_element_by_id('download').click()
        sleep(2)
        pyautogui.press(['enter'])




