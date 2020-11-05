from appium import webdriver
import time


capabilities = {
    "deviceName": "android",
    "version": "9.0",
    'app': 'https://github.com/sozdai/behave-sample/raw/main/com.instagram.android.apk',
    'appActivity': 'com.instagram.mainactivity.LauncherActivity',
    'appPackage': 'com.instagram.android',
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
