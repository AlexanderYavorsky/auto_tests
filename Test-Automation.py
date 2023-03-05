from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5) # Задержка для дальнейшего всплывающего окна в конце с "ок"
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
    #Ищем элемент, на странице, пока не станет 100 
    price = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")

    )
    button = browser.find_element(By.ID, "book")
    button.click()
    
    # Captha
    captha = browser.find_element(By.ID, "input_value")
    x_element = captha.text
    x = calc(x_element)
    # Put capcha at input
    input = browser.find_element(By.ID, "answer")
    input.send_keys(x)
    # Find and click on the button
    submit = browser.find_element(By.CSS_SELECTOR, "[type=submit]")
    submit.click()
    # Нажимаем ок, на всплывающем окне
    confirm = browser.switch_to.alert
    confirm.accept()

finally:
  time.sleep(5)
  browser.quit()