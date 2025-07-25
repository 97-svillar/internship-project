from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

@when("Click on the settings option")
def click_settings(context):
    context.app.side_menu_page.click_settings(context)
    sleep(5)
