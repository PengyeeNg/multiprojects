import unittest
import SetUp.Base_SetUp
from Actions.member_page import Member_Edit_Actions
from Actions.member_page import Member_Levels_Actions
from Actions.member_page import Member_Log_Actions


class Navigate_Member_Modules(SetUp.Base_SetUp.BSetUp):

    def test_TC_Member_01_Navigate_Member_Edit_Page(self):
        Member_Edit_Actions.Navigate_Member_Edit(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Member_02_Navigate_Member_Levels_Page(self):
        Member_Levels_Actions.Navigate_Member_Levels(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Member_03_Navigate_Member_log_Page(self):
        Member_Log_Actions.Navigate_Member_Log(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")


if __name__ == '__main__':
    unittest.main()
