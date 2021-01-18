import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

USERNAME = 'user@email.com'
PASSWORD = 'pass'

driver = webdriver.Chrome()
driver.get("https://app.pontomaisweb.com.br/#/acessar")


def ponto():
    usuario = driver.find_element_by_name('login')
    usuario.send_keys(USERNAME)

    senha = driver.find_element_by_name('password')
    senha.send_keys(PASSWORD)

    logar = driver.find_element_by_xpath("/html/body/ng-view/div/div/form/div/div[4]/div/div/div[3]/button")
    logar.click()
    time.sleep(20)
    
    registrar = driver.find_element_by_xpath('//*[@id="content-wrapper"]/div[2]/div/ng-view/div[2]/button')
    driver.execute_script("arguments[0].click();", registrar)
    
    driver.quit()

if __name__ == "__main__":
    ponto()