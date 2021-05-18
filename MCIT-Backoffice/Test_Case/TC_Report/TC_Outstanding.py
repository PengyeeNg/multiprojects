import unittest
import SetUp.Base_SetUp
from Actions.report_page import Outstanding_Actions
from Actions.report_page import Report_Actions
from Elements.report_page import Outstanding_Element
from Elements.report_page import Report_Element
from Input_Data.report_page import Report_Data
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class Outstanding(SetUp.Base_SetUp.BSetUp):

    def test_TC_Outstanding_01_Filter_Outstanding_Report(self):
        Outstanding_Actions.Navigate_Outstanding(self)
        print("<li>" + "Insert Member Name" + "</li>" + "<br>")
        self.driver.find_element_by_id(Outstanding_Element.username_filter_field).send_keys(Report_Data.member_name_filter)
        print("<li>" + "Click on Search button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Report_Element.search_filter_button).click()
        Report_Actions.Assert_Search_results(self)

    def test_TC_Outstanding_02_View_All_Outstanding_Report(self):
        Outstanding_Actions.Navigate_Outstanding(self)
        wait_all_button = EC.element_to_be_clickable((By.ID, Outstanding_Element.view_all_button))
        WebDriverWait(self.driver, 30).until(wait_all_button)
        print("<li>" + "Click on All button" + "</li>" + "<br>")
        self.driver.find_element_by_id(Outstanding_Element.view_all_button).click()
        self.driver.implicitly_wait(30)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Outstanding Report", "Page breaks after clicking Search button.")
        print("Expected Results: Page does not break after clicking Search button." + "<br>")

    def test_TC_Outstanding_03_Table_Sorting_Outstanding_Report(self):
        Outstanding_Actions.Navigate_Outstanding(self)
        print("<li>" + "Click on ID header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.id_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Source Name header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.source_name_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Reference No header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.reference_no_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Soc Trans ID header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.soc_trans_id_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Is First Half header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.is_first_half_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Trans Date header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.trans_date_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Is Home Give header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.is_home_give_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Is Bet Home header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.is_bet_home_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Bet Amount header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.bet_amount_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Outstanding header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.outstanding_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Hdp header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.hdp_header_sorting).click()
        self.driver.implicitly_wait(30)
        # Move the slidebar
        slide_bar_01 = self.driver.find_element_by_xpath(Outstanding_Element.slide_bar_01)
        self.driver.execute_script("arguments[0].scrollIntoView();", slide_bar_01)
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Odds header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.odds_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Currency header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.currency_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Win Amount header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.win_amount_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Exchange Rate header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.exchange_rate_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Win Lose Status header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.win_lose_status_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Trans Type header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.trans_type_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Danger Status header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.danger_status_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Mem Commission Set header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.mem_commission_set_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Mem Commission header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.mem_commission_header_sorting).click()
        self.driver.implicitly_wait(30)
        # Move the slidebar
        slide_bar_02 = self.driver.find_element_by_xpath(Outstanding_Element.slide_bar_02)
        self.driver.execute_script("arguments[0].scrollIntoView();", slide_bar_02)
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Bet Ip header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.bet_ip_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Home Score header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.home_score_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Away Score header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.away_score_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Run Home Score header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.run_home_score_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Run Away Score header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.run_away_score_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Is Running header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.is_running_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Reject Reason header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.reject_reason_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Sort Type header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.sort_type_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Choice header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.choice_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Working Date header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.working_date_header_sorting).click()
        self.driver.implicitly_wait(30)
        # Move the slidebar
        slide_bar_03 = self.driver.find_element_by_xpath(Outstanding_Element.slide_bar_03)
        self.driver.execute_script("arguments[0].scrollIntoView();", slide_bar_03)
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Odds Type header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.odds_type_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Match Date header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.match_date_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Home Team ID header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.home_team_id_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Away Team ID header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.away_team_id_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Special ID header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.special_id_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Is Cash Out header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.is_cash_out_header_sorting).click()
        self.driver.implicitly_wait(30)
        # print("<li>" + "Click on Cash Out Total header" + "</li>" + "<br>")
        # self.driver.find_element_by_xpath(Outstanding_Element.cash_out_total_header_sorting).click()
        # self.driver.implicitly_wait(30)
        print("<li>" + "Click on Cash Out Take Back header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.cash_out_take_back_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Cash Out Win Lose header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.cash_out_win_lose_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Bet Source header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.bet_source_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Status Change header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.status_change_header_sorting).click()
        self.driver.implicitly_wait(30)
        # Move the slidebar
        slide_bar_04 = self.driver.find_element_by_xpath(Outstanding_Element.slide_bar_04)
        self.driver.execute_script("arguments[0].scrollIntoView();", slide_bar_04)
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on State Update Ts header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.state_update_ts_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Aos Excluding header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.aos_excluding_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Mmr Percent header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.mmr_percent_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Bet Remarks header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.bet_remarks_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Is Special header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.is_special_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Created Time header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.created_time_header_sorting).click()
        self.driver.implicitly_wait(30)
        # Move the slidebar
        slide_bar_05 = self.driver.find_element_by_xpath(Outstanding_Element.slide_bar_05)
        self.driver.execute_script("arguments[0].scrollIntoView();", slide_bar_05)
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Cash Out Total header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.cash_out_total_header_sorting).click()
        self.driver.implicitly_wait(30)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Outstanding Report", "Page breaks after clicking table sorting.")
        print("Expected Results: Page does not break after clicking table sorting." + "<br>")


if __name__ == '__main__':
    unittest.main()
