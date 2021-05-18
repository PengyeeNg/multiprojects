import unittest
from selenium.webdriver import ActionChains
from Setup.T4 import Base_Setup
from Elements.T4.user_page import UserpageElement
from Actions.T4.login_page import LoginpageActions
from Actions.T4.user_page import UserActions
from Input_Data.T4.user_page import UserData
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class UserProfileModule(Base_Setup.BSetup):

    def test_TC_Profile_01_Edit_Profile(self):
        print("<b> Expected Results: Able to edit profile. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        UserActions.Access_to_Profile(self)
        print("<li>" + "Edit username: " + UserData.username + "</li>" + "<br>")
        self.driver.find_element_by_id(UserpageElement.account_username_field).clear()
        time.sleep(1)
        self.driver.find_element_by_id(UserpageElement.account_username_field).send_keys(UserData.username)
        print("<li>" + "Click on Save button" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserpageElement.account_save_button).click()
        # Wait till alert is present
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        # Switch the control to the Alert window
        registration_prompt = self.driver.switch_to.alert
        # Retrieve the message on the Alert window
        prompt_message = registration_prompt.text
        print("Alert shows following message: " + prompt_message + "<br>")
        # Click on the OK button (Accept)
        print("<li>" + "Click on OK button" + "</li>" + "<br>")
        registration_prompt.accept()
        time.sleep(1)
        # Assert
        self.assertEqual(prompt_message, "success", "User is not able to edit profile.")


if __name__ == '__main__':
    unittest.main()
