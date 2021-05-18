import unittest
from Setup.T4 import Base_Setup
from Elements.T4.register_page import RegisterpageElement
from Elements.T4.login_page import LogInElement
from Elements.T4.main_page import MainpageElement
from Actions.T4.main_page import MainpageActions
from Input_Data.T4.register_page import RegisterData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

class RegisterModule(Base_Setup.BSetup):

    def test_TC_Register_01_Register_New_User(self):
        print("<b> Expected Results: Able to login with registered username and password. </b>" + "<br>")
        MainpageActions.Access_to_Register_Page(self)
        print("<li>" + "Insert Username: " + RegisterData.new_username + "</li>" + "<br>")
        self.driver.find_element_by_id(RegisterpageElement.username_field).send_keys(RegisterData.new_username)
        print("<li>" + "Insert Mobile Phone: " + RegisterData.phone_number + "</li>" + "<br>")
        self.driver.find_element_by_id(RegisterpageElement.mobile_phone_field).send_keys(RegisterData.phone_number)
        print("<li>" + "Insert Email: " + RegisterData.email + "</li>" + "<br>")
        self.driver.find_element_by_id(RegisterpageElement.email_field).send_keys(RegisterData.email)
        print("<li>" + "Insert Password: " + RegisterData.password + "</li>" + "<br>")
        self.driver.find_element_by_id(RegisterpageElement.password_field).send_keys(RegisterData.password)
        print("<li>" + "Insert Confirm Password: " + RegisterData.confirm_password + "</li>" + "<br>")
        self.driver.find_element_by_id(RegisterpageElement.confirm_password_field).send_keys(RegisterData.confirm_password)
        print("<li>" + "Insert Invitation Code: " + RegisterData.invitation_code + "</li>" + "<br>")
        self.driver.find_element_by_id(RegisterpageElement.invitation_code_field).send_keys(RegisterData.invitation_code)
        print("<li>" + "Click on Create Account button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(RegisterpageElement.create_acc_button).click()
        # Wait till alert is present
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        # Switch the control to the Alert window
        registration_prompt = self.driver.switch_to.alert
        # Retrieve the message on the Alert window
        # prompt_message = registration_prompt.text
        # print("Alert shows following message: " + prompt_message + "<br>")
        # Click on the OK button (Accept)
        print("<li>" + "Click on OK button" + "</li>" + "<br>")
        registration_prompt.accept()
        time.sleep(2)
        print("<li>" + "Insert Username: " + RegisterData.new_username + "</li>" + "<br>")
        self.driver.find_element_by_id(LogInElement.username_field).send_keys(RegisterData.new_username)
        print("<li>" + "Insert Password: " + RegisterData.password + "</li>" + "<br>")
        self.driver.find_element_by_id(LogInElement.password_field).send_keys(RegisterData.password)
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


if __name__ == '__main__':
    unittest.main()
