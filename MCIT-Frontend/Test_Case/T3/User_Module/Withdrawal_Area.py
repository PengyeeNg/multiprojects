import unittest
from Actions.T3.user_page import UserpageActions
from Setup.T3 import Base_Setup
from Elements.T3.user_page import UserElement
from Input_Data.T3.user_page import UserData
from selenium.webdriver.support.ui import Select
import time

class WithdrawalAreaModule(Base_Setup.BSetup):

    def test_TC_WithdrawalArea_01_Navigate_to_WithdrawalAreaPage(self):
        print("<b> Expected Results: Able to access to withdrawal area page. </b>" + "<br>")
        UserpageActions.Access_to_Withdrawal_Area(self)

    def test_TC_WithdrawalArea_02_Withdraw_Balance(self):
        print("<b> Expected Results: Able to perform Withdrawal. </b>" + "<br>")
        UserpageActions.Access_to_Withdrawal_Area(self)
        print("<li>" + "Select Bank: Maybank" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserElement.withdrawal_area_select_bank).click()
        print("<li>" + "Insert Withdrawal Amount: " + UserData.withdrawal_area_withdrawal_amount + "</li>" + "<br>")
        self.driver.find_element_by_id(UserElement.withdrawal_area_amount_field).send_keys(UserData.withdrawal_area_withdrawal_amount)
        print("<li>" + "Click on Next Step button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(UserElement.withdrawal_area_next_step).click()

    def test_TC_WithdrawalArea_03_Add_Bank(self):
        print("<b> Expected Results: Able to add bank. </b>" + "<br>")
        UserpageActions.Access_to_Withdrawal_Area(self)
        time.sleep(2)
        print("<li>" + "Click on Add Bank button" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserElement.withdrawal_area_add_bank).click()
        print("<li>" + "Insert Account Name: " + UserData.acc_name + "</li>" + "<br>")
        self.driver.find_element_by_id(UserElement.withdrawal_area_account_name_field).send_keys(UserData.acc_name)
        print("<li>" + "Insert Account Number: " + UserData.acc_number + "</li>" + "<br>")
        self.driver.find_element_by_id(UserElement.withdrawal_area_acc_number_field).send_keys(UserData.acc_number)
        print("<li>" + "Select Bank: Public Bank" + "</li>" + "<br>")
        select_bank = Select(self.driver.find_element_by_id(UserElement.withdrawal_area_select_bank_drop_down))
        # select by visible text
        select_bank.select_by_visible_text('Public Bank')
        print("<li>" + "Click on Submit button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(UserElement.withdrawal_area_submit_button).click()

    def test_TC_WithdrawalArea_04_Reset_Add_Bank(self):
        print("<b> Expected Results: Able to reset add bank details. </b>" + "<br>")
        UserpageActions.Access_to_Withdrawal_Area(self)
        time.sleep(2)
        print("<li>" + "Click on Add Bank button" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserElement.withdrawal_area_add_bank).click()
        print("<li>" + "Insert Account Name: " + UserData.acc_name + "</li>" + "<br>")
        self.driver.find_element_by_id(UserElement.withdrawal_area_account_name_field).send_keys(UserData.acc_name)
        print("<li>" + "Insert Account Number: " + UserData.acc_number + "</li>" + "<br>")
        self.driver.find_element_by_id(UserElement.withdrawal_area_acc_number_field).send_keys(UserData.acc_number)
        print("<li>" + "Select Bank: Public Bank" + "</li>" + "<br>")
        select_bank = Select(self.driver.find_element_by_id(UserElement.withdrawal_area_select_bank_drop_down))
        # select by visible text
        select_bank.select_by_visible_text('Public Bank')
        print("<li>" + "Click on Reset button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(UserElement.withdrawal_area_reset_button).click()
        time.sleep(2)
        # Assert
        # acc_name = self.driver.find_element_by_id(UserElement.withdrawal_area_account_name_field).text
        # acc_number = self.driver.find_element_by_id(UserElement.withdrawal_area_acc_number_field).text
        # acc_bank = self.driver.find_element_by_id(UserElement.withdrawal_area_select_bank_drop_down).text
        # self.assertEqual(acc_name, "", "Account Name is not reset.")
        # self.assertEqual(acc_number, "", "Account Number is not reset.")
        # self.assertEqual(acc_bank, "", "Account Bank is not reset.")


if __name__ == '__main__':
    unittest.main()
