import unittest
import SetUp.Base_SetUp
from Actions.promotion_page import List_Promotion_Actions
from Actions.promotion_page import Promotion_Banner_Actions
from Actions.promotion_page import Promotion_Statistic_Actions
from Actions.promotion_page import Promotion_Mission_Actions


class Navigate_Promotion_Modules(SetUp.Base_SetUp.BSetUp):

    def test_TC_Promotion_01_Navigate_List_Promotion_Page(self):
        List_Promotion_Actions.Navigate_List_Promotion(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Promotion_02_Navigate_Promotion_Banner_Page(self):
        Promotion_Banner_Actions.Navigate_Promotion_Banner(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Promotion_03_Navigate_Promotion_Statistic_Page(self):
        Promotion_Statistic_Actions.Navigate_Promotion_Statistic(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Promotion_04_Navigate_Promotion_Mission_Page(self):
        Promotion_Mission_Actions.Navigate_Promotion_Mission(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")


if __name__ == '__main__':
    unittest.main()
