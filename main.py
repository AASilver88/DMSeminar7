from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

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