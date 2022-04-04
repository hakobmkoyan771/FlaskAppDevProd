from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sys
import os

def get_path(path):
    os.chdir(path)
    sys.path.insert(0,path)


get_path("/home/erida-employee/Desktop/ssh/page_class/Kadr_POM_Model/Page")
get_path("/home/erida-employee/Desktop/ssh/page_class/Kadr_POM_Model")
from kadr_hotels_email_subscribe import KadrHotelsEmailSubscribe
from config import get_page_link



class KadrHotelsEmailSubscribeLocators:
    locator_kadr_send_keys_email_subscribe = (By.XPATH, '//*[@id="subscibe_mail"]')
    locator_clik_button_send_emils = (By.XPATH, '//*[@id="btnSendEmail"]')

class TestKadrHotelsEmailSubscribe(KadrHotelsEmailSubscribe):

    def send_emil_address(self):
        send_field = self.find_element(KadrHotelsEmailSubscribeLocators.locator_kadr_send_keys_email_subscribe)
        send_field.send_keys('testtamara@gmail.com')


    def clik_button_send_emils(self):
        self.find_element(KadrHotelsEmailSubscribeLocators.locator_clik_button_send_emils,time=2).click()
