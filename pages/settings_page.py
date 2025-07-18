from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Settings(Page):
    EDIT_PROFILE_LINK = (By.CSS_SELECTOR, 'a[href="/profile-edit"]')
    YOUR_NAME_INPUT = (By.ID, 'Fullname')
    EMAIL_INPUT = (By.ID, 'Email-2')
    SAVE_CHANGES_BTN = (By.CSS_SELECTOR, 'div[wized="saveButtonProfile"]')
    CLOSE_BTN = (By.CSS_SELECTOR, 'a[class*="close-button"]')

    def click_edit_profile(self):
        self.wait_for_element_click(*self.EDIT_PROFILE_LINK)

    def click_save_changes(self):
        self.wait_for_element_click(*self.SAVE_CHANGES_BTN)

    def click_close(self):
        self.wait_for_element_click(*self.CLOSE_BTN)

    def edit_name(self, name, *locator):
        self.input_text(name, *self.YOUR_NAME_INPUT)

    def edit_email(self, email, *locator):
        self.input_text(email,*self.EMAIL_INPUT)

    def fill_edit_profile_fields(self, name, email):
        self.input_text(name,*self.YOUR_NAME_INPUT)
        self.input_text(email,*self.EMAIL_INPUT)
        self.click_save_changes()

    def get_input_value(self, field):
        if field in ["name", "fullname"]:
            locator = self.YOUR_NAME_INPUT
        elif field == "email":
            locator = self.EMAIL_INPUT
        else:
            raise ValueError("Unknown field")

        element = self.find_element(*locator)
        return element.get_attribute("value")

    def is_element_clickable(self, *locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator)
            )
            return element.is_displayed()
        except:
            return False