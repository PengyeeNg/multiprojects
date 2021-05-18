import unittest
import SetUp.Base_SetUp
from Actions.deposit_withdraw_page import Withdraw_History_Actions
from Actions.deposit_withdraw_page import Deposit_Withdraw_Actions
from Elements.deposit_withdraw_page import Withdraw_History_Element
from Elements.deposit_withdraw_page import Deposit_Withdraw_Element
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Input_Data.deposit_withdraw_page import Deposit_Withdraw_Data

class Withdraw_History(SetUp.Base_SetUp.BSetUp):

    def test_TC_Withdraw_History_01_Filter_Withdrawal_History(self):
        Withdraw_History_Actions.Navigate_Withdraw_History(self)
        print("<li>" + "Click on add icon at the end of filter column" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Deposit_Withdraw_Element.filter_add_button).click()
        wait_filter_column_expand = EC.presence_of_element_located((By.CLASS_NAME, Deposit_Withdraw_Element.filter_search_button))
        WebDriverWait(self.driver, 10).until(wait_filter_column_expand)
        print("<li>" + "Insert Username" + "</li>" + "<br>")
        self.driver.find_element_by_id(Withdraw_History_Element.username_filter_field).send_keys(Deposit_Withdraw_Data.username_filter)
        print("<li>" + "Click on Search button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Deposit_Withdraw_Element.filter_search_button).click()
        # Assert
        Deposit_Withdraw_Actions.Assert_Search_results(self)

    def test_TC_Withdraw_History_02_Select_Column(self):
        Withdraw_History_Actions.Navigate_Withdraw_History(self)
        print("<li>" + "Click on Select column button" + "</li>" + "<br>")
        self.driver.find_element_by_id(Deposit_Withdraw_Element.select_column_button).click()
        # Wait till dropdown expanded
        wait_dropdown_expanded = EC.presence_of_element_located((By.CLASS_NAME, Deposit_Withdraw_Element.select_columns))
        WebDriverWait(self.driver, 10).until(wait_dropdown_expanded)
        print("<li>" + "Click on 'Select Columns'" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Deposit_Withdraw_Element.select_columns).click()
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Withdrawal Management", "Page breaks after clicking 'Select Columns'.")
        print("Expected Results: Page does not break after clicking 'Select Column'." + "<br>")

    def test_TC_Withdraw_History_03_Export_Withdrawal(self):
        Withdraw_History_Actions.Navigate_Withdraw_History(self)
        print("<li>" + "Click on Export button" + "</li>" + "<br>")
        self.driver.find_element_by_id(Deposit_Withdraw_Element.export_button).click()
        # Wait till dropdown expanded
        wait_dropdown_expanded = EC.presence_of_element_located((By.CLASS_NAME, Deposit_Withdraw_Element.html_button))
        WebDriverWait(self.driver, 10).until(wait_dropdown_expanded)
        print("<li>" + "Click on 'HTML'" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Deposit_Withdraw_Element.html_button).click()
        # Assert
        export_dialog_box = self.driver.find_element_by_class_name(Deposit_Withdraw_Element.export_confirmation_ok_button).is_displayed()
        self.assertTrue(export_dialog_box, "User is not able export deposit history.")
        print("Expected Results: Export Confirmation dialog box popped out." + "<br>")

    def test_TC_Withdraw_History_04_View_All_Withdraw_History(self):
        Withdraw_History_Actions.Navigate_Withdraw_History(self)
        # Wait till button is clickable
        wait_all_button = EC.element_to_be_clickable((By.ID, Withdraw_History_Element.all_button))
        WebDriverWait(self.driver, 30).until(wait_all_button)
        print("<li>" + "Click on All button" + "</li>" + "<br>")
        self.driver.find_element_by_id(Withdraw_History_Element.all_button).click()
        self.driver.implicitly_wait(30)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Withdrawal Management", "Page breaks after clicking All button.")
        print("Expected Results: Page does not break after clicking All button." + "<br>")

    def test_TC_Withdraw_History_05_Table_Sorting_Withdraw_History(self):
        Withdraw_History_Actions.Navigate_Withdraw_History(self)
        print("<li>" + "Click on Withdraw Type header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Withdraw_History_Element.withdraw_type_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Withdrawal Amount header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Withdraw_History_Element.withdrawal_amount_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Withdrawal Time header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Withdraw_History_Element.withdrawal_time_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Approval Time header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Withdraw_History_Element.approval_time_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Status header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Withdraw_History_Element.status_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Reason header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Withdraw_History_Element.reason_header_sorting).click()
        self.driver.implicitly_wait(30)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Withdrawal Management", "Page breaks after clicking table sorting.")
        print("Expected Results: Page does not break after clicking table sorting." + "<br>")

if __name__ == '__main__':
    unittest.main()
