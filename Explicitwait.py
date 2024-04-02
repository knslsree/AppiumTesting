import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
# Step 1 : Import Appium Service class
from appium.webdriver.appium_service import AppiumService
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementNotSelectableException;
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
driver = webdriver.Remote("http://127.0.0.1:4723", options=capabilities_options)


# Step 7 : Wait for 2 seconds

wait = WebDriverWait(driver, 25, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                         NoSuchElementException])

ele = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue"))
ele.click()

ele = wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText"))
ele.send_keys("Skill2Lead")

time.sleep(4)
driver.quit()

appium_service.stop()