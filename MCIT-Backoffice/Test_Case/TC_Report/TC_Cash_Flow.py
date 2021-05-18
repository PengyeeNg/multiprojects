import unittest
import SetUp.Base_SetUp
from Actions.report_page import Cash_Flow_Actions
from Actions.report_page import Report_Actions
from Elements.report_page import Cash_Flow_Element


class Cash_Flow(SetUp.Base_SetUp.BSetUp):

    def test_TC_Cash_Flow_01_Filter_Cash_Flow_Report(self):
        Cash_Flow_Actions.Navigate_Cash_Flow(self)
        Report_Actions.Filter_by_Member_Name(self)
        Report_Actions.Assert_Search_results(self)

    def test_TC_Cash_Flow_02_View_All_Cash_Flow_Report(self):
        Cash_Flow_Actions.Navigate_Cash_Flow(self)
        Report_Actions.View_All(self)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Cash Flow Report", "Page breaks after clicking Search button.")
        print("Expected Results: Page does not break after clicking Search button." + "<br>")

    def test_TC_Cash_Flow_03_Select_Columns_Cash_Flow_Report(self):
        Cash_Flow_Actions.Navigate_Cash_Flow(self)
        Report_Actions.Select_Columns(self)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Cash Flow Report", "Page breaks after clicking Select Columns.")
        print("Expected Results: Page does not break after clicking Select Columns." + "<br>")

    def test_TC_Cash_Flow_04_Export_Cash_Flow_Report(self):
        Cash_Flow_Actions.Navigate_Cash_Flow(self)
        Report_Actions.Export_to_HTML(self)

    def test_TC_Cash_Flow_05_Table_Sorting_Cash_Flow_Report(self):
        Cash_Flow_Actions.Navigate_Cash_Flow(self)
        print("<li>" + "Click on Username header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Cash_Flow_Element.username_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Third Party Game Betting Amount header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Cash_Flow_Element.third_party_game_betting_amount_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Third Party Game Win Lose header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Cash_Flow_Element.third_party_game_win_lose_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Third Party Game Rebate header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Cash_Flow_Element.third_party_game_rebate_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Manual Deposit header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Cash_Flow_Element.manual_deposit_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Manual Deduct header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Cash_Flow_Element.manual_deduct_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Manual Bonus header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Cash_Flow_Element.manual_bonus_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Manual Withdrawal header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Cash_Flow_Element.manual_withdrawal_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Overall Affiliate Withdrawal Amount header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Cash_Flow_Element.overall_affiliate_withdrawal_amount_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Overall Online Topup Amount header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Cash_Flow_Element.overall_online_topup_amount_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Overall Deposit Amount header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Cash_Flow_Element.overall_deposit_amount_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Overall Topup Bonus Amount header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Cash_Flow_Element.overall_topup_bonus_amount_header_sorting).click()
        self.driver.implicitly_wait(30)
        # Move the slidebar
        slide_bar = self.driver.find_element_by_xpath(Cash_Flow_Element.slide_bar)
        self.driver.execute_script("arguments[0].scrollIntoView();", slide_bar)
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Overall Registration Bonus Amount header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Cash_Flow_Element.overall_registration_bonus_amount_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Overall Withdrawal Amount header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Cash_Flow_Element.overall_withdrawal_amount_header_sorting).click()
        self.driver.implicitly_wait(30)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Cash Flow Report", "Page breaks after clicking table sorting.")
        print("Expected Results: Page does not break after clicking table sorting." + "<br>")


if __name__ == '__main__':
    unittest.main()
