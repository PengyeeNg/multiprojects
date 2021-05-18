from Setup.T4 import Base_Setup
from Actions.T4.main_page import MainpageActions
from Input_Data.T4.login_page import LoginData
from Elements.T4.main_page import MainpageElement
from Elements.T4.login_page import LogInElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

class LoginpageActions(Base_Setup.BSetup):

    def Login_to_Mainpage(self):
        MainpageActions.Access_to_Mainpage(self)
        # Login with registered username and password
        print("<li>" + "Click on Log In button" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(LogInElement.login_button).click()
        time.sleep(3)
        print("<li>" + "Insert Username: " + LoginData.username + "</li>" + "<br>")
        self.driver.find_element_by_id(LogInElement.username_field).send_keys(LoginData.username)
        print("<li>" + "Insert Password: " + LoginData.password + "</li>" + "<br>")
        self.driver.find_element_by_id(LogInElement.password_field).send_keys(LoginData.password)
        print("<li>" + "Click on Log in button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(LogInElement.confirm_login_button).click()
        # Wait the page loads
        time.sleep(2)
        # Wait the page loads
        wait_main_page = EC.element_to_be_clickable((By.CLASS_NAME, MainpageElement.announcement_modal_dialog_close_button))
        WebDriverWait(self.driver, 20).until(wait_main_page)
        # Close Announcement dialog box
        print("<li>" + "Close the Announcement modal dialog" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(MainpageElement.announcement_modal_dialog_close_button).click()
        self.driver.implicitly_wait(10)
        time.sleep(2)
        # Assert
        login_mainpage = self.driver.find_element_by_class_name(LogInElement.logout_button).is_displayed()
        self.assertTrue(login_mainpage, "User is not able to login to the account.")
