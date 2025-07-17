from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class SignUp(Page):
    LOGIN_LINK = (By.CSS_SELECTOR, 'div[wized="signinButtonSignup"]')


    def open_sign_up_page(self):
        self.driver.get('https://soft.reelly.io/sign-up')


    def click_login_link(self):
        self.click(*self.LOGIN_LINK)