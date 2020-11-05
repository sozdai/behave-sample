from selenium import webdriver
import time


capabilities = {
    "browserName": "android",
    "version": "9.0",
    'app': 'https://github.com/sozdai/behave-sample/raw/main/org.wikipedia.com.apk',
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False
    }
}

driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    desired_capabilities=capabilities)


time.sleep(10)
time.sleep(10)

driver.quit()
