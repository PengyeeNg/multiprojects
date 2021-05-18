import unittest
import SetUp.Base_SetUp
from Actions.deposit_withdraw_page import Deposit_History_Actions
from Actions.deposit_withdraw_page import Deposit_Withdraw_Actions
from Elements.deposit_withdraw_page import Deposit_History_Element
from Elements.deposit_withdraw_page import Deposit_Withdraw_Element
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class Deposit_History(SetUp.Base_SetUp.BSetUp):

    def test_TC_Deposit_History_01_Deal_Deposit(self):
        Deposit_History_Actions.Navigate_Deposit_History(self)
        print("<li>" + "Click on Deal button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Deposit_History_Element.deal_button).click()
        # Assert
        deal_dialog_box = self.driver.find_element_by_class_name(Deposit_History_Element.deal_save_button).is_displayed()
        self.assertTrue(deal_dialog_box, "User is not able to deal deposit.")
        print("Expected Results: Deal dialog box popped out." + "<br>")

    def test_TC_Deposit_History_02_Filter_Deposit(self):
        Deposit_History_Actions.Navigate_Deposit_History(self)
        Deposit_Withdraw_Actions.Filter_Deposit_Withdraw(self)
        Deposit_Withdraw_Actions.Assert_Search_results(self)

    def test_TC_Deposit_History_03_View_All_Deposit(self):
        Deposit_History_Actions.Navigate_Deposit_History(self)
        # Wait till button is clickable
        wait_all_button = EC.element_to_be_clickable((By.ID, Deposit_History_Element.all_button))
        WebDriverWait(self.driver, 30).until(wait_all_button)
        print("<li>" + "Click on All button" + "</li>" + "<br>")
        self.driver.find_element_by_id(Deposit_History_Element.all_button).click()
        self.driver.implicitly_wait(30)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Deposit Management", "Page breaks after clicking All button.")
        print("Expected Results: Page does not break after clicking All button." + "<br>")

    def test_TC_Deposit_History_04_Select_Column(self):
        Deposit_History_Actions.Navigate_Deposit_History(self)
        print("<li>" + "Click on Select column button" + "</li>" + "<br>")
        self.driver.find_element_by_id(Deposit_Withdraw_Element.select_column_button).click()
        # Wait till dropdown expanded
        wait_dropdown_expanded = EC.presence_of_element_located((By.CLASS_NAME, Deposit_Withdraw_Element.select_columns))
        WebDriverWait(self.driver, 10).until(wait_dropdown_expanded)
        print("<li>" + "Click on 'Select Columns'" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Deposit_Withdraw_Element.select_columns).click()
        #Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Deposit Management", "Page breaks after clicking 'Select Columns'.")
        print("Expected Results: Page does not break after clicking 'Select Column'." + "<br>")

    def test_TC_Deposit_History_05_Export_Deposit(self):
        Deposit_History_Actions.Navigate_Deposit_History(self)
        print("<li>" + "Click on Export button" + "</li>" + "<br>")
        self.driver.find_element_by_id(Deposit_Withdraw_Element.export_button).click()
        # Wait till dropdown expanded
        wait_dropdown_expanded = EC.presence_of_element_located((By.CLASS_NAME, Deposit_Withdraw_Element.html_button))
        WebDriverWait(self.driver, 10).until(wait_dropdown_expanded)
        print("<li>" + "Click on 'HTML'" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Deposit_Withdraw_Element.html_button).click()
        #Assert
        export_dialog_box = self.driver.find_element_by_class_name(Deposit_Withdraw_Element.export_confirmation_ok_button).is_displayed()
        self.assertTrue(export_dialog_box, "User is not able export deposit history.")
        print("Expected Results: Export Confirmation dialog box popped out." + "<br>")

    def test_TC_Deposit_History_06_Table_Sorting_Deposit(self):
        Deposit_History_Actions.Navigate_Deposit_History(self)
        print("<li>" + "Click on Topup Amount header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Deposit_History_Element.topup_amount_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Submit Period header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Deposit_History_Element.submit_period_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Approval Time header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Deposit_History_Element.approval_time_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Status" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Deposit_History_Element.status_header_sorting).click()
        self.driver.implicitly_wait(30)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Deposit Management", "Page breaks after clicking table sorting.")
        print("Expected Results: Page does not break after clicking table sorting." + "<br>")



if __name__ == '__main__':
    unittest.main()
