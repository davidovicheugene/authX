from selenium import webdriver
import time
import requests
import os


options = webdriver.ChromeOptions()

driver = webdriver.Chrome(
    executable_path="/Users/mac/code/authX/chromedriver",
    options=options,
)


def authvk():
    pass


def authyandex():
    pass


def authgmail():
    pass


def authnotion():
    pass


def authgithub():
    pass


def main():
    try:
        pass
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

if __name__ == "__main__":
    main()