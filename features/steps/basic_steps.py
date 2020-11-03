from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from features.pages.apple_com_invalid_page import AppleComInvalidPage
from features.pages.apple_com_page import AppleComPage
from features.pages.bananarepublic_gap_com_page import BananarepublicGapComPage
from features.pages.base_page import BasePage


@when('I click button with text "{text}"')
def step_impl(context, text):
    element = (By.XPATH, "//button[text() = '{}']".format(text))
    WebDriverWait(context.driver, 10).until(
        ec.element_to_be_clickable(element), "Unable to click element").click()


@then('I see element with text "{text}"')
def step_impl(context, text):
    element = (By.TAG_NAME, "body")
    WebDriverWait(context.driver, 10).until(
        ec.text_to_be_present_in_element(element, text), "Unable to find text: {}".format(text))


@given("I open url '{url}")
def step_impl(context, url):
    context.driver.get(url)


@given("I open page '{website}'")
def step_impl(context, website):
    if website == "apple.com":
        context.page = AppleComPage(context.driver)
    elif website == "apple.com.invalid":
        context.page = AppleComInvalidPage(context.driver)
    elif website == "bananarepublic.gap.com":
        context.page = BananarepublicGapComPage(context.driver)


@when("I add to bag")
def step_impl(context):
    context.product = context.page.add_to_basket()


@when("I open checkout page")
def step_impl(context):
    context.page.open_checkout_page()


@when('I verify extension has product')
def step_impl(context):
    extension_widget_page = BasePage(context.driver)
    extension_widget_page.verify_product(context.product)
