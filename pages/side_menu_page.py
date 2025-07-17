from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class SideMenu(Page):
    SETTINGS_LINK = (By.CSS_SELECTOR, 'a[href="/settings"]')


    def click_settings(self, context):
        self.wait_for_element_click(*self.SETTINGS_LINK)

