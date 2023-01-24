from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

desired_caps = {
    "lt:options": {
        "w3c": True,
        "platformName": "android",
        "deviceName": "Pixel .*",
        "platformVersion": "10",
        "isRealMobile": True
    }
}


def startingTest():

    if os.environ.get("LT_USERNAME") is None:
        # Enter LT username here if environment variables have not been added
        username = "username"
    else:
        username = os.environ.get("LT_USERNAME")
    if os.environ.get("LT_ACCESS_KEY") is None:
        # Enter LT accesskey here if environment variables have not been added
        accesskey = "accesskey"
    else:
        accesskey = os.environ.get("LT_ACCESS_KEY")

    try:
        driver = webdriver.Remote(desired_capabilities=desired_caps, command_executor="https://" +
                                  username+":"+accesskey+"@mobile-hub.lambdatest.com/wd/hub")

        driver.get("https://www.playojo.com/#registration")
        # print(driver.page_source)
        time.sleep(10)
        # colorElement = WebDriverWait(driver, 30).until(
        #     EC.element_to_be_clickable((AppiumBy.ID, "firstName")))

        colorElement = driver.find_element(
            by=AppiumBy.XPATH, value="//input[contains(@name,'firstName')]")
        colorElement.click()
        colorElement.send_keys("Kaustubh")

        # colorElement = driver.find_element(
        #     by=AppiumBy.XPATH, value='/html/body/son-cookie-consent//div/div/div[2]/button')
        # colorElement.click()

        colorElement = driver.find_element(
            by=AppiumBy.XPATH, value="//input[contains(@id,'lastName')]")
        colorElement.click()
        colorElement.send_keys("LambdaTest")

        # LT-Kaustubh
        # reg_01 = self.driver.self.driver.find_element_by_id("firstName")
        # reg_01 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "firstName")
        # reg_01 = driver.find_element(By.ID, "firstName")
        # reg_01.click()
        # reg_01.send_keys("kaustubhd@lambdatest.com")

        # textElement = WebDriverWait(driver, 30).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "div > div > div.consent-bar-right > button")))
        # textElement.click()

        # toastElement = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
        #     (By.ID, "details")))
        # toastElement.click()

        # notification = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
        #     (By.ID, "timezone")))
        # notification.click()

        time.sleep(5)

        driver.quit()
    except Exception as e:
        print(e)
        driver.quit()


startingTest()
