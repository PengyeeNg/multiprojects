import unittest
import SetUp.Base_SetUp
from Actions.report_page import Mega_Actions
from Actions.report_page import Betting_Record_Actions
from Elements.report_page import Betting_Record_Mega_Betting_Record_Element
from Elements.report_page import Report_Element
from Input_Data.report_page import Report_Data

class Mega_Betting_Record(SetUp.Base_SetUp.BSetUp):

    def test_TC_Mega_Bet_01_Filter_Mega_Bet(self):
        Mega_Actions.Navigate_Mega(self)
        print("<li>" + "Insert Member Name" + "</li>" + "<br>")
        self.driver.find_element_by_id(Betting_Record_Mega_Betting_Record_Element.member_name_filter_field).send_keys(Report_Data.member_name_filter)
        print("<li>" + "Click on Search button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Report_Element.search_filter_button).click()
        self.driver.implicitly_wait(30)
        Betting_Record_Actions.Assert_Search_results(self)

    def test_TC_Mega_Bet_02_Reset_Filter_Mega_Bet(self):
        Mega_Actions.Navigate_Mega(self)
        print("<li>" + "Insert Member Name" + "</li>" + "<br>")
        self.driver.find_element_by_id(Betting_Record_Mega_Betting_Record_Element.member_name_filter_field).send_keys(Report_Data.member_name_filter)
        print("<li>" + "Click on Reset button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Report_Element.reset_search_button).click()
        # Assert Field is Empty
        empty_member_name_field = self.driver.find_element_by_id(Betting_Record_Mega_Betting_Record_Element.member_name_filter_field).text
        self.assertEqual(empty_member_name_field, "", "Use is not able to reset search.")
        print("Expected Results: Member ID removed from Member ID field." + "<br>")

    def test_TC_Mega_Bet_03_View_All_Mega_Bet(self):
        Mega_Actions.Navigate_Mega(self)
        Betting_Record_Actions.View_All(self)

    def test_TC_Mega_Bet_04_Table_Sorting_Mega(self):
        Mega_Actions.Navigate_Mega(self)
        print("<li>" + "Click on User ID header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Betting_Record_Mega_Betting_Record_Element.user_id_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Bet Amount header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Betting_Record_Mega_Betting_Record_Element.bet_amount_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Win/Lose header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Betting_Record_Mega_Betting_Record_Element.win_lose_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Betting Period header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Betting_Record_Mega_Betting_Record_Element.betting_period_header_sorting).click()
        self.driver.implicitly_wait(30)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Mega bet", "Page breaks after clicking table sorting.")
        print("Expected Results: Page does not break after clicking table sorting." + "<br>")


if __name__ == '__main__':
    unittest.main()