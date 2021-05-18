import unittest
import SetUp.Base_SetUp
from Actions.report_page import Overall_Actions
from Actions.report_page import Report_Actions

class Overall(SetUp.Base_SetUp.BSetUp):

    def test_TC_Overall_01_Filter_Overall_Report(self):
        Overall_Actions.Navigate_Overall(self)
        Report_Actions.Filter_by_Member_Name(self)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Overall Report", "Page breaks after clicking Search button.")
        print("Expected Results: Page does not break after clicking Search button." + "<br>")


if __name__ == '__main__':
    unittest.main()
