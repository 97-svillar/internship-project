
from pages.base_page import Page
from pages.sign_up_page import SignUp
from pages.sign_in_page import SignIn
from pages.side_menu_page import SideMenu
from pages.settings_page import Settings

class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.sign_in_page = SignIn(driver)
        self.sign_up_page = SignUp(driver)
        self.side_menu_page = SideMenu(driver)
        self.settings_page = Settings(driver)
