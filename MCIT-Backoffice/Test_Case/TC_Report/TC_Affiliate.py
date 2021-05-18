import unittest
import SetUp.Base_SetUp
from Actions.report_page import Affiliate_Actions
from Actions.report_page import Report_Actions


class Affiliate(SetUp.Base_SetUp.BSetUp):

    def test_TC_Affiliat_01_Filter_Affiliate_Report(self):
        Affiliate_Actions.Navigate_Affiliate(self)
        Report_Actions.Filter_by_Member_Name(self)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Overall Report", "Page breaks after clicking Search button.")
        print("Expected Results: Page does not break after clicking Search button." + "<br>")


if __name__ == '__main__':
    unittest.main()
