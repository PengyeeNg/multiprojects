import unittest
import SetUp.Base_SetUp
from Actions.deposit_withdraw_page import Adjustment_Record_Actions
from Actions.deposit_withdraw_page import Deposit_Withdraw_Actions
from Elements.deposit_withdraw_page import Adjustment_Record_Element
from Elements.deposit_withdraw_page import Deposit_Withdraw_Element
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Input_Data.deposit_withdraw_page import Deposit_Withdraw_Data


class Adjustment_Record(SetUp.Base_SetUp.BSetUp):

    def test_TC_Adjustment_Record_01_Filter_Adjustment_Record(self):
        Adjustment_Record_Actions.Navigate_Adjustment_Record(self)
        print("<li>" + "Insert Member Name" + "</li>" + "<br>")
        self.driver.find_element_by_id(Adjustment_Record_Element.member_name_filter_field).send_keys(Deposit_Withdraw_Data.member_name_filter)
        print("<li>" + "Click on Search button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Deposit_Withdraw_Element.filter_search_button).click()
        # Assert
        Deposit_Withdraw_Actions.Assert_Search_results(self)

    def test_TC_Adjustment_Record_02_Reset_Filter(self):
        Adjustment_Record_Actions.Navigate_Adjustment_Record(self)
        print("<li>" + "Insert Member Name" + "</li>" + "<br>")
        self.driver.find_element_by_id(Adjustment_Record_Element.member_name_filter_field).send_keys(Deposit_Withdraw_Data.member_name_filter)
        print("<li>" + "Click on Reset button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Deposit_Withdraw_Element.reset_search_button).click()
        self.driver.implicitly_wait(30)
        # Assert Field is Empty
        empty_field = self.driver.find_element_by_id(Adjustment_Record_Element.member_name_filter_field).text
        self.assertEqual(empty_field, "", "Use is not able to reset search.")
        print("Expected Results: Member name removed from Member Name field." + "<br>")

    def test_TC_Adjustment_Record_03_View_All_Adjustment_Record(self):
        Adjustment_Record_Actions.Navigate_Adjustment_Record(self)
        # Wait till button is clickable
        wait_all_button = EC.element_to_be_clickable((By.ID, Adjustment_Record_Element.all_button))
        WebDriverWait(self.driver, 30).until(wait_all_button)
        print("<li>" + "Click on All button" + "</li>" + "<br>")
        self.driver.find_element_by_id(Adjustment_Record_Element.all_button).click()
        self.driver.implicitly_wait(30)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Adjustment Record", "Page breaks after clicking All button.")
        print("Expected Results: Page does not break after clicking All button." + "<br>")

    def test_TC_Adjustment_Record_04_Table_Sorting_Adjustment_Record(self):
        Adjustment_Record_Actions.Navigate_Adjustment_Record(self)
        print("<li>" + "Click on Username header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Adjustment_Record_Element.username_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Operation Type header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Adjustment_Record_Element.operation_type_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Operation Amount header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Adjustment_Record_Element.operation_amount_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Turn Over header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Adjustment_Record_Element.turn_over_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Turn Over Amount header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Adjustment_Record_Element.turn_over_amount_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Benefits From Activity header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Adjustment_Record_Element.benefits_from_activity_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Credit header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Adjustment_Record_Element.credit_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Operation Period header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Adjustment_Record_Element.operation_period_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Remark header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Adjustment_Record_Element.remark_header_sorting).click()
        self.driver.implicitly_wait(30)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Adjustment Record", "Page breaks after clicking table sorting.")
        print("Expected Results: Page does not break after clicking table sorting." + "<br>")


if __name__ == '__main__':
    unittest.main()

