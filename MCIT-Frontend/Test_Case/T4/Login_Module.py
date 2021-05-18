import unittest
from Setup.T4 import Base_Setup
from Actions.T4.login_page import LoginpageActions
from Elements.T4.login_page import LogInElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class LoginModule(Base_Setup.BSetup):

    def test_TC_Login_01_Valid_Login(self):
        print("<b> Expected Results: Login to Main Page with valid username and password. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)

    def test_TC_Login_02_Logout(self):
        print("<b> Expected Results: Login from the account. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        print("<li>" + "Click on Log Out button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(LogInElement.logout_button).click()
        # Wait page load
        wait_page_load = EC.presence_of_element_located((By.XPATH, LogInElement.login_button))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        logout_from_main = self.driver.find_element_by_xpath(LogInElement.login_button).is_displayed()
        self.assertTrue(logout_from_main, "User is not able to logout from the account.")




if __name__ == '__main__':
    unittest.main()
