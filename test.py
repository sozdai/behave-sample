from selenium import webdriver
import time
import urllib

urllib.urlretrieve ("https://dw.uptodown.com/dwn/8c_0a6VR8EofzKPe6qvRMtzyAaECK4AHZOC7ZJw1djMYNqzTlmr6qNNKDVy66wx15CV2meHMNtvJ_CxQUKOEi9QrsLrC497Anh6Ye8LbupS_mkrD_iUw-lpVD3LghYXk/43enMmaHRurwOYGt_SMXOeULadzrFMx4tQQ_-3xuUuxwkSJ3jFP4Kx2tfUX3m0CS7D522bpnyaxBoOfS51gznHtKNs0w7eCzmqZhOEt5Bx72uWBL6ottns7Aotyw3ezd/LiiQjy0mrTdypm26ePpKQDRbdFuSijql_1QCTDRMOzlcxJ2eS_c8Y2pi3HYTBVJFkAuV0kG_7udB_o5lkG_jfAedxA-0sK6KNWV8jUmvb4Q=/", "app.apk")

capabilities = {
    "browserName": "android",
    "version": "9.0",
    'app': 'app.apk',
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
