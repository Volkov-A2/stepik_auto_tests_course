import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"


def registation(link):
    driver = webdriver.Chrome()
    driver.get(link)
    first_name = driver.find_element(By.XPATH, "//input[contains(@placeholder, 'first')]")
    first_name.send_keys("Ivan")
    last_name = driver.find_element(By.XPATH, "//input[contains(@placeholder, 'last')]")
    last_name.send_keys("Petrov")
    email = driver.find_element(By.XPATH, "//input[contains(@placeholder, 'email')]")
    email.send_keys("Smolensk@uk.ru")
    phone = driver.find_element(By.XPATH, "//input[contains(@placeholder, 'phone')]")
    phone.send_keys("89996588989")
    address = driver.find_element(By.XPATH, "//input[contains(@placeholder, 'addres')]")
    address.send_keys("Samara")
    button = driver.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()
    expected_result = "Congratulations! You have successfully registered!"
    actual_result = driver.find_element(By.XPATH, "//h1").text
    assert (expected_result, actual_result, "Not expected")


def test_registation1():
    registation(link1)


def test_registation2():
    registation(link2)


if __name__ == "__main__":
    unittest.main()