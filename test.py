from selenium import webdriver
import time
import os

# capabilities = {
#     "deviceName": "android",
#     "version": "9.0",
#     'app': 'https://github.com/sozdai/behave-sample/raw/main/com.instagram.android.apk',
#     'appActivity': 'com.instagram.mainactivity.LauncherActivity',
#     'appPackage': 'com.instagram.android',
#     "selenoid:options": {
#         "enableVNC": True,
#         "enableVideo": False
#     }
# }
#
# driver = webdriver.Remote(
#     command_executor="http://localhost:4444/wd/hub",
#     desired_capabilities=capabilities)
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
d = webdriver.Chrome(chrome_options=chrome_options)

driver = webdriver.Chrome()

time.sleep(10)
driver.get("https://www.google.com")

driver.quit()
