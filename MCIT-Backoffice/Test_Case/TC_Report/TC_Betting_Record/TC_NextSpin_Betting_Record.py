import unittest
import SetUp.Base_SetUp
from Actions.report_page import Nextspin_Actions
from Actions.report_page import Betting_Record_Actions
from Elements.report_page import Betting_Record_Nextspin_Betting_Record_Element
from Elements.report_page import Report_Element
from Input_Data.report_page import Report_Data

class NextSpin_Betting_Record(SetUp.Base_SetUp.BSetUp):

    def test_TC_NextSpin_Bet_01_Filter_NextSpin_Bet(self):
        Nextspin_Actions.Navigate_Nextspin(self)
        print("<li>" + "Insert Member Name" + "</li>" + "<br>")
        self.driver.find_element_by_id(Betting_Record_Nextspin_Betting_Record_Element.member_name_filter_field).send_keys(Report_Data.member_name_filter)
        print("<li>" + "Click on Search button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Report_Element.search_filter_button).click()
        self.driver.implicitly_wait(30)
        Betting_Record_Actions.Assert_Search_results(self)

    def test_TC_NextSpin_Bet_02_Reset_Filter_NextSpin_Bet(self):
        Nextspin_Actions.Navigate_Nextspin(self)
        print("<li>" + "Insert Member Name" + "</li>" + "<br>")
        self.driver.find_element_by_id(Betting_Record_Nextspin_Betting_Record_Element.member_name_filter_field).send_keys(Report_Data.member_name_filter)
        print("<li>" + "Click on Reset button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Report_Element.reset_search_button).click()
        # Assert Field is Empty
        empty_member_name_field = self.driver.find_element_by_id(Betting_Record_Nextspin_Betting_Record_Element.member_name_filter_field).text
        self.assertEqual(empty_member_name_field, "", "Use is not able to reset search.")
        print("Expected Results: Member ID removed from Member ID field." + "<br>")

    def test_TC_NextSpin_Bet_03_View_All_NextSpin_Bet(self):
        Nextspin_Actions.Navigate_Nextspin(self)
        Betting_Record_Actions.View_All(self)

    def test_TC_NextSpin_Bet_04_Table_Sorting_NextSpin(self):
        Nextspin_Actions.Navigate_Nextspin(self)
        print("<li>" + "Click on User ID header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Betting_Record_Nextspin_Betting_Record_Element.user_id_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Valid Amount header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Betting_Record_Nextspin_Betting_Record_Element.valid_amount_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Win/Lose header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Betting_Record_Nextspin_Betting_Record_Element.win_loss_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Bet Time header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Betting_Record_Nextspin_Betting_Record_Element.bet_time_header_sorting).click()
        self.driver.implicitly_wait(30)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Nextspin", "Page breaks after clicking table sorting.")
        print("Expected Results: Page does not break after clicking table sorting." + "<br>")


if __name__ == '__main__':
    unittest.main()