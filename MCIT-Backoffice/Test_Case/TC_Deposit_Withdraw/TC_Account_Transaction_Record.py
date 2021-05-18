import unittest
import SetUp.Base_SetUp
from Actions.deposit_withdraw_page import Account_Transaction_Record_Actions
from Actions.deposit_withdraw_page import Deposit_Withdraw_Actions
from Elements.deposit_withdraw_page import Account_Transaction_Record_Element
from Elements.deposit_withdraw_page import Deposit_Withdraw_Element
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Input_Data.deposit_withdraw_page import Deposit_Withdraw_Data


class Account_Transaction_Record(SetUp.Base_SetUp.BSetUp):

    def test_TC_Account_Transaction_Record_01_Export_Account_Turnover(self):
        Account_Transaction_Record_Actions.Navigate_Account_Transaction_Record(self)
        print("<li>" + "Click on Export button (Blue)" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Account_Transaction_Record_Element.export_blue_button).click()
        # Wait till dialog box displayed
        wait_export_confirmation = EC.presence_of_element_located((By.CLASS_NAME, Account_Transaction_Record_Element.export_blue_confirmation_ok_button))
        WebDriverWait(self.driver, 10).until(wait_export_confirmation)
        # Assert
        export_confirmation_dialog_box = self.driver.find_element_by_class_name(Account_Transaction_Record_Element.export_blue_confirmation_ok_button).is_displayed()
        self.assertTrue(export_confirmation_dialog_box, "User is not able to export account turnover.")
        print("Expected Results: Export Confirmation dialog box pooped out." + "<br>")

    def test_TC_Account_Transaction_Record_02_Search_Account_Turnover(self):
        Account_Transaction_Record_Actions.Navigate_Account_Transaction_Record(self)
        print("<li>" + "Insert Member Name" + "</li>" + "<br>")
        self.driver.find_element_by_id(Account_Transaction_Record_Element.member_name_filter_field).send_keys(Deposit_Withdraw_Data.member_name_filter)
        print("<li>" + "Click on Search button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Deposit_Withdraw_Element.filter_search_button).click()
        # Assert
        Deposit_Withdraw_Actions.Assert_Search_results(self)

    def test_TC_Account_Transaction_Record_03_Select_Columns(self):
        Account_Transaction_Record_Actions.Navigate_Account_Transaction_Record(self)
        print("<li>" + "Click on Select column button" + "</li>" + "<br>")
        self.driver.find_element_by_id(Account_Transaction_Record_Element.select_column_button).click()
        # Wait till dropdown expanded
        wait_dropdown_expanded = EC.presence_of_element_located((By.CLASS_NAME, Deposit_Withdraw_Element.select_columns))
        WebDriverWait(self.driver, 10).until(wait_dropdown_expanded)
        print("<li>" + "Click on 'Select Columns'" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Deposit_Withdraw_Element.select_columns).click()
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Account Turnover", "Page breaks after clicking 'Select Columns'.")
        print("Expected Results: Page does not break after clicking 'Select Column'." + "<br>")

    def test_TC_Account_Transaction_Record_04_Export_Account_Turnover(self):
        Account_Transaction_Record_Actions.Navigate_Account_Transaction_Record(self)
        print("<li>" + "Click on Export button" + "</li>" + "<br>")
        self.driver.find_element_by_id(Account_Transaction_Record_Element.export_button).click()
        # Wait till dropdown expanded
        wait_dropdown_expanded = EC.presence_of_element_located((By.CLASS_NAME, Deposit_Withdraw_Element.html_button))
        WebDriverWait(self.driver, 10).until(wait_dropdown_expanded)
        print("<li>" + "Click on 'HTML'" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Deposit_Withdraw_Element.html_button).click()
        # Assert
        export_dialog_box = self.driver.find_element_by_class_name(Deposit_Withdraw_Element.export_confirmation_ok_button).is_displayed()
        self.assertTrue(export_dialog_box, "User is not able export deposit history.")
        print("Expected Results: Export Confirmation dialog box popped out." + "<br>")

    def test_TC_Account_Transaction_Record_05_Table_Sorting_Account_Transaction_Record(self):
        Account_Transaction_Record_Actions.Navigate_Account_Transaction_Record(self)
        print("<li>" + "Click on Username header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Account_Transaction_Record_Element.username_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Name header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Account_Transaction_Record_Element.name_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Deposit Account Type header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Account_Transaction_Record_Element.deposit_account_type_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Type header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Account_Transaction_Record_Element.type_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Related Username header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Account_Transaction_Record_Element.related_username_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Original Amount header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Account_Transaction_Record_Element.original_amount_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Changes Amount header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Account_Transaction_Record_Element.changes_amount_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on New Amount header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Account_Transaction_Record_Element.new_amount_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Operation Period header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Account_Transaction_Record_Element.operation_period_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Remark header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Account_Transaction_Record_Element.remark_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Administrator header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Account_Transaction_Record_Element.administrator_header_sorting).click()
        self.driver.implicitly_wait(30)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Account Turnover", "Page breaks after clicking table sorting.")
        print("Expected Results: Page does not break after clicking table sorting." + "<br>")

    def test_TC_Account_Transaction_Record_06_View_All_Account_Turnover(self):
        Account_Transaction_Record_Actions.Navigate_Account_Transaction_Record(self)
        # Wait till button is clickable
        wait_all_button = EC.element_to_be_clickable((By.ID, Account_Transaction_Record_Element.all_button))
        WebDriverWait(self.driver, 30).until(wait_all_button)
        print("<li>" + "Click on All button" + "</li>" + "<br>")
        self.driver.find_element_by_id(Account_Transaction_Record_Element.all_button).click()
        self.driver.implicitly_wait(30)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Account Turnover", "Page breaks after clicking All button.")
        print("Expected Results: Page does not break after clicking All button." + "<br>")


if __name__ == '__main__':
    unittest.main()
