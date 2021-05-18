import unittest
from Actions.T3.user_page import UserpageActions
from Setup.T3 import Base_Setup
from Elements.T3.user_page import UserElement
import time


class MemberAgentModule(Base_Setup.BSetup):

    def test_TC_MemberAgent_01_Navigate_to_MemberAgentPage(self):
        print("<b> Expected Results: Able to access to member agent page. </b>" + "<br>")
        UserpageActions.Access_to_Member_Agent(self)

    def test_TC_MemberAgent_02_View_MemberDetails(self):
        print("<b> Expected Results: Able to view member details. </b>" + "<br>")
        UserpageActions.Access_to_Member_Agent(self)
        print("<li>" + "Click on Member Details tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserElement.member_agent_member_detail).click()
        time.sleep(3)
        # Assert
        member_detail = self.driver.find_element_by_xpath(UserElement.member_agent_member_detail_element).text
        self.assertNotEqual(member_detail, "", "Member detail is not available.")


    def test_TC_MemberAgent_03_View_DetailReport(self):
        print("<b> Expected Results: Able to view detail report. </b>" + "<br>")
        UserpageActions.Access_to_Member_Agent(self)
        print("<li>" + "Click on Detail Report tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserElement.member_agent_detail_report).click()
        time.sleep(3)
        # Assert
        detail_report = self.driver.find_element_by_xpath(UserElement.member_agent_detail_report_element).is_displayed()
        self.assertTrue(detail_report, "Detail Report is not available.")

    def test_TC_MemberAgent_04_View_BettingRecord(self):
        print("<b> Expected Results: Able to view betting record. </b>" + "<br>")
        UserpageActions.Access_to_Member_Agent(self)
        print("<li>" + "Click on Betting Record tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserElement.member_agent_betting_record).click()
        time.sleep(3)
        # Assert
        betting_record = self.driver.find_element_by_xpath(UserElement.member_agent_betting_record_element).text
        self.assertNotEqual(betting_record, "", "Betting Record is not available.")



if __name__ == '__main__':
    unittest.main()
