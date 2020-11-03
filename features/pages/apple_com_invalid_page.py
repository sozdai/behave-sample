from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class AppleComInvalidPage(BasePage):
    BASE_URL = "https://www.apple.com/shop/buy-mac/mac-mini/3.6ghz-quad-core-processor-256gb#"
    CHECKOUT_URL = "https://www.apple.com/shop"
    BUTTON_ADD_BASSKET = (By.NAME, "add-to-cart")
    BUTTON_PROCEED = (By.NAME, "proceed")
    NAME_PRODUCT = (By.CLASS_NAME, "localnav-title")

    def _verify_page(self):
        self.driver.get(self.BASE_URL)
        self.on_this_page(self.BUTTON_ADD_BASSKET)

    def add_to_basket(self):
        product = self.get_text(self.NAME_PRODUCT)
        self.click_on(self.BUTTON_ADD_BASSKET)
        self.get_element(self.BUTTON_PROCEED)
        print(f'Product: {product}')
        return product

    def open_checkout_page(self):
        self.driver.get(self.CHECKOUT_URL)
