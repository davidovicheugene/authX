from selenium import webdriver
import time
import requests
import os
import json
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()

driver = webdriver.Chrome(
    executable_path="/Users/mac/code/authX/chromedriver",
    options=options,
)

with open('data.json', 'r') as file:
    datajson = json.load(file)

with open('accounts.json', 'r') as file:
    accountjson = json.load(file)

def setdata(source, account, login_field_id, pass_field_id, btn_class, flogin_btn_xpath='clear'):
    if source == 'gmail':
        login_input = driver.find_element(By.ID,login_field_id)
    else:
        login_input = driver.find_element(By.ID,login_field_id)
    login_input.send_keys(datajson[source][account]['login'])
    # if source == 'gmail':
    #     flogin_btn = driver.find_element(By.XPATH,flogin_btn_xpath)
    #     flogin_btn.click()
    pass_input = driver.find_element(By.ID,pass_field_id)
    pass_input.send_keys(datajson[source][account]['pass'])
    login_btn = driver.find_element(By.CLASS_NAME, btn_class)
    login_btn.click()
    
def loadpage(page):
    url = page
    driver.get(url=url)

def authvk(account):
    loadpage("https://vk.com/")
    setdata("vk.com", account, "index_email", "index_pass", "index_login_button")

def authyandex(account):
    loadpage("")
    setdata("vk.com", account, "index_email", "index_pass", "index_login_button")
    time.sleep(10)


def authgmail(account):
    url = "https://accounts.google.com/AccountChooser?service=mail&continue=https://mail.google.com/mail/"
    driver.get(url=url)
    setdata("gmail", account, "identifierId", "index_pass", "index_login_button",
        flogin_btn="/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button"
    )
    time.sleep(10)


# def authnotion(account):
#     loadpage("")
#     setdata("vk.com", account, "index_email", "index_pass", "index_login_button")
#     time.sleep(10)


def authgithub(account):
    loadpage("https://github.com/login")
    setdata("github", account, "login_field", "password", "js-sign-in-button")
    


def main():
    try:
        authvk(accountjson['vk'])
        authgithub(accountjson['github'])
        # authgmail(accountjson['gmail'])

        time.sleep(100)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

if __name__ == "__main__":
    main()