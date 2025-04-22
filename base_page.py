from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
