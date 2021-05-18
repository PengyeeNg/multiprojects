import unittest
from Setup.T4 import Base_Setup
from Elements.T4.user_page import UserpageElement
from Actions.T4.login_page import LoginpageActions
from Actions.T4.user_page import UserActions
import time


class UserReferrerModule(Base_Setup.BSetup):

    def test_TC_Referrer_01_View_Member_List(self):
        print("<b> Expected Results: Able to view member list. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        UserActions.Access_to_Referrer(self)
        print("<li>" + "Click on Member List tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserpageElement.member_list_tab).click()
        time.sleep(3)
        # Assert
        member_detail = self.driver.find_element_by_xpath(UserpageElement.member_list_details).text
        self.assertNotEqual(member_detail, "", "Member detail is not available.")

    def test_TC_Referrer_02_View_Bet_Record(self):
        print("<b> Expected Results: Able to view bet record. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        UserActions.Access_to_Referrer(self)
        print("<li>" + "Click on Bet Record tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserpageElement.bet_record_tab).click()
        time.sleep(3)
        # Assert
        bet_detail = self.driver.find_element_by_xpath(UserpageElement.bet_record_details).text
        self.assertNotEqual(bet_detail, "", "Bet Record is not available.")

    def test_TC_Referrer_03_View_Report(self):
        print("<b> Expected Results: Able to view report. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        UserActions.Access_to_Referrer(self)
        print("<li>" + "Click on Report tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserpageElement.report_tab).click()
        time.sleep(3)
        # Assert
        report_detail = self.driver.find_element_by_class_name(UserpageElement.report_details).is_displayed()
        self.assertTrue(report_detail, "Report is not available.")


if __name__ == '__main__':
    unittest.main()
