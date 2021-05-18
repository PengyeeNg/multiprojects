import unittest
import SetUp.Base_SetUp
from Actions.report_page import Merchant_Daily_Win_Loss_Actions
from Elements.report_page import Report_Element
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class Merchant_Daily_Win_Loss(SetUp.Base_SetUp.BSetUp):

    def test_TC_Merchant_Daily_Win_Loss_01_Filter_Merchant_Daily_Win_Loss_Report(self):
        Merchant_Daily_Win_Loss_Actions.Navigate_Merchant_Daily_Win_Loss(self)
        print("<li>" + "Select Range- Today" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Report_Element.range_today_button).click()
        print("<li>" + "Click on Search button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Report_Element.search_filter_button).click()
        # Wait filter
        wait_filter = EC.text_to_be_present_in_element((By.ID, Report_Element.start_date_filter_field),"")
        WebDriverWait(self.driver, 10).until(wait_filter)
        wait_filter = EC.text_to_be_present_in_element((By.ID, Report_Element.end_date_filter_field), "")
        WebDriverWait(self.driver, 10).until(wait_filter)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Merchant Daily Win/loss", "Page breaks after clicking Search button.")
        print("Expected Results: Page does not break after clicking Search button." + "<br>")

    def test_TC_Merchant_Daily_Win_Loss_02_Reset_Filter_Merchant_Daily_Win_Loss_Report(self):
        Merchant_Daily_Win_Loss_Actions.Navigate_Merchant_Daily_Win_Loss(self)
        print("<li>" + "Select Range- Today" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Report_Element.range_today_button).click()
        print("<li>" + "Click on Reset button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Report_Element.reset_search_button).click()
        # Assert Field is Empty
        empty_start_date = self.driver.find_element_by_id(Report_Element.start_date_filter_field).text
        self.assertEqual(empty_start_date, "", "Use is not able to reset search.")
        empty_end_date = self.driver.find_element_by_id(Report_Element.end_date_filter_field).text
        self.assertEqual(empty_end_date, "", "Use is not able to reset search.")
        print("Expected Results: Today's start and end date and time removed from Start and End field." + "<br>")


if __name__ == '__main__':
    unittest.main()
