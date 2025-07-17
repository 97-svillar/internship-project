from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

@when("Click on the Edit profile option")
def click_on_the_edit_profile(context):
    context.app.settings_page.click_edit_profile()

@then("Enter some test information in the input fields")
def enter_test_info(context):
    context.app.settings_page.fill_edit_profile_fields(
        name="User Test",
        email="testuser@careerist.com"
    )
    context.app.settings_page.click_save_changes()
    sleep(8)

@then("Check the right information is present in the input fields")
def check_input_values(context):
    name_value = context.app.settings_page.get_input_value("name")
    email_value = context.app.settings_page.get_input_value("email")
    print("DEBUG: Name field contains:", repr(name_value))
    print("DEBUG: Email field contains:", repr(email_value))
    assert name_value == "User Test"
    assert email_value == "testuser@careerist.com"
    # assert context.app.settings_page.get_input_value("name") == "User Test"
    # assert context.app.settings_page.get_input_value("email") == "testuser@careerist.com"