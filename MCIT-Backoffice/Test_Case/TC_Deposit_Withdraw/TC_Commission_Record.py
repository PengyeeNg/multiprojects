import unittest
import SetUp.Base_SetUp
from Actions.deposit_withdraw_page import Commission_Record_Actions
from Actions.deposit_withdraw_page import Deposit_Withdraw_Actions
from Elements.deposit_withdraw_page import Commission_Record_Element
from Elements.deposit_withdraw_page import Deposit_Withdraw_Element
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Input_Data.deposit_withdraw_page import Deposit_Withdraw_Data


class Commission_Record(SetUp.Base_SetUp.BSetUp):

    def test_TC_Commission_Record_01_Filter_Member_Commission_Details(self):
        Commission_Record_Actions.Navigate_Commision_Record(self)
        print("<li>" + "Insert Member Name" + "</li>" + "<br>")
        self.driver.find_element_by_id(Commission_Record_Element.member_name_filter_field).send_keys(Deposit_Withdraw_Data.member_name_filter)
        print("<li>" + "Click on Search button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Deposit_Withdraw_Element.filter_search_button).click()
        # Assert
        Deposit_Withdraw_Actions.Assert_Search_results(self)

    def test_TC_Commission_Record_02_View_All_Member_Commission_Details(self):
        Commission_Record_Actions.Navigate_Commision_Record(self)
        # Wait till button is clickable
        wait_all_button = EC.element_to_be_clickable((By.ID, Commission_Record_Element.all_button))
        WebDriverWait(self.driver, 30).until(wait_all_button)
        print("<li>" + "Click on All button" + "</li>" + "<br>")
        self.driver.find_element_by_id(Commission_Record_Element.all_button).click()
        self.driver.implicitly_wait(30)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Member Commission Details", "Page breaks after clicking All button.")
        print("Expected Results: Page does not break after clicking All button." + "<br>")

    def test_TC_Commission_Record_03_Table_Sorting_Commission(self):
        Commission_Record_Actions.Navigate_Commision_Record(self)
        print("<li>" + "Click on Nickname header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Commission_Record_Element.nickname_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Betting header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Commission_Record_Element.betting_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Rebate Amount header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Commission_Record_Element.rebate_amount_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Time header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Commission_Record_Element.time_header_sorting).click()
        self.driver.implicitly_wait(30)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Member Commission Details", "Page breaks after clicking table sorting.")
        print("Expected Results: Page does not break after clicking table sorting." + "<br>")


if __name__ == '__main__':
    unittest.main()
