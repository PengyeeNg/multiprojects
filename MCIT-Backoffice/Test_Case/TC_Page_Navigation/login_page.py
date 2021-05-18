import unittest
import SetUp.Base_SetUp
from Actions.login_page import Login_Actions


class Navigate_Login_Modules(SetUp.Base_SetUp.BSetUp):

    def test_TC_Login_01_Navigate_Home_Page(self):
        Login_Actions.valid_login_flow(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")


if __name__ == '__main__':
    unittest.main()
