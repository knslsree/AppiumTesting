import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Step 2 : Create object for Appium Service class
appium_service = AppiumService()

# Step 3 : Call Start method by using Appium Service class object
appium_service.start()


capabilities = {
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'platformVersion': '11',
    'deviceName': 'Medium_Phone_API_30',
    'appPackage': 'com.code2lead.kwad',
    'appActivity': 'com.code2lead.kwad.MainActivity'
}

capabilities_options = UiAutomator2Options().load_capabilities(capabilities)

driver = webdriver.Remote("http://127.0.0.1:4723",options=capabilities_options)

try:
    ele_index = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().index(6)"))
    )

    ele_index.click()
    # Step 7 : Wait for 2 seconds
    time.sleep(2)

finally:
    # Close the driver object
    driver.quit()

    # Call stop method by using Appium Service class object
    appium_service.stop()
