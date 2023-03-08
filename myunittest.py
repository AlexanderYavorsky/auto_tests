from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import unittest




class TestUnit(unittest.TestCase):
    
    def test_Unit(self):
        
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
        input.send_keys("Test")
        input2 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
        input2.send_keys("Test")
        input3 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
        input3.send_keys("Test3")
        input4 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your phone:']")
        input4.send_keys("Test4")
        input4 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your address:']")
        input4.send_keys("Test5")
        time.sleep(3)
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        #ждем загрузки страницы
        time.sleep(1)
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Your Test Fail")
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        #time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_Unit2(self):
        browser = webdriver.Chrome()
        link2 = "http://suninjuly.github.io/registration2.html"
        browser.get(link2)

        # Ваш код, который заполняет обязательные поля
        input = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your name']")
        input.send_keys("Test")
        #input2 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
        #input2.send_keys("Test")
        input3 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
        input3.send_keys("Test3")
        input4 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your phone']")
        input4.send_keys("Test4")
        input4 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your address:']")
        input4.send_keys("Test5")
        time.sleep(3)
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        # time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

        #ждем загрузки страницы
        time.sleep(1)

        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Your Test Fail")
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        #time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()
        
if __name__ == "__main__":
    unittest.main()
 
    
# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#assert "Congratulations! You have successfully registered!" == welcome_text



