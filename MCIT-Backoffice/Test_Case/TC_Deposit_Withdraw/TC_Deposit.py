import unittest
import SetUp.Base_SetUp
from Actions.deposit_withdraw_page import Deposit_Actions
from Actions.deposit_withdraw_page import Deposit_Withdraw_Actions
from Elements.deposit_withdraw_page import Deposit_Element
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class Deposit(SetUp.Base_SetUp.BSetUp):

    def test_TC_Deposit_01_Lock_Deposit(self):
        Deposit_Actions.Navigate_Deposit(self)
        print("<li>" + "Click on lock icon" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Deposit_Element.lock_button).click()
        # Assert
        lock_dialog_box = self.driver.find_element_by_class_name(Deposit_Element.lock_confirmation_ok_button).is_displayed()
        self.assertTrue(lock_dialog_box, "User is not able to lock deposit.")
        print("Expected Results: Lock dialog box popped out." + "<br>")

    def test_TC_Deposit_02_Filter_Deposit(self):
        Deposit_Actions.Navigate_Deposit(self)
        Deposit_Withdraw_Actions.Filter_Deposit_Withdraw(self)
        Deposit_Withdraw_Actions.Assert_Search_results(self)

    def test_TC_Deposit_03_Deal_Deposit(self):
        Deposit_Actions.Navigate_Deposit(self)
        print("<li>" + "Click on Deal button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Deposit_Element.deal_button).click()
        # Assert
        deal_dialog_box = self.driver.find_element_by_class_name(Deposit_Element.deal_save_button).is_displayed()
        self.assertTrue(deal_dialog_box, "User is not able to deal deposit.")
        print("Expected Results: Deal dialog box popped out." + "<br>")

    def test_TC_Deposit_04_Table_Sorting_Deposit(self):
        Deposit_Actions.Navigate_Deposit(self)
        print("<li>" + "Click on Topup Amount header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Deposit_Element.topup_amount_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Submit Period header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Deposit_Element.submit_period_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Approval Time header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Deposit_Element.approval_time_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Status" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Deposit_Element.status_header_sorting).click()
        self.driver.implicitly_wait(30)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Deposit Management", "Page breaks after clicking table sorting.")
        print("Expected Results: Page does not break after clicking table sorting." + "<br>")

    def test_TC_Deposit_05_View_All_Deposit(self):
        Deposit_Actions.Navigate_Deposit(self)
        # Wait till button is clickable
        wait_all_button = EC.element_to_be_clickable((By.ID, Deposit_Element.all_button))
        WebDriverWait(self.driver, 30).until(wait_all_button)
        print("<li>" + "Click on All button" + "</li>" + "<br>")
        self.driver.find_element_by_id(Deposit_Element.all_button).click()
        self.driver.implicitly_wait(30)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Deposit Management", "Page breaks after clicking All button.")
        print("Expected Results: Page does not break after clicking All button." + "<br>")



if __name__ == '__main__':
    unittest.main()
