import unittest
from Actions.T3.user_page import UserpageActions
from Setup.T3 import Base_Setup
from Elements.T3.user_page import UserElement


class DepositAreaModule(Base_Setup.BSetup):

    def test_TC_DepositArea_01_Navigate_to_DepositAreaPage(self):
        print("<b> Expected Results: Able to access to deposit area page. </b>" + "<br>")
        UserpageActions.Access_to_Deposit_Area(self)

    def test_TC_DepositArea_02_Bank_Transfer(self):
        print("<b> Expected Results: Able to perform bank transfer. </b>" + "<br>")
        UserpageActions.Access_to_Deposit_Area(self)
        print("<li>" + "Select deposit method: Public Bank" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserElement.deposit_area_deposit_method).click()
        print("<li>" + "Select deposit amount: 30" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserElement.deposit_area_deposit_amount).click()
        print("<li>" + "Click on Next Step button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(UserElement.deposit_area_next_step_button).click()
        print("<li>" + "Click on Complete the Deposit, the Next Step button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(UserElement.deposit_area_complete_deposit_button).click()


if __name__ == '__main__':
    unittest.main()
