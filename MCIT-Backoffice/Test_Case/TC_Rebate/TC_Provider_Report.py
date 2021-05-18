import unittest
import SetUp.Base_SetUp
from Actions.rebate_page import Provider_Report_Actions
from Actions.rebate_page import Rebate_Actions
from Elements.rebate_page import Provider_Report_Element
from Elements.rebate_page import Rebate_Element
from Input_Data.rebate_page import Rebate_Data
from selenium.webdriver.common.keys import Keys

class Provider_Report(SetUp.Base_SetUp.BSetUp):

    def test_TC_Provider_Report_01_Filter_Provider_Report(self):
        Provider_Report_Actions.Navigate_Provider_Report(self)
        self.driver.find_element_by_id(Provider_Report_Element.start_date_filter_field).send_keys(Rebate_Data.start_date_filter)
        self.driver.find_element_by_id(Provider_Report_Element.start_date_filter_field).send_keys(Keys.RETURN)
        self.driver.find_element_by_id(Provider_Report_Element.close_date_filter_field).send_keys(Rebate_Data.close_date_filter)
        self.driver.find_element_by_id(Provider_Report_Element.close_date_filter_field).send_keys(Keys.RETURN)
        self.driver.find_element_by_class_name(Rebate_Element.search_filter_button).click()
        self.driver.implicitly_wait(30)
        # Assert
        Rebate_Actions.Assert_Search_results(self)

    def test_TC_Provider_Report_02_View_All_Provider_Report(self):
        Provider_Report_Actions.Navigate_Provider_Report(self)
        Rebate_Actions.View_All(self)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Rebate Provider Report", "Page breaks after clicking All button.")
        print("Expected Results: Page does not break after clicking All button." + "<br>")

    def test_TC_Provider_Report_03_Table_Sorting_Provider_Report(self):
        Provider_Report_Actions.Navigate_Provider_Report(self)
        print("<li>" + "Click on Provider header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Provider_Report_Element.provider_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Bet Amount header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Provider_Report_Element.bet_amount_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Rebate Amount header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Provider_Report_Element.rebate_amount_header_sorting).click()
        self.driver.implicitly_wait(30)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Rebate Provider Report", "Page breaks after clicking table sorting.")
        print("Expected Results: Page does not break after clicking table sorting." + "<br>")


if __name__ == '__main__':
    unittest.main()
