import unittest
import SetUp.Base_SetUp
from Actions.rebate_page import Member_Report_Actions
from Actions.rebate_page import Rebate_Actions
from Elements.rebate_page import Member_Report_Element
from Elements.rebate_page import Rebate_Element
from Input_Data.rebate_page import Rebate_Data


class Member_Report(SetUp.Base_SetUp.BSetUp):

    def test_TC_Member_Report_01_Filter_Provider_Report(self):
        Member_Report_Actions.Navigate_Member_Report(self)
        print("<li>" + "Insert Member ID" + "</li>" + "<br>")
        self.driver.find_element_by_id(Member_Report_Element.member_id_filter_field).send_keys(Rebate_Data.member_id_filter)
        print("<li>" + "Click on Search button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Rebate_Element.search_filter_button).click()
        # Assert
        Rebate_Actions.Assert_Search_results(self)

    def test_TC_Member_Report_02_View_All_Provider_Report(self):
        Member_Report_Actions.Navigate_Member_Report(self)
        Rebate_Actions.View_All(self)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Rebate Player Report", "Page breaks after clicking All button.")
        print("Expected Results: Page does not break after clicking All button." + "<br>")

    def test_TC_Member_Report_03_Table_Sorting_Provider_Report(self):
        Member_Report_Actions.Navigate_Member_Report(self)
        print("<li>" + "Click on Bet Amount header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Report_Element.bet_amount_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Rebate Amount header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Report_Element.rebate_amount_header_sorting).click()
        self.driver.implicitly_wait(30)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Rebate Player Report", "Page breaks after clicking table sorting.")
        print("Expected Results: Page does not break after clicking table sorting." + "<br>")



if __name__ == '__main__':
    unittest.main()
