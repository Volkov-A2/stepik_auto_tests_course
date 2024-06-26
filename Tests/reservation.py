from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")


price = WebDriverWait(browser, 10).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
button = browser.find_element(By.ID, "book")
button.click()

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)
input = browser.find_element(By.ID, "answer")
input.send_keys(y)

button_submit = browser.find_element(By.ID, "solve")
button_submit.click()
allert = browser.switch_to.alert
print(allert.text)
allert.accept()


