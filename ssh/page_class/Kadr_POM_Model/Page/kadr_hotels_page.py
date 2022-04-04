from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



class KadrHotelsPage():

    def __init__(self, driver, page_link):
        self.driver = driver
        self.page_link = page_link

    def find_element(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                          message=f"Can't find element by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.page_link)

    def quit_driver(self):
        return self.driver.close()

