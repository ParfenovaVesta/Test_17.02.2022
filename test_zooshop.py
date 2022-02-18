from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "https://zooshoptest.ru/"

try:
    # подключаем драйвер для браузера
    browser = webdriver.Chrome()
    # сообщаем тесту ожидать появление каждого элемента до пяти секунд
    browser.implicitly_wait(5)
    # открываем ссылку в браузере
    browser.get(link)

    # ищем и кликаем нопку "обратная связь"
    browser.find_element(By.CLASS_NAME, "shop_menuone_top_right_svyaz").click()
    
    # очищаем и заполняем поля формы обратной связи
    browser.find_element(By.XPATH, "/html/body/div[3]//input[@name='name']").clear()
    browser.find_element(By.XPATH, "/html/body/div[3]//input[@name='name']").send_keys("Ivan")

    browser.find_element(By.XPATH, "/html/body/div[3]//input[@name='lastname']").clear()
    browser.find_element(By.XPATH, "/html/body/div[3]//input[@name='lastname']").send_keys("Ivanov")

    browser.find_element(By.XPATH, "/html/body/div[3]//input[@name='phone']").clear()
    browser.find_element(By.XPATH, "/html/body/div[3]//input[@name='phone']").send_keys("+799999999")

    browser.find_element(By.XPATH, "/html/body/div[3]//textarea[@class='b24-form-control']").clear()
    browser.find_element(By.XPATH, "/html/body/div[3]//textarea[@class='b24-form-control']").send_keys("test")

    # находим и кликаем кнопку отправить
    browser.find_element(By.XPATH, "/html/body/div[3]//div[@class='b24-form-btn-block']/button[@type='submit']").click()

    # находим элемент, содержащий текст, подтверждающий отправку сообщения
    welcome_text_elt = browser.find_element(By.XPATH, "//div[3]/div[2]/div[1]/div[2]//*[contains(text(),'Спасибо, ваше сообщение отправлено')]")

    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text


    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert welcome_text == 'Спасибо, ваше сообщение отправлено.', "Send Error"



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла