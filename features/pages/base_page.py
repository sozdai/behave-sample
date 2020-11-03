from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    DIALOG = (By.ID, "reward-dialog")
    FIRST_PRODUCT = (By.XPATH, "//div[@id='reward-container-items']/div[1]/span")

    def __init__(self, driver):
        self.driver = driver
        self._verify_page()

    def _verify_page(self):
        pass

    def verify_product(self, text):
        self.on_this_page(self.DIALOG)
        self.driver.find_element_by_xpath(
            f"//div[@id='reward-container-items']/div[1]/span[contains(text(), '{text}')]")

    def get_element(self, locator):
        expected_condition = ec.presence_of_element_located(locator)
        return WebDriverWait(self.driver, 10).until(expected_condition, message=f"Unable to locate element {locator}")

    def get_element_with_text(self, locator, text):
        expected_condition = ec.text_to_be_present_in_element_value(locator, text)
        return WebDriverWait(self.driver, 10).until(expected_condition,
                                                    message=f"Text '{text}' not found in element {locator}")

    def on_this_page(self, *args):
        for locator in args:
            self.get_element(locator)

    def click_on(self, locator):
        expected_condition = ec.element_to_be_clickable(locator)
        WebDriverWait(self.driver, 10).until(expected_condition, message="Unable to click element").click()

    def type_in(self, locator, text):
        self.get_element(locator).clear()
        self.get_element(locator).send_keys(text)

    def get_text(self, locator):
        return self.get_element(locator).text

    def verify_text_in_extension(self, text):
        pass
