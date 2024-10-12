from time import sleep

from googletrans import Translator
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

# url = 'https://store.steampowered.com/news/app/2074920/view/4619091776604954828'

print('Название(полное): Steam News Translate\n'
      'Версия: 1.2.11024\n'
      'Автор программы: Джон\n'
      'Написать в Telegram: @jon007god\n'
      'Ссылка на Discord сообщество: https://discord.gg/vvv777\n')

url = str(input('Ссылка Steam новости: '))
options = Options()
options.add_argument('-headless')
browser = webdriver.Firefox(options=options)
print('Ожидайте...')
browser.get(url)
browser.implicitly_wait(5)
num_time = .2

title_news = browser.find_element(By.CLASS_NAME, 'TqEPC9bhvVpZ1rb3Z8Mbd').text.strip()
desc_text = browser.find_element(By.CLASS_NAME, 'EventDetailsBody').text.strip()

if len(desc_text) > 12000:
    print(f'олее 12к символов (сейчас:{len(desc_text)}). Перевод может быть не выполнен из-за лимита сервиса.')
    num_time = 5
elif len(desc_text) > 5500:
    num_time = 1.6
elif len(desc_text) < 800:
    num_time = 1
elif len(desc_text) < 500:
    num_time = .4

desc_text.replace('<br>', '\n').strip()

sleep(num_time)
# ПЕРЕВОД ДАННЫХ
translator = Translator()
title_trans = translator.translate(text=title_news, dest='ru', src='en')
sleep(num_time)
desc_trans = translator.translate(text=desc_text, dest='ru', src='en')
print('Начинаем записывать данные....')
sleep(num_time)

f = open('RU.txt', 'w+', encoding='utf-8')
f.write(f'{title_trans}\n'
        f'{desc_trans}')
f.close()
print(f'Файл RU.txt перевода успешно создан')
sleep(.8)

f = open('EN.txt', 'w+', encoding='utf-8')
f.write(f'{title_news}\n'
        f'{desc_text}')
f.close()
print(f'Файл EX.txt оригинала успешно создан')
browser.quit()
