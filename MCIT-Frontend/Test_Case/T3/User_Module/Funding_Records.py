import unittest
from Actions.T3.user_page import UserpageActions
from Setup.T3 import Base_Setup
from Elements.T3.user_page import UserElement
import time


class FundingRecordsModule(Base_Setup.BSetup):

    def test_TC_FundingRecords_01_Navigate_to_FundingRecordsPage(self):
        print("<b> Expected Results: Able to access to funding records page. </b>" + "<br>")
        UserpageActions.Access_to_Funding_Records(self)

    def test_TC_FundingRecords_02_View_DepositRecord(self):
        print("<b> Expected Results: Able to view deposit record. </b>" + "<br>")
        UserpageActions.Access_to_Funding_Records(self)
        print("<li>" + "Click on Deposit Record tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserElement.funding_record_deposit_record).click()
        time.sleep(3)
        # Assert
        deposit_record = self.driver.find_element_by_xpath(UserElement.funding_record_deposit_details).text
        self.assertNotEqual(deposit_record, "", "Deposit Record is not available.")


    def test_TC_FundingRecords_03_View_WithdrawalRecord(self):
        print("<b> Expected Results: Able to view withdrawal record. </b>" + "<br>")
        UserpageActions.Access_to_Funding_Records(self)
        print("<li>" + "Click on Withdrawal Record tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserElement.funding_record_withdrawal_record).click()
        time.sleep(3)
        # Assert

        withdrawal_record = self.driver.find_element_by_xpath(UserElement.funding_record_withdrawal_details).text
        self.assertNotEqual(withdrawal_record, "", "Withdrawal Record is not available.")




if __name__ == '__main__':
    unittest.main()
