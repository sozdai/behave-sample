from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class GoogleLoginPage(BasePage):
    FIELD_USERNAME = (By.ID, "identifierId")
    FIELD_PASSWORD = (By.NAME, "password")
    BUTTON_NEXT = (By.ID, "identifierNext")
    BUTTON_SUBMIT = (By.ID, "passwordNext")
    BUTTON_ALLOW = (By.ID, "submit_approve_access")
    TITLE_GOOGLE = (By.ID, "googlebar")
    BUTTON_SIGN_IN_WITH_GOOGLE = (By.XPATH, "//*[text()='Sign In with Google']")
    LOGO = (By.XPATH, '//*[@id="root"]/div/header/div/p/img')

    def _verify_page(self):
        self.on_this_page(self.FIELD_USERNAME)

    def login(self, username, password):
        self.type_in(self.FIELD_USERNAME, username)
        self.click_on(self.BUTTON_NEXT)
        self.type_in(self.FIELD_PASSWORD, password)
        self.click_on(self.BUTTON_SUBMIT)

        try:
            self.get_element(self.TITLE_GOOGLE)
        except:
            self.click_on(self.BUTTON_ALLOW)
            self.get_element(self.TITLE_GOOGLE)

        # self.driver.switch_to.window(self.driver.window_handles[-1])
        # self.click_on(self.BUTTON_SIGN_IN_WITH_GOOGLE)
        # self.get_element(self.LOGO)
