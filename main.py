from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
import time

#Инициалия драйвера Chrome
driver = webdriver.Chrome()
#Обращаемся к нужному сайту
driver.get("https://pskov.samodelkin-mag.ru/")

#Ищем поисковое поле
search_box = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[3]/ul/li[1]/form/input')
#Отправляем запрос для поиска запчастей для марки Индезит
search_box.send_keys("индезит")

search_box2 = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[3]/ul/li[1]/form/button')
search_box2.submit()
#Проверяем получили ли какой-нибудь результат
assert "No results found." not in driver.page_source

# Инициализация пустого списка для хранения цитат
parts = []
while True:
    # Поиск всех цитат на странице с помощью xpath
    part_elements = driver.find_elements(By.XPATH, '//form[@class="ms2_form"]')
    # Извлечение текста каждой цитаты
    for part_element in part_elements:
        spare_part_title = part_element.find_element(By.XPATH, './/span[@class="item-title wide"]').text
        spare_part_article = part_element.find_element(By.XPATH, './/span[@class="data-article"]').text
        spare_part_price = part_element.find_element(By.XPATH, './/span[@class="data-price"]').text
        parts.append({"spare_part_title": spare_part_title, "spare_part_article": spare_part_article, "spare_part_price": spare_part_price})
    # Проверка наличия следующей кнопки
    next_button = driver.find_elements(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div[1]/div[7]/div/ul/li[8]/a')

    if not next_button:
        break
    # Нажатие следующей кнопки
    next_button[0].click()
    # Ожидание загрузки страницы
    time.sleep(1)

with open("spare_parts.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["spare_part_title", "spare_part_article", "spare_part_price"])
    writer.writeheader()
    writer.writerows(parts)

driver.close()