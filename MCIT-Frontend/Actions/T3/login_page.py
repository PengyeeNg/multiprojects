from Setup.T3 import Base_Setup
from Actions.T3.main_page import MainpageActions
from Input_Data.T3.login_page import LoginData
from Elements.T3.main_page import MainpageElement
from Elements.T3.login_page import LogInElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class LoginpageActions(Base_Setup.BSetup):

    def Login_to_Mainpage(self):
        MainpageActions.Access_to_Mainpage(self)
        # Login with registered username and password
        print("<li>" + "Insert Username: " + LoginData.username + "</li>" + "<br>")
        self.driver.find_element_by_id(LogInElement.username_field).clear()
        self.driver.find_element_by_id(LogInElement.username_field).send_keys(LoginData.username)
        print("<li>" + "Insert Password: " + LoginData.password + "</li>" + "<br>")
        self.driver.find_element_by_id(LogInElement.password_field).clear()
        self.driver.find_element_by_id(LogInElement.password_field).send_keys(LoginData.password)
        print("<li>" + "Click on Log in button" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(LogInElement.login_button).click()
        # Wait the page loads
        wait_main_page = EC.presence_of_element_located((By.XPATH, LogInElement.account_name))
        WebDriverWait(self.driver, 20).until(wait_main_page)
        # Assert
        account_name = self.driver.find_element_by_xpath(LogInElement.account_name).text
        self.assertEqual(account_name, LoginData.username, "User is not able to login to the account.")

    def Assert_Access_to_Linkpage(self):
        # Wait page load
        wait_page_load = EC.presence_of_element_located((By.XPATH, LogInElement.link_page_title))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        page_loaded = self.driver.find_element_by_xpath(LogInElement.link_page_title).is_displayed()
        self.assertTrue(page_loaded, "User is not able to access to the page.")
