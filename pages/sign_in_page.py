from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class SignIn(Page):
    LOGIN_LINK = (By.CSS_SELECTOR, 'div[wized="signinButtonSignup"]')
    EMAIL = (By.ID, "email-2")
    PASSWORD = (By.ID, "field")
    LOGIN_BTN = (By.CSS_SELECTOR, "a[wized='loginButton']")
    ERROR_MESSAGE = (By.ID, "password--ErrorMessage")

    def verify_sign_in_page(self):
        self.verify_partial_url('/login')

    def open_sign_in_page(self):
        self.driver.get('https://soft.reelly.io/sign-in')

    def click_login_link(self):
        self.click(*self.LOGIN_LINK)

    def verify_error_message(self):
        self.find_element(*self.ERROR_MESSAGE)

    def click_login_btn(self):
        self.click(*self.LOGIN_BTN)

    def login(self, email, password):
        self.input_text(email, *self.EMAIL)
        self.input_text(password, *self.PASSWORD)
        self.click(*self.LOGIN_BTN)

