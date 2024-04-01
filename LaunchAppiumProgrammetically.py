import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

# Step 1 : Import Appium Service class
from appium.webdriver.appium_service import AppiumService

# Step 2 : Create object for Appium Service class
appium_service = AppiumService()

# Step 3 : Call Start method by using Appium Service class object
appium_service.start()

# Step 4 : Create "Desired Capabilities"

capabilities = {}
capabilities['platformName'] = 'Android'
capabilities['automationName'] = 'UiAutomator2'
capabilities['platformVersion'] = '11'
capabilities['deviceName'] = 'Medium_Phone_API_30'
# capabilities['app'] = ('/Users/Hari/Downloads/Android_Demo_App.apk')
capabilities['appPackage'] = 'com.code2lead.kwad'
capabilities['appActivity'] = 'com.code2lead.kwad.MainActivity'


capabilities_options = UiAutomator2Options().load_capabilities(capabilities)

# Step 5 : Create "Driver object"
driver = webdriver.Remote("http://127.0.0.1:4723",options=capabilities_options)

# Step 6 : "Click on the button using ID locator value"
ele_id = driver.find_element(AppiumBy.ID,"com.code2lead.kwad:id/Zoom")
ele_id.click()

# Step 7 : Wait for 2 seconds
time.sleep(2)

# Step 8 : Close the driver object
driver.quit()

# Step 9 : Call stop method by using Appium Service class object
appium_service.stop()