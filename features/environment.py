import configparser
import time

import allure
from selenium import webdriver

from features.pages.google_login_page import GoogleLoginPage


def before_all(context):
    # options = webdriver.ChromeOptions()
    # options.add_extension('idkfomapecgcmaciblgfnopkofdclmfg.crx')
    # options.add_argument("--enable-automation")
    # options.add_experimental_option("prefs", {"profile.default_content_settings.cookies": 1})

    # context.driver = webdriver.Chrome(options=options)
    
    capabilities = {
    "browserName": "chrome",
    "browserVersion": "86.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False
    }
}

    context.driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        desired_capabilities=capabilities)
    
    context.driver.implicitly_wait(20)
    parser = configparser.ConfigParser()
    parser.read("behave.ini")
    context.config = parser
    open_google_auth_page(context, parser.get("settings", "google_auth_url"))


def open_google_auth_page(context, url):
    time.sleep(0.5)  # wait for extension to be opened in new tab
    # context.driver.switch_to.window(context.driver.window_handles[0])
    context.driver.get(url)
    g_login_page = GoogleLoginPage(context.driver)
    g_login_page.login(context.config.get("user", "username"), context.config.get("user", "password"))


def after_step(context, step):
    if step.status == "failed":
        allure.attach(context.driver.get_screenshot_as_png(),
                      name="screenshot",
                      attachment_type=allure.attachment_type.PNG)


def after_all(context):
    context.driver.quit()
