from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class KadrHotelsPage():

    def test_GoogleSearch(self):
        driver_chrome = webdriver.Chrome()
        self.driver = driver_chrome
        driver_chrome.maximize_window()
        driver_chrome.get('https://www.kadrtour.com/en/hotels')
 
        # Perform search operation
        elem = driver_chrome.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div/div[2]/a[2]")
        elem.click()
        time.sleep(1) 
 
    def tearDown(self):
        # Close the browser.
        self.driver.close()
        self.driver.quit()
 


case1 = KadrHotelsPage()
case1.test_GoogleSearch()
case1.tearDown()

