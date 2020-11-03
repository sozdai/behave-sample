import time

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class BananarepublicGapComPage(BasePage):
    BASE_URL = "https://bananarepublic.gap.com/browse/category.do?cid=1032801"
    BUTTON_CLOSE_SIGN_UP_MODAL = (By.XPATH, "//button[@aria-label='close email sign up modal']")
    CARD_FIRST_PRODUCT = (By.XPATH, "(//div[@class = 'product-card'])[1]//div[@class='product-card__name']")
    NAME_PRODUCT = (By.CLASS_NAME, "product-title__text")
    SIZE_FIRST_AVAILABLE = (By.XPATH, "(//div[@class='dimensions-group']//input[@aria-disabled='false'])[1]/..")
    URL_CHECKOUT = "https://secure-bananarepublic.gap.com/shopping-bag"
    BUTTON_ADD_BAG = (By.CLASS_NAME, "add-to-bag")
    BUTTON_CHECKOUT = (By.ID, "checkoutButton")

    def _verify_page(self):
        self.driver.get(self.BASE_URL)
        self.on_this_page(self.CARD_FIRST_PRODUCT)

    def add_to_basket(self):
        product_name = self.get_text(self.CARD_FIRST_PRODUCT)
        print(f'Product: {product_name}')
        try:
            self.click_on(self.BUTTON_CLOSE_SIGN_UP_MODAL)
            time.sleep(0.5)
        except Exception:
            pass
        self.click_on(self.CARD_FIRST_PRODUCT)
        self.get_element(self.NAME_PRODUCT)
        time.sleep(1)
        self.click_on(self.SIZE_FIRST_AVAILABLE)
        self.click_on(self.BUTTON_ADD_BAG)
        self.get_element(self.BUTTON_CHECKOUT)
        return product_name

    def open_checkout_page(self):
        self.click_on(self.BUTTON_CHECKOUT)
