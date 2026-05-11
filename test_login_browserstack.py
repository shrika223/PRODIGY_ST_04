from selenium import webdriver
from selenium.webdriver.common.by import By
import os

USERNAME = os.getenv("BROWSERSTACK_USERNAME")
ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")

browsers = [
    {"browserName": "Chrome", "os": "Windows", "osVersion": "11"},
    {"browserName": "Firefox", "os": "Windows", "osVersion": "11"},
    {"browserName": "Safari", "os": "OS X", "osVersion": "Monterey"},
    {"browserName": "Edge", "os": "Windows", "osVersion": "11"}
]

for browser in browsers:
    desired_cap = {
        'browserName': browser["browserName"],
        'bstack:options': {
            'os': browser["os"],
            'osVersion': browser["osVersion"],
            'local': 'false',
            'seleniumVersion': '4.0.0',
            'buildName': 'Task04-CrossBrowser',
            'sessionName': f'Login Test - {browser["browserName"]}'
        }
    }

    driver = webdriver.Remote(
        command_executor=f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub",
        desired_capabilities=desired_cap
    )

    try:
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        assert "inventory" in driver.current_url
        print(f"{browser['browserName']} login successful!")
    except Exception as e:
        print(f"{browser['browserName']} test failed: {e}")
    finally:
        driver.quit()
