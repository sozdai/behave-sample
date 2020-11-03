import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_extension('idkfomapecgcmaciblgfnopkofdclmfg.crx')
options.add_argument("--enable-automation")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(20)

time.sleep(5)
driver.switch_to.window(driver.window_handles[0])
driver.get("https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow")

driver.find_element_by_id("identifierId").send_keys("shevchenkosofiya61@gmail.com")
driver.find_element_by_id("identifierNext").click()

password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
password.send_keys("Ab123456!")

element = driver.find_element_by_id('passwordNext')
driver.execute_script("arguments[0].click();", element)

try:
    driver.find_element_by_id("googlebar")
except:
    driver.find_element_by_id("submit_approve_access").click()
    driver.find_element_by_id("googlebar")

driver.switch_to.window(driver.window_handles[-1])
driver.find_element_by_xpath("//*[text()='Sign In with Google']").click()


time.sleep(10)

driver.get("https://www.apple.com/shop/buy-mac/mac-mini/3.6ghz-quad-core-processor-256gb#")

driver.find_element_by_name("add-to-cart").click()
driver.find_element_by_name("proceed").click()


driver.find_element_by_xpath("//div[@id='reward-dialog']")
driver.find_element_by_xpath("//div[@id='reward-container-items'][0]/div/span[contains(text(), 'Mac mini')]")

driver.quit()