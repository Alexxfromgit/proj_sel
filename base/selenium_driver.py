from selenium import webdriver


class SeleniumDriver:

    def driver_instance(self):
        driver = webdriver.Chrome('C:/chromedriver.exe')
        return driver
