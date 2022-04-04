# -*- encoding: utf-8 -*-
#!/usr/bin/env python

#import chromedriver_autoinstaller
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import time
import os.path
from os import path
import os
import shutil
#from shutil import make_archive
import smtplib
#import email
#from email.message import EmailMessage
#from email.mime.multipart import MIMEMultipart
#from email.mime.base import MIMEBase
#from email.mime.text import MIMEText
#from email.utils import COMMASPACE, formatdate
#from email import encoders
#import chromedriver_autoinstaller


#chromedriver_autoinstaller.install()
#driver = webdriver.Chrome("C:\\Users\\комп\\Desktop\\selenium_works\\chromedriver.exe")
#driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe", service_args=["--verbose", "--log-path=D:\\qc1.log"])

driver = webdriver.FirefoxProfile()
driver.get("http://tata.am/")

    
    

def crate_folder():
    path = "$HOME/Desktop/python/Tata"
    os.mkdir(path) 


output_url = [] 

def output():
  
    html_list = driver.find_element_by_xpath("/html/body/header/nav/div[2]/div/div/ul/li[3]/ul")
    items = html_list.find_elements_by_tag_name("a")
    for item in items:
        out = item.get_attribute("href")
        if out == None:
            continue 
        output_url.append(out)
    output_url.remove("http://tata.am/#")

output_content = []
result = {}

def content():
    for url in output_url:
    
        driver.get(url)
        time.sleep(10) 
        content_section = driver.find_element_by_xpath("/html/body/section/div/div/div/div/div/div[2]")
        time.sleep(5)
        content = content_section.find_elements_by_tag_name("p")
        for con in content:
            output_content.append(con.text)


def write_content():    
    name = ""
    for v in range(0, len(output_content)):
        if v%2 == 0:
            name = output_content[v]
            f = open('C:\\Users\\комп\\Desktop\\python\\Tata\\{}.txt'.format(output_content[v]), mode = 'x', encoding = 'utf-8')
        else:
            f = open('C:\\Users\\комп\\Desktop\\python\\Tata\\{}.txt'.format(name), mode = 'a+', encoding = 'utf-8')
            f.write(' >>> ' + str(output_content[v]))
            f.close()
          
        
def create_zip():
    parent_dir_zip = "$HOME/Desktop/python/Tata"
    shutil.make_archive("Tata", "zip",parent_dir_zip)


#send email
# def send_email():
    # fromaddr = 'tamarapapikyan9@gmail.com'
    # toaddrs  = 'tamarapapikyan21.96@gmail.com'


    # msg = MIMEMultipart()
    # msg['From'] = fromaddr
    # msg['To'] = toaddrs
    # msg['Subject'] = "Test"
    # body = "Test mail"
    # msg.attach(MIMEText(body, 'plain'))
    # filename = "Tata.zip"
    # attachment = open(r"C:\\Users\\комп\\Desktop\\python\\Tata.zip", "rb")
    # part = MIMEBase('application', 'octet-stream')
    # part.set_payload((attachment).read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    # msg.attach(part)


    # server = smtplib.SMTP('smtp.gmail.com', 587)
    # server.starttls()
    # server.login(fromaddr, "**********")
    # text = msg.as_string()
    # server.sendmail(fromaddr, toaddrs, text)
    # server.quit()

def main():

    crate_folder()
    output()
    content()
    write_content()
    #create_zip()
    #send_email()

main()
driver.quit()





























