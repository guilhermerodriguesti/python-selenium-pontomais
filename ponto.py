import time
import sys
import os
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys

# Credentials
load_dotenv('.env')

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

driver = webdriver.Chrome()
driver.get("https://app.pontomaisweb.com.br/#/acessar")

def ponto():
    driver.find_element_by_name('login').send_keys(username)
    driver.find_element_by_name('password').send_keys(password)

    logar = driver.find_element_by_xpath("/html/body/ng-view/div/div/form/div/div[4]/div/div/div[3]/button")
    logar.click()
    time.sleep(20)
    
    #registrar = driver.find_element_by_xpath('//*[@id="content-wrapper"]/div[2]/div/ng-view/div[2]/button')
    #driver.execute_script("arguments[0].click();", registrar)
    
    #driver.find_element_by_css_selector("a[ng-click='Registrar ponto']").click()
    #button = driver.find_element_by_class_name("text-center mt15 ng-scope")
    #button.click()
    
    driver.quit()

if __name__ == "__main__":
    ponto()