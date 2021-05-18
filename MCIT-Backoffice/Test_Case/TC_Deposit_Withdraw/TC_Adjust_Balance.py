import unittest
import SetUp.Base_SetUp
from Actions.deposit_withdraw_page import Adjust_Balance_Actions
from Elements.deposit_withdraw_page import Adjust_Balance_Element
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class Adjust_Balance(SetUp.Base_SetUp.BSetUp):

    def test_TC_Adjust_Balance_01_Confirm_Deposit(self):
        Adjust_Balance_Actions.Navigate_Adjust_Balance(self)
        print("<li>" + "Click on Yes icon" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Adjust_Balance_Element.deposite_yes_button).click()
        # Wait till the dialog displayed
        wait_deposit_confirmation = EC.presence_of_element_located((By.CLASS_NAME, Adjust_Balance_Element.deposite_confirmation_ok_button))
        WebDriverWait(self.driver, 10).until(wait_deposit_confirmation)
        # Assert
        deposit_dialog_box = self.driver.find_element_by_class_name(Adjust_Balance_Element.deposite_confirmation_ok_button).is_displayed()
        self.assertTrue(deposit_dialog_box, "User is not able to confirm deposit.")
        print("Expected Results: Deposit Confirmation dialog box popped out." + "<br>")

    def test_TC_Adjust_Balance_02_Navigate_Back_From_Adjust_Balance(self):
        Adjust_Balance_Actions.Navigate_Adjust_Balance(self)
        print("<li>" + "Click on Member List Link" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Adjust_Balance_Element.member_list_navigation_link).click()
        # Assert
        member_list_page = self.driver.title
        self.assertEqual(member_list_page, "Member List", "User is not able to access to Member List Page.")
        print("Expected Results: Navigated to Member List page." + "<br>")


if __name__ == '__main__':
    unittest.main()
