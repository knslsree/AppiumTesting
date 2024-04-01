import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

capabilities = {}
capabilities['platformName'] = 'Android'
capabilities['automationName'] = 'UiAutomator2'
capabilities['platformVersion'] = '11'
capabilities['deviceName'] = 'Medium_Phone_API_30'
capabilities['appPackage'] = 'com.android.chrome'
capabilities['appActivity'] = 'com.google.android.apps.chrome.Main'

driver = webdriver.Remote("http://127.0.0.1:4723",capabilities)

ele_index= driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"uiselector.index(6)")
ele_index.click()
# Step 7 : Wait for 2 seconds
time.sleep(2)

# Step 8 : Close the driver object
driver.quit()

# Step 9 : Call stop method by using Appium Service class object
appium_service.stop()