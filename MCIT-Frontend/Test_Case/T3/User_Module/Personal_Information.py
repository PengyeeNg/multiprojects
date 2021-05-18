import unittest
from Actions.T3.user_page import UserpageActions
from Setup.T3 import Base_Setup
from Elements.T3.user_page import UserElement
from Input_Data.T3.user_page import UserData
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class PersonalInformationModule(Base_Setup.BSetup):

    def test_TC_PersonalInformation_01_Navigate_to_PersonalInformationPage(self):
        print("<b> Expected Results: Able to access to personal information page. </b>" + "<br>")
        UserpageActions.Access_to_Personal_Information(self)

    def test_TC_PersonalInformation_02_Modify_Personal_Information(self):
        print("<b> Expected Results: Able to modify personal information. </b>" + "<br>")
        UserpageActions.Access_to_Personal_Information(self)
        print("<li>" + "Click on Modify button" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserElement.personal_info_modify).click()
        print("<li>" + "Modify Actual Name Field: " + UserData.actual_name + "</li>" + "<br>")
        self.driver.find_element_by_id(UserElement.personal_info_actual_name).clear()
        time.sleep(1)
        print("<li>" + "Click on Confirm button" + "</li>" + "<br>")
        self.driver.find_element_by_id(UserElement.personal_info_actual_name).send_keys(UserData.actual_name)
        # Assert
        wait_button_clickable = EC.element_to_be_clickable((By.CLASS_NAME, UserElement.personal_info_confirm_button))
        WebDriverWait(self.driver, 10).until(wait_button_clickable)
        self.driver.find_element_by_class_name(UserElement.personal_info_confirm_button).click()

    def test_TC_PersonalInformation_03_Change_Password(self):
        print("<b> Expected Results: Able to change password. </b>" + "<br>")
        UserpageActions.Access_to_Personal_Information(self)
        print("<li>" + "Click on Change Password button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(UserElement.personal_info_change_password).click()
        print("<li>" + "Insert old password: " + UserData.old_password + "</li>" + "<br>")
        self.driver.find_element_by_id(UserElement.personal_info_old_password).send_keys(UserData.old_password)
        print("<li>" + "Insert new password: " + UserData.new_password + "</li>" + "<br>")
        self.driver.find_element_by_id(UserElement.personal_info_new_password).send_keys(UserData.new_password)
        print("<li>" + "Insert confirm password: " + UserData.confirm_password + "</li>" + "<br>")
        self.driver.find_element_by_id(UserElement.personal_info_confirm_password).send_keys(UserData.confirm_password)
        print("<li>" + "Click on Next Step button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(UserElement.personal_info_next_step).click()
        # Assert
        wait_password_modified = EC.presence_of_element_located((By.XPATH, UserElement.personal_info_password_modified))
        WebDriverWait(self.driver, 10).until(wait_password_modified)
        password_modified = self.driver.find_element_by_xpath(UserElement.personal_info_password_modified).is_displayed()
        self.assertTrue(password_modified, "Password is not modified successfully.")


if __name__ == '__main__':
    unittest.main()
