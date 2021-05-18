import unittest
import SetUp.Base_SetUp
from Actions.announcement_page import Member_Message_Actions


class Navigate_Announcement_Modules(SetUp.Base_SetUp.BSetUp):

    def test_TC_Announcement_01_Navigate_Member_Message_Page(self):
        Member_Message_Actions.Navigate_Member_Message(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

if __name__ == '__main__':
    unittest.main()
