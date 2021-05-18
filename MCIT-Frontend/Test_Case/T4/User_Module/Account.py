import unittest
from Setup.T4 import Base_Setup
from Elements.T4.user_page import UserpageElement
from Actions.T4.login_page import LoginpageActions
from Actions.T4.user_page import UserActions
from Input_Data.T4.user_page import UserData
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class UserAccountModule(Base_Setup.BSetup):

    def test_TC_Account_01_Submit_Deposit(self):
        print("<b> Expected Results: Able to submit deposit. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        UserActions.Access_to_Account(self)
        print("<li>" + "Click on Deposit tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserpageElement.account_deposit_tab).click()
        time.sleep(1)
        print("<li>" + "Select Deposit Bank: Public Bank" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserpageElement.account_deposit_bank).click()
        print("<li>" + "Select Deposit Amount: 50" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserpageElement.account_deposit_amount).click()
        print("<li>" + "Click on Submit button" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserpageElement.account_deposit_submit_button).click()

    def test_TC_Account_02_Submit_Withdrawal(self):
        print("<b> Expected Results: Able to submit withdrawal. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        UserActions.Access_to_Account(self)
        print("<li>" + "Click on Withdrawal tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserpageElement.account_withdrawal_tab).click()
        time.sleep(1)
        print("<li>" + "Select Withdrawal Bank: Maybank : 27****8452" + "</li>" + "<br>")
        # Select transfer form
        select_withdrawal_bank = Select(self.driver.find_element_by_xpath(UserpageElement.account_withdrawal_bank))
        # select by visible text
        select_withdrawal_bank.select_by_visible_text('Maybank : 27****8452')
        print("<li>" + "Insert Withdrawal Amount: " + UserData.withdrawal_withdrawal_amount + "</li>" + "<br>")
        self.driver.find_element_by_id(UserpageElement.account_withdrawal_amount).send_keys(UserData.withdrawal_withdrawal_amount)
        print("<li>" + "Click on Submit button" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserpageElement.account_withdrawal_submit_button).click()

    def test_TC_Account_03_Perform_Transfer(self):
        print("<b> Expected Results: Able to perform transfer. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        UserActions.Access_to_Account(self)
        print("<li>" + "Click on Transfer tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserpageElement.account_transfer_tab).click()
        time.sleep(1)
        print("<li>" + "Select Transfer from: Main Wallet" + "</li>" + "<br>")
        # Select transfer form
        select_transfer_from = Select(self.driver.find_element_by_xpath(UserpageElement.account_transfer_from))
        # select by visible text
        select_transfer_from.select_by_visible_text('Main Wallet')
        print("<li>" + "Select Transfer to: Evolution Gaming" + "</li>" + "<br>")
        # Select transfer to
        select_transfer_to = Select(self.driver.find_element_by_xpath(UserpageElement.account_transfer_to))
        # select by visible text
        select_transfer_to.select_by_visible_text('Evolution Gaming')
        print("<li>" + "Insert Transfer Amount: " + UserData.account_transfer_amount + "</li>" + "<br>")
        self.driver.find_element_by_id(UserpageElement.account_transfer_amount_field).send_keys(UserData.account_transfer_amount)
        print("<li>" + "Click on Submit button" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserpageElement.account_transfer_submit_button).click()
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
        self.assertEqual(prompt_message, "success", "User is not able to perform transfer.")

    def test_TC_Account_04_View_Deposit_Record(self):
        print("<b> Expected Results: Able to view deposit record. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        UserActions.Access_to_Account(self)
        print("<li>" + "Click on Record tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserpageElement.account_record_tab).click()
        print("<li>" + "Click on Deposit Record tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserpageElement.account_rdeposit_tab).click()
        time.sleep(3)
        # Assert
        deposit_detail = self.driver.find_element_by_xpath(UserpageElement.account_deposit_details).text
        self.assertNotEqual(deposit_detail, "", "Report is not available.")

    def test_TC_Account_05_View_Withdrawal_Record(self):
        print("<b> Expected Results: Able to view withdrawal record. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        UserActions.Access_to_Account(self)
        print("<li>" + "Click on Record tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserpageElement.account_record_tab).click()
        print("<li>" + "Click on Withdrawal Record tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserpageElement.account_rwithdrawal_tab).click()
        time.sleep(3)
        # Assert
        withdrawal_detail = self.driver.find_element_by_xpath(UserpageElement.account_withdrawal_details).text
        self.assertNotEqual(withdrawal_detail, "", "Report is not available.")


if __name__ == '__main__':
    unittest.main()
