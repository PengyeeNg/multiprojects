import unittest
import SetUp.Base_SetUp
from Actions.deposit_withdraw_page import Deposit_History_Actions
from Actions.deposit_withdraw_page import Deposit_Actions
from Actions.deposit_withdraw_page import Withdraw_History_Actions
from Actions.deposit_withdraw_page import Withdrawal_Actions
from Actions.deposit_withdraw_page import Adjust_Balance_Actions
from Actions.deposit_withdraw_page import Account_Transaction_Record_Actions
from Actions.deposit_withdraw_page import Bonus_Actions
from Actions.deposit_withdraw_page import Commission_Record_Actions
from Actions.deposit_withdraw_page import Adjustment_Record_Actions
from Actions.deposit_withdraw_page import Turn_Over_Amount_Record_Actions
from Actions.deposit_withdraw_page import Wallet_Transfer_Actions


class Navigate_Deposit_Withdraw_Modules(SetUp.Base_SetUp.BSetUp):

    def test_TC_Deposit_Withdraw_01_Navigate_Deposit_Page(self):
        Deposit_Actions.Navigate_Deposit(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Deposit_Withdraw_02_Deposit_History_Page(self):
        Deposit_History_Actions.Navigate_Deposit_History(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Deposit_Withdraw_03_Navigate_Withdrawal_Page(self):
        Withdrawal_Actions.Navigate_Withdrawal(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Deposit_Withdraw_04_Navigate_Withdraw_History_Page(self):
        Withdraw_History_Actions.Navigate_Withdraw_History(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Deposit_Withdraw_05_Navigate_Adjust_Balance_Page(self):
        Adjust_Balance_Actions.Navigate_Adjust_Balance(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Deposit_Withdraw_06_Navigate_Account_Transaction_Record_Page(self):
        Account_Transaction_Record_Actions.Navigate_Account_Transaction_Record(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Deposit_Withdraw_07_Navigate_Bonus_Page(self):
        Bonus_Actions.Navigate_Bonus(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Deposit_Withdraw_08_Navigate_Commission_Record_Page(self):
        Commission_Record_Actions.Navigate_Commision_Record(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Deposit_Withdraw_09_Navigate_Adjustment_Record_Page(self):
        Adjustment_Record_Actions.Navigate_Adjustment_Record(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Deposit_Withdraw_10_Navigate_Turn_Over_Amount_record_Page(self):
        Turn_Over_Amount_Record_Actions.Navigate_Turn_Over_Amount_Record(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Deposit_Withdraw_11_Navigate_Wallet_Transfer_Page(self):
        Wallet_Transfer_Actions.Navigate_Wallet_Transfer(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

if __name__ == '__main__':
    unittest.main()
