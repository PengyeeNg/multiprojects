import unittest
import SetUp.Base_SetUp
from Actions.bank_page import Bank_Account_Actions


class Navigate_Bank_Modules(SetUp.Base_SetUp.BSetUp):

    def test_TC_Bank_01_Navigate_Bank_Account_Page(self):
        Bank_Account_Actions.Navigate_Bank_Account(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

if __name__ == '__main__':
    unittest.main()
