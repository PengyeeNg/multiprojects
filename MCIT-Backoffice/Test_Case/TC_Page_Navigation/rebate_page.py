import unittest
import SetUp.Base_SetUp
from Actions.rebate_page import Rebate_Setting_Actions
from Actions.rebate_page import Rebate_record_Actions
from Actions.rebate_page import Provider_Report_Actions
from Actions.rebate_page import Member_Report_Actions


class Navigate_Rebate_Modules(SetUp.Base_SetUp.BSetUp):

    def test_TC_Rebate_01_Navigate_Rebate_Setting_Page(self):
        Rebate_Setting_Actions.Navigate_Rebate_Setting(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Rebate_02_Navigate_Rebate_Record_Page(self):
        Rebate_record_Actions.Navigate_Rebate_Record(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Rebate_03_Navigate_Provider_Report_Page(self):
        Provider_Report_Actions.Navigate_Provider_Report(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Rebate_04_Navigate_Member_Report_Page(self):
        Member_Report_Actions.Navigate_Member_Report(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")



if __name__ == '__main__':
    unittest.main()
