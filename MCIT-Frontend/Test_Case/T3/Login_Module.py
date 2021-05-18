import unittest
from selenium.webdriver import ActionChains
from Setup.T3 import Base_Setup
from Actions.T3.login_page import LoginpageActions
from Elements.T3.login_page import LogInElement
from Elements.T3.main_page import MainpageElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class LoginModule(Base_Setup.BSetup):

    def TC_Login_01_Valid_Login(self):
        print("<b> Expected Results: Login to Main Page with valid username and password. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)

    def TC_Login_02_Logout(self):
        print("<b> Expected Results: Login from the account. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        print("<li>" + "Click on Log Out button" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(LogInElement.logout_button).click()
        print("<li>" + "Click on Confirm button" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(LogInElement.logout_confirm_button).click()
        # Wait page load
        wait_page_load = EC.presence_of_element_located((By.CLASS_NAME, MainpageElement.announcement_modal_dialog_close_button))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        logout_from_main = self.driver.find_element_by_class_name(MainpageElement.announcement_modal_dialog_close_button).is_displayed()
        self.assertTrue(logout_from_main, "User is not able to logout from the account.")

    def TC_Login_03_Access_to_Announcement(self):
        print("<b> Expected Results: Able to access to announcement page. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        print("<li>" + "Click on Announcement" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(LogInElement.notification_link).click()
        # Assert
        LoginpageActions.Assert_Access_to_Linkpage(self)

    def TC_Login_04_Access_to_Member_Center(self):
        print("<b> Expected Results: Able to access to member center page. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        print("<li>" + "Click on Member Center" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(LogInElement.member_center_link).click()
        # Assert
        LoginpageActions.Assert_Access_to_Linkpage(self)

    def TC_Login_05_Access_to_Online_Deposit(self):
        print("<b> Expected Results: Able to access to online deposit page. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        print("<li>" + "Click on Online Deposit" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(LogInElement.online_deposit_link).click()
        # Assert
        LoginpageActions.Assert_Access_to_Linkpage(self)

    def TC_Login_06_Access_to_Online_Withdrawal(self):
        print("<b> Expected Results: Able to access to online withdrawal page. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        print("<li>" + "Click on Online Withdrawal" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(LogInElement.online_withdrawal_link).click()
        # Assert
        LoginpageActions.Assert_Access_to_Linkpage(self)

    def TC_Login_07_Access_to_Transaction_Record(self):
        print("<b> Expected Results: Able to access to transaction record page. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        print("<li>" + "Click on Transaction Record" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(LogInElement.transaction_record_link).click()
        # Assert
        LoginpageActions.Assert_Access_to_Linkpage(self)

    def TC_Login_08_Access_to_Betting_Record(self):
        print("<b> Expected Results: Able to access to betting record page. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        print("<li>" + "Click on Betting Record" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(LogInElement.betting_record_link).click()
        # Assert
        LoginpageActions.Assert_Access_to_Linkpage(self)

    def test_TC_Login_09_Access_to_Member_Agent(self):
        print("<b> Expected Results: Able to access to member agent page. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        print("<li>" + "Click on Member Agent" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(LogInElement.member_agent_link).click()
        # Assert
        LoginpageActions.Assert_Access_to_Linkpage(self)


if __name__ == '__main__':
    unittest.main()
