"""
Before run this code download chromedriver:
https://sites.google.com/a/chromium.org/chromedriver/

Then put the executable into current directory. Check `executable_path` in below
"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


if __name__ == "__main__":
    chrome = webdriver.Chrome(executable_path='./chromedriver')
    chrome.get("https://www.google.com")
    element = WebDriverWait(chrome, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='q']")))
    element.click()
    element.send_keys('site:gainanov.pro Web Automation: Selenium WebDriver and Python')
    element.send_keys(Keys.RETURN)
    sleep(10)  # sleep 10s before quit
    chrome.quit()