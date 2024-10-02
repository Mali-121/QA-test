from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

class LoginTest(unittest.TestCase):
    def setUp(self):
        # Specify the full path to ChromeDriver using the Service object
        chrome_service = Service(r'C:\Users\user\Downloads\chromedriver-win64\chromedriver.exe')
        self.driver = webdriver.Chrome(service=chrome_service)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # Implicit wait

    def test_login_logout(self):
        driver = self.driver
        wait = WebDriverWait(driver, 30)  # Explicit wait of 30 seconds

        # Navigate to the login page
        driver.get('https://voiceoverping.net/login')

        # Wait for the email input field to be present and interact with it
        email_field = wait.until(EC.presence_of_element_located((By.ID, 'inputEmail')))
        email_field.send_keys('1@qatest.vp')

        # Wait for the password field to be present and interact with it
        password_field = wait.until(EC.presence_of_element_located((By.ID, 'inputPassword')))
        password_field.send_keys('1234')

        # Wait for the Sign in button and click it
        sign_in_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
        sign_in_button.click()

        # Wait and verify if redirected to the dashboard
        time.sleep(3)
        self.assertIn('Channels', driver.page_source, 'User was not redirected to the dashboard')

        # Log out from the dashboard by clicking the 'LOGOUT' link (Using PARTIAL LINK TEXT)
        logout_link = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'LOGOUT')))
        logout_link.click()

        # Wait and verify redirection back to the login page
        time.sleep(3)
        self.assertIn('Sign in', driver.page_source, 'User was not redirected back to the login page after logging out')

    def tearDown(self):
        # Close the browser after the test
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
