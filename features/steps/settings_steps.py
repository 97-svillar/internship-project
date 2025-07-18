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
    context.app.settings_page.edit_name(name = "User Test")
    context.app.settings_page.click_save_changes()
    context.app.settings_page.edit_email(email = "testuser@careerist.com")
    # context.app.settings_page.fill_edit_profile_fields(
    #     name="User Test",
    #     email="testuser@careerist.com"
    # )

    context.app.settings_page.click_save_changes()


@then("Check the right information is present in the input fields")
def check_input_values(context):
    assert context.app.settings_page.get_input_value("name") == "User Test"
    assert context.app.settings_page.get_input_value("email") == "testuser@careerist.com"


@then("Check the “Close” and “Save Changes” buttons are available and clickable")
def check_buttons_clickable(context):
    assert context.app.settings_page.is_element_clickable(*context.app.settings_page.CLOSE_BTN
    ), "Close button is not clickable"
    assert context.app.settings_page.is_element_clickable(*context.app.settings_page.SAVE_CHANGES_BTN
    ), "Save Changes button is not clickable"