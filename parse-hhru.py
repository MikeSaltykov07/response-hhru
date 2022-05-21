#%%
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import config


url = 'https://hh.ru/account/login?backurl=%2F&customDomain=1'
driver = webdriver.Chrome(executable_path="../chromedriver")
try:
    driver.get(url= url)
    time.sleep(2)
    driver.find_element(by=By.XPATH, value="//button[contains(@class, 'bloko-link_pseudo') and @data-qa= 'expand-login-by-password']").click()
    time.sleep(2)
    editor = driver.find_element(by=By.XPATH, value="//input[contains(@data-qa, 'login-input-username')]")
    editor.send_keys(config.email)
    editor = driver.find_element(by=By.XPATH, value="//input[contains(@data-qa, 'login-input-password')]")
    editor.send_keys(config.password)
    time.sleep(2)
    driver.find_element(by=By.XPATH, value="//button[contains(@class, 'bloko-button_kind-primary') and @data-qa='account-login-submit']").click()
    time.sleep(15)
    driver.find_element(by=By.XPATH, value="//*[@data-qa='search-button']").click()
    time.sleep(5)
    driver.refresh()
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    try:
        while True:
            print("Начало откликов")
            try: 
                while True:
                    try:
                        driver.find_element(by=By.XPATH, value="//*[span='Откликнуться']").click()
                        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                        time.sleep(5)
                    except:
                        driver.refresh()
                        time.sleep(25)
                        print("Что-то не так")
                        driver.find_element(by=By.XPATH, value="//*[span='Откликнуться']").click()
                        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            except: 
                print("Завершение откликов на этой странице")
            driver.find_element(by=By.XPATH, value="//*[@class='bloko-button' and @data-qa='pager-next']").click()
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            print("Новая страница")
            time.sleep(15)
    except:
        print("Страницы закончились")
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()