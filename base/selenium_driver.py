from selenium import webdriver


class SeleniumDriver:

    @staticmethod
    def driver_instance():
        driver = webdriver.Chrome('C:/webdrivers/chromedriver.exe')
        return driver
