from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


@given("Open Reelly sign-up page")
def open_sign_up_page(context):
    context.app.sign_up_page.open_sign_up_page()

