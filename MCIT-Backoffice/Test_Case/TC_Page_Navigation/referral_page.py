import unittest
import SetUp.Base_SetUp
from Actions.referral_page import Member_Map_Actions


class Navigate_Referral_Modules(SetUp.Base_SetUp.BSetUp):

    def test_TC_Referral_01_Navigate_Member_Map_Page(self):
        Member_Map_Actions.Navigate_New_Member_Map(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")


if __name__ == '__main__':
    unittest.main()
