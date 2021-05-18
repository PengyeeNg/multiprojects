import unittest
import SetUp.Base_SetUp
from Actions.main_page import General_Actions
from Actions.member_page import Member_Log_Actions
from Elements.member_page import Member_Log_Element
from Input_Data.member_page import Member_Data


class Member_Log(SetUp.Base_SetUp.BSetUp):

    def test_TC_Member_Levels_01_Search_Member_Login_Log(self):
        Member_Log_Actions.Navigate_Member_Log(self)
        print("<li>" + "Insert Member Name" + "</li>" + "<br>")
        self.driver.find_element_by_id(Member_Log_Element.member_name_filter_field).send_keys(Member_Data.filter_name)
        print("<li>" + "Click on search icon" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Log_Element.filter_search_button).click()
        # Assert
        General_Actions.Assert_Filter_Results(self)

    def test_TC_Member_Levels_02_View_All_Member_Login_Log(self):
        Member_Log_Actions.Navigate_Member_Log(self)
        print("<li>" + "Click on All button" + "</li>" + "<br>")
        self.driver.find_element_by_id(Member_Log_Element.all_button).click()
        self.driver.implicitly_wait(30)
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Member Login Log", "Page breaks after clicking All button.")
        print("Expected Results: Page does not break after clicking All button." + "<br>")

    def test_TC_Member_Levels_03_Reset_Search(self):
        Member_Log_Actions.Navigate_Member_Log(self)
        print("<li>" + "Insert Member Name" + "</li>" + "<br>")
        self.driver.find_element_by_id(Member_Log_Element.member_name_filter_field).send_keys(Member_Data.filter_name)
        print("<li>" + "Click on Reset button" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Log_Element.reset_search_button).click()
        # Assert Field is Empty
        empty_field = self.driver.find_element_by_id(Member_Log_Element.member_name_filter_field).text
        self.assertEqual(empty_field, "", "Use is not able to reset search.")
        print("Expected Results: The Member Login Log search is reset." + "<br>")


if __name__ == '__main__':
    unittest.main()
