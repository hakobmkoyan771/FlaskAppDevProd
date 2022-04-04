from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import os

def get_path(path):
    os.chdir(path)
    sys.path.insert(0,path)


get_path("/home/erida-employee/Desktop/ssh/page_class/Kadr_POM_Model/Page")
get_path("/home/erida-employee/Desktop/ssh/page_class/Kadr_POM_Model")
from  kadr_hotels_page import KadrHotelsPage
from config import get_page_link



class KadrPageLocators:
    locator_kadr_click_button = (By.CSS_SELECTOR, ".page > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(4)")
    locator_kadr_navigation_bar = (By.XPATH, "/html/body/header/nav/div/div[2]/ul/li[3]/a")

class TestKadrHotelsPage(KadrHotelsPage):

    def enter_word(self):
        search_field = self.find_element(KadrPageLocators.locator_kadr_navigation_bar)
        search_field.click()
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(KadrPageLocators.locator_kadr_click_button,time=2).click()
