import unittest
import SetUp.Base_SetUp
from Actions.administrarion_page import Admin_Log_Actions
from Actions.administrarion_page import Admin_List_Actions


class Navigate_Administration_Modules(SetUp.Base_SetUp.BSetUp):

    def test_TC_Administration_01_Navigate_Admin_Log_Page(self):
        Admin_Log_Actions.Navigate_Admin_Log(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Administration_02_Navigate_Admin_List_Page(self):
        Admin_List_Actions.Navigate_Admin_List(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

if __name__ == '__main__':
    unittest.main()
