import unittest
import SetUp.Base_SetUp
from Actions.deposit_withdraw_page import Bonus_Actions
from Actions.deposit_withdraw_page import Deposit_Withdraw_Actions
from Elements.deposit_withdraw_page import Bonus_Element
from Elements.deposit_withdraw_page import Deposit_Withdraw_Element
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Input_Data.deposit_withdraw_page import Deposit_Withdraw_Data


class Bonus(SetUp.Base_SetUp.BSetUp):

    def test_TC_Bonus_Record_01_Search_Bonus(self):
        Bonus_Actions.Navigate_Bonus(self)
        print("<li>" + "Insert Username" + "</li>" + "<br>")
        self.driver.find_element_by_id(Bonus_Element.username_filter_field).send_keys(Deposit_Withdraw_Data.username_filter)
        print("<li>" + "Click on Search button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Deposit_Withdraw_Element.filter_search_button).click()
        # Assert
        Deposit_Withdraw_Actions.Assert_Search_results(self)

    def test_TC_Bonus_Record_02_View_All_Bonus(self):
        Bonus_Actions.Navigate_Bonus(self)
        # Wait till button is clickable
        wait_all_button = EC.element_to_be_clickable((By.ID, Bonus_Element.all_button))
        WebDriverWait(self.driver, 30).until(wait_all_button)
        print("<li>" + "Click on All button" + "</li>" + "<br>")
        self.driver.find_element_by_id(Bonus_Element.all_button).click()
        self.driver.implicitly_wait(30)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Bonus Management", "Page breaks after clicking All button.")
        print("Expected Results: Page does not break after clicking All button." + "<br>")

    def test_TC_Bonus_Record_03_Table_Sorting_Bonus(self):
        Bonus_Actions.Navigate_Bonus(self)
        print("<li>" + "Click on Username header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Bonus_Element.username_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Credit header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Bonus_Element.credit_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Bonus Type header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Bonus_Element.bonus_type_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Status header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Bonus_Element.status_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Bonus Period header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Bonus_Element.bonus_period_sorting).click()
        self.driver.implicitly_wait(30)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Bonus Management", "Page breaks after clicking table sorting.")
        print("Expected Results: Page does not break after clicking table sorting." + "<br>")

    def test_TC_Bonus_Record_04_Verify_Bonus(self):
        Bonus_Actions.Navigate_Bonus(self)
        # Wait till button is clickable
        wait_verified_button = EC.element_to_be_clickable((By.CLASS_NAME, Bonus_Element.verified_status_button))
        WebDriverWait(self.driver, 30).until(wait_verified_button)
        print("<li>" + "Click on 'Verified' button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Bonus_Element.verified_status_button).click()
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Bonus Management", "Page breaks after clicking 'Verified' button.")
        print("Expected Results: Page does not break after clicking 'Verified' button." + "<br>")


if __name__ == '__main__':
    unittest.main()
