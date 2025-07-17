from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


@when("login to the page with {email} and {password}")
def log_in(context, email, password):
    context.app.base_page.wait_for_element_click(By.CSS_SELECTOR, 'div[wized="signinButtonSignup"]')
    context.app.sign_in_page.login(email, password)
    sleep(5)
