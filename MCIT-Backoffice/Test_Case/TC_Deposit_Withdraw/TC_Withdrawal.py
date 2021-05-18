import unittest
import SetUp.Base_SetUp
from Actions.deposit_withdraw_page import Withdrawal_Actions
from Actions.deposit_withdraw_page import Deposit_Withdraw_Actions
from Elements.deposit_withdraw_page import Withdrawal_Element
from Elements.deposit_withdraw_page import Deposit_Withdraw_Element
from Input_Data.deposit_withdraw_page import Deposit_Withdraw_Data
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class Withdrawal(SetUp.Base_SetUp.BSetUp):

    def test_TC_Withdrawal_01_Filter_Deposit(self):
        Withdrawal_Actions.Navigate_Withdrawal(self)
        print("<li>" + "Click on add icon at the end of filter column" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Deposit_Withdraw_Element.filter_add_button).click()
        wait_filter_column_expand = EC.presence_of_element_located((By.CLASS_NAME, Deposit_Withdraw_Element.filter_search_button))
        WebDriverWait(self.driver, 10).until(wait_filter_column_expand)
        print("<li>" + "Insert Username" + "</li>" + "<br>")
        self.driver.find_element_by_id(Withdrawal_Element.username_filter_field).send_keys(Deposit_Withdraw_Data.username_filter)
        print("<li>" + "Click on Search button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Deposit_Withdraw_Element.filter_search_button).click()
        # Assert
        Deposit_Withdraw_Actions.Assert_Search_results(self)

    def test_TC_Withdrawal_02_Table_Sorting_Withdrawal(self):
        Withdrawal_Actions.Navigate_Withdrawal(self)
        print("<li>" + "Click on Withdraw Type header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Withdrawal_Element.withdraw_type_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Withdrawal Amount header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Withdrawal_Element.withdrawal_amount_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Withdrawal Time header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Withdrawal_Element.withdrawal_time_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Status" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Withdrawal_Element.status_header_sorting).click()
        self.driver.implicitly_wait(30)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Withdrawal Management", "Page breaks after clicking table sorting.")
        print("Expected Results: Page does not break after clicking table sorting." + "<br>")

    def test_TC_Withdrawal_03_View_All_Withdrawal(self):
        Withdrawal_Actions.Navigate_Withdrawal(self)
        # Wait till button is clickable
        wait_all_button = EC.element_to_be_clickable((By.ID, Withdrawal_Element.all_button))
        WebDriverWait(self.driver, 30).until(wait_all_button)
        print("<li>" + "Click on All button" + "</li>" + "<br>")
        self.driver.find_element_by_id(Withdrawal_Element.all_button).click()
        self.driver.implicitly_wait(30)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Withdrawal Management", "Page breaks after clicking All button.")
        print("Expected Results: Page does not break after clicking All button." + "<br>")

    def test_TC_Withdrawal_04_Lock_Withdrawal(self):
        Withdrawal_Actions.Navigate_Withdrawal(self)
        # Assert
        check_lock = self.driver.find_element_by_class_name(Withdrawal_Element.locked_withdrawal_button).is_displayed()
        if check_lock is True:
            self.driver.find_element_by_class_name(Withdrawal_Element.locked_withdrawal_button).click()
            alert = WebDriverWait(self.driver, 20).until(EC.alert_is_present())
            # Switch the control to the Alert window
            a = self.driver.switch_to_alert()
            a.accept()
            print("<li>" + "Click on Lock button" + "</li>" + "<br>")
            self.driver.find_element_by_class_name(Withdrawal_Element.lock_withdrawal_button).click()
            alert = WebDriverWait(self.driver, 20).until(EC.alert_is_present())
            # Switch the control to the Alert window
            a = self.driver.switch_to_alert()
            a.accept()
            # Assert
            lock_icon = self.driver.find_element_by_class_name(Withdrawal_Element.locked_withdrawal_button).is_displayed()
            self.assertTrue(lock_icon, "User is not able to lock withdrawal.")
            print("Expected Results: Withdrawal is locked." + "<br>")
        else:
            print("no true")
            print("<li>" + "Click on Lock button" + "</li>" + "<br>")
            self.driver.find_element_by_class_name(Withdrawal_Element.lock_withdrawal_button).click()
            alert = WebDriverWait(self.driver, 20).until(EC.alert_is_present())
            # Switch the control to the Alert window
            a = self.driver.switch_to_alert()
            a.accept()
            # Assert
            lock_icon = self.driver.find_element_by_class_name(Withdrawal_Element.locked_withdrawal_button).is_displayed()
            self.assertTrue(lock_icon, "User is not able to lock withdrawal.")
            print("Expected Results: Withdrawal is locked." + "<br>")

    def test_TC_Withdrawal_05_Deal_Withdrawal(self):
        Withdrawal_Actions.Navigate_Withdrawal(self)
        print("<li>" + "Click on Deal button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Withdrawal_Element.deal_withdrawal_button).click()
        # Wait dialog box to display
        wait_deal_dialog_box = EC.presence_of_element_located((By.ID, Withdrawal_Element.deal_confirmation_submit_button))
        WebDriverWait(self.driver, 10).until(wait_deal_dialog_box)
        # Assert
        deal_dialog_box = self.driver.find_element_by_id(Withdrawal_Element.deal_confirmation_submit_button).is_displayed()
        self.assertTrue(deal_dialog_box, "User is not able to deal withdrawal.")
        print("Expected Results: Deal dialog box popped out." + "<br>")


if __name__ == '__main__':
    unittest.main()
