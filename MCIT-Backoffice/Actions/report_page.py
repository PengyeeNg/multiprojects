import SetUp.Base_SetUp
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Actions.login_page import Login_Actions
from Elements.report_page import Overall_Element
from Elements.report_page import Affiliate_Element
from Elements.report_page import Cash_Flow_Element
from Elements.report_page import Merchant_Win_Loss_Element
from Elements.report_page import Merchant_Daily_Win_Loss_Element
from Elements.report_page import Outstanding_Element
from Elements.report_page import Betting_Record_Evo_Betting_Record_Element
from Elements.report_page import Betting_Record_SPA_Betting_Record_Element
from Elements.report_page import Betting_Record_Mega_Betting_Record_Element
from Elements.report_page import Betting_Record_XE88_Betting_Record_Element
from Elements.report_page import Betting_Record_Joker_Betting_Record_Element
from Elements.report_page import Betting_Record_Playtech_Betting_Record_Element
from Elements.report_page import Betting_Record_CMD_Betting_Record_Element
from Elements.report_page import Betting_Record_BG_Betting_Record_Element
from Elements.report_page import Betting_Record_IBC_Betting_Record_Element
from Elements.report_page import Betting_Record_IGS_Betting_Record_Element
from Elements.report_page import Betting_Record_M8_Betting_Record_Element
from Elements.report_page import Betting_Record_Nextspin_Betting_Record_Element
from Elements.report_page import Betting_Record_WM_Betting_Record_Element
from Elements.report_page import Report_Element
from Elements.report_page import Betting_Record_Element
from Input_Data.report_page import Report_Data
from Actions.main_page import General_Actions

class Report_Actions(SetUp.Base_SetUp.BSetUp):
    def Filter_by_Member_Name(self):
        print("<li>" + "Insert Member Name" + "</li>" + "<br>")
        self.driver.find_element_by_id(Report_Element.member_name_filter_field).send_keys(Report_Data.member_name_filter)
        print("<li>" + "Click on Search button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Report_Element.search_filter_button).click()

    def Assert_Search_results(self):
        # Verify filter results
        filtered_results = EC.text_to_be_present_in_element((By.CLASS_NAME, Report_Element.no_results_found),"No results found.")
        WebDriverWait(self.driver, 10).until(filtered_results)
        print("Expected Results: Filtered results = No results found." + "<br>")

    def View_All(self):
        # Wait till button is clickable
        wait_all_button = EC.element_to_be_clickable((By.ID, Report_Element.view_all_button))
        WebDriverWait(self.driver, 30).until(wait_all_button)
        print("<li>" + "Click on All button" + "</li>" + "<br>")
        self.driver.find_element_by_id(Report_Element.view_all_button).click()
        self.driver.implicitly_wait(30)

    def Select_Columns(self):
        print("<li>" + "Click on Select column button" + "</li>" + "<br>")
        self.driver.find_element_by_id(Report_Element.select_columns_button).click()
        # Wait till dropdown expanded
        wait_dropdown_expanded = EC.presence_of_element_located((By.CLASS_NAME, Report_Element.select_columns))
        WebDriverWait(self.driver, 10).until(wait_dropdown_expanded)
        print("<li>" + "Click on 'Select Columns'" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Report_Element.select_columns).click()


    def Export_to_HTML(self):
        print("<li>" + "Click on Export button" + "</li>" + "<br>")
        self.driver.find_element_by_id(Report_Element.export_button).click()
        # Wait till dropdown expanded
        wait_dropdown_expanded = EC.presence_of_element_located((By.CLASS_NAME, Report_Element.export_to_html))
        WebDriverWait(self.driver, 10).until(wait_dropdown_expanded)
        print("<li>" + "Click on 'HTML'" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Report_Element.export_to_html).click()
        # Wait till dialog box displayed
        wait_export_dialog_box = EC.presence_of_element_located((By.CLASS_NAME, Report_Element.export_confirmation_ok_button))
        WebDriverWait(self.driver, 10).until(wait_export_dialog_box)
        # Assert
        export_dialog_box = self.driver.find_element_by_class_name(Report_Element.export_confirmation_ok_button).is_displayed()
        self.assertTrue(export_dialog_box, "User is not able export cash flow report.")
        print("Expected Results: Export Confirmation dialog box popped out." + "<br>")


class Overall_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Overall(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Report' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Report_Element.report).click()
        overall = EC.presence_of_element_located((By.XPATH, Overall_Element.overall))
        WebDriverWait(self.driver, 10).until(overall)
        print("<li>" + "Select 'Overall'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Overall_Element.overall).click()
        overall_page = self.driver.title
        self.assertEqual(overall_page, "Overall Report", "User is not able to navigate to Overall Page.")

class Affiliate_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Affiliate(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Report' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Report_Element.report).click()
        affiliate = EC.presence_of_element_located((By.XPATH, Affiliate_Element.affiliate))
        WebDriverWait(self.driver, 10).until(affiliate)
        print("<li>" + "Select 'Affiliate'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Affiliate_Element.affiliate).click()
        affiliate_page = self.driver.title
        self.assertEqual(affiliate_page, "Overall Report", "User is not able to navigate to Affiliate Page.")

class Cash_Flow_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Cash_Flow(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Report' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Report_Element.report).click()
        cash_flow = EC.presence_of_element_located((By.XPATH, Cash_Flow_Element.cash_flow))
        WebDriverWait(self.driver, 10).until(cash_flow)
        print("<li>" + "Select 'Cash Flow'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Cash_Flow_Element.cash_flow).click()
        cash_flow_page = self.driver.title
        self.assertEqual(cash_flow_page, "Cash Flow Report", "User is not able to navigate to Cash Flow Page.")

class Merchant_Win_Loss_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Merchant_Win_loss(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Report' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Report_Element.report).click()
        merchant_win_loss = EC.presence_of_element_located((By.XPATH, Merchant_Win_Loss_Element.merchant_win_loss))
        WebDriverWait(self.driver, 10).until(merchant_win_loss)
        print("<li>" + "Select 'Merchant Win Loss'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Merchant_Win_Loss_Element.merchant_win_loss).click()
        merchant_win_loss_page = self.driver.title
        self.assertEqual(merchant_win_loss_page, "Merchant Win/Loss Report", "User is not able to navigate to Merchant Win Loss Page.")

class Merchant_Daily_Win_Loss_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Merchant_Daily_Win_Loss(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Report' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Report_Element.report).click()
        merchant_daily_win_loss = EC.presence_of_element_located((By.XPATH, Merchant_Daily_Win_Loss_Element.merchant_daily_win_loss))
        WebDriverWait(self.driver, 10).until(merchant_daily_win_loss)
        print("<li>" + "Select 'Merchant Daily Win Loss'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Merchant_Daily_Win_Loss_Element.merchant_daily_win_loss).click()
        merchant_daily_win_loss_page = self.driver.title
        self.assertEqual(merchant_daily_win_loss_page, "Merchant Daily Win/loss", "User is not able to navigate to Merchant Daily Win Loss Page.")

class Outstanding_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Outstanding(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Report' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Report_Element.report).click()
        outstanding = EC.presence_of_element_located((By.XPATH, Outstanding_Element.outstanding))
        WebDriverWait(self.driver, 10).until(outstanding)
        print("<li>" + "Select 'Outstanding'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Outstanding_Element.outstanding).click()
        outstanding_page = self.driver.title
        self.assertEqual(outstanding_page, "Outstanding Report", "User is not able to navigate to Outstanding Page.")

class Betting_Record_Actions(SetUp.Base_SetUp.BSetUp):

    def Assert_Search_results(self):
        # Verify filter results
        filtered_results = EC.text_to_be_present_in_element((By.CLASS_NAME, Betting_Record_Element.no_results_found),"No results found.")
        WebDriverWait(self.driver, 10).until(filtered_results)
        print("Expected Results: Filtered results = No results found." + "<br>")

    def View_All(self):
        # Wait till button is clickable
        wait_all_button = EC.element_to_be_clickable((By.ID, Betting_Record_Element.all_button))
        WebDriverWait(self.driver, 30).until(wait_all_button)
        print("<li>" + "Click on All button" + "</li>" + "<br>")
        self.driver.find_element_by_id(Betting_Record_Element.all_button).click()
        self.driver.implicitly_wait(30)

class Evo_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Evo(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Report' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Report_Element.report).click()
        betting_record = EC.presence_of_element_located((By.XPATH, Betting_Record_Element.betting_record))
        WebDriverWait(self.driver, 10).until(betting_record)
        print("<li>" + "Click on 'Betting Record' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Betting_Record_Element.betting_record).click()
        evo = EC.presence_of_element_located((By.XPATH, Betting_Record_Evo_Betting_Record_Element.evo))
        WebDriverWait(self.driver, 10).until(evo)
        print("<li>" + "Select 'Evo Betting Record'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Betting_Record_Evo_Betting_Record_Element.evo).click()
        evo_page = self.driver.title
        self.assertEqual(evo_page, "Evo bet", "User is not able to navigate to EVO Betting Record Page.")

class SPA_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_SPA(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Report' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Report_Element.report).click()
        betting_record = EC.presence_of_element_located((By.XPATH, Betting_Record_Element.betting_record))
        WebDriverWait(self.driver, 10).until(betting_record)
        print("<li>" + "Click on 'Betting Record' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Betting_Record_Element.betting_record).click()
        SPA = EC.presence_of_element_located((By.XPATH, Betting_Record_SPA_Betting_Record_Element.SPA))
        WebDriverWait(self.driver, 10).until(SPA)
        print("<li>" + "Select 'SPA Betting Record'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Betting_Record_SPA_Betting_Record_Element.SPA).click()
        SPA_page = self.driver.title
        self.assertEqual(SPA_page, "SPA bet", "User is not able to navigate to SPA Betting Record Page.")

class Mega_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Mega(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Report' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Report_Element.report).click()
        betting_record = EC.presence_of_element_located((By.XPATH, Betting_Record_Element.betting_record))
        WebDriverWait(self.driver, 10).until(betting_record)
        print("<li>" + "Click on 'Betting Record' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Betting_Record_Element.betting_record).click()
        mega = EC.presence_of_element_located((By.XPATH, Betting_Record_Mega_Betting_Record_Element.mega))
        WebDriverWait(self.driver, 10).until(mega)
        General_Actions.Scroll_Page_to_Bottom(self)
        print("<li>" + "Select 'MEGA Betting Record'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Betting_Record_Mega_Betting_Record_Element.mega).click()
        mega_page = self.driver.title
        self.assertEqual(mega_page, "Mega bet", "User is not able to navigate to MEGA Betting Record.")

class XE88_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_XE88(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Report' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Report_Element.report).click()
        betting_record = EC.presence_of_element_located((By.XPATH, Betting_Record_Element.betting_record))
        WebDriverWait(self.driver, 10).until(betting_record)
        print("<li>" + "Click on 'Betting Record' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Betting_Record_Element.betting_record).click()
        xe88 = EC.presence_of_element_located((By.XPATH, Betting_Record_XE88_Betting_Record_Element.XE88))
        WebDriverWait(self.driver, 10).until(xe88)
        General_Actions.Scroll_Page_to_Bottom(self)
        print("<li>" + "Select 'XE88 Betting Record'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Betting_Record_XE88_Betting_Record_Element.XE88).click()
        xe88_page = self.driver.title
        self.assertEqual(xe88_page, "Xe88", "User is not able to navigate to XE88 Betting Record.")

class Joker_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Joker(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Report' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Report_Element.report).click()
        betting_record = EC.presence_of_element_located((By.XPATH, Betting_Record_Element.betting_record))
        WebDriverWait(self.driver, 10).until(betting_record)
        print("<li>" + "Click on 'Betting Record' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Betting_Record_Element.betting_record).click()
        joker = EC.presence_of_element_located((By.XPATH, Betting_Record_Joker_Betting_Record_Element.joker))
        WebDriverWait(self.driver, 10).until(joker)
        General_Actions.Scroll_Page_to_Bottom(self)
        print("<li>" + "Select 'Joker Betting Record'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Betting_Record_Joker_Betting_Record_Element.joker).click()
        joker_page = self.driver.title
        self.assertEqual(joker_page, "Joker", "User is not able to navigate to JOKER Betting Record Page.")

class Playtech_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Playtech(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Report' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Report_Element.report).click()
        betting_record = EC.presence_of_element_located((By.XPATH, Betting_Record_Element.betting_record))
        WebDriverWait(self.driver, 10).until(betting_record)
        print("<li>" + "Click on 'Betting Record' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Betting_Record_Element.betting_record).click()
        playtech = EC.presence_of_element_located((By.XPATH, Betting_Record_Playtech_Betting_Record_Element.playtech))
        WebDriverWait(self.driver, 10).until(playtech)
        General_Actions.Scroll_Page_to_Bottom(self)
        print("<li>" + "Select 'Playtech Betting Record'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Betting_Record_Playtech_Betting_Record_Element.playtech).click()
        playtech_page = self.driver.title
        self.assertEqual(playtech_page, "Playtech", "User is not able to navigate to PLAYTECH Betting Record Page.")

class CMD_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_CMD(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Report' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Report_Element.report).click()
        betting_record = EC.presence_of_element_located((By.XPATH, Betting_Record_Element.betting_record))
        WebDriverWait(self.driver, 10).until(betting_record)
        print("<li>" + "Click on 'Betting Record' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Betting_Record_Element.betting_record).click()
        cmd = EC.presence_of_element_located((By.XPATH, Betting_Record_CMD_Betting_Record_Element.CMD))
        WebDriverWait(self.driver, 10).until(cmd)
        General_Actions.Scroll_Page_to_Bottom(self)
        print("<li>" + "Select 'CMD Betting Record'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Betting_Record_CMD_Betting_Record_Element.CMD).click()
        cmd_page = self.driver.title
        self.assertEqual(cmd_page, "Cmd", "User is not able to navigate to CMD Betting Record Page.")

class BG_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_BG(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Report' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Report_Element.report).click()
        betting_record = EC.presence_of_element_located((By.XPATH, Betting_Record_Element.betting_record))
        WebDriverWait(self.driver, 10).until(betting_record)
        print("<li>" + "Click on 'Betting Record' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Betting_Record_Element.betting_record).click()
        bg = EC.presence_of_element_located((By.XPATH, Betting_Record_BG_Betting_Record_Element.BG))
        WebDriverWait(self.driver, 10).until(bg)
        General_Actions.Scroll_Page_to_Bottom(self)
        print("<li>" + "Select 'BG Betting Record'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Betting_Record_BG_Betting_Record_Element.BG).click()
        bg_page = self.driver.title
        self.assertEqual(bg_page, "Bg", "User is not able to navigate to BG Betting Record Page.")

class IBC_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_IBC(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Report' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Report_Element.report).click()
        betting_record = EC.presence_of_element_located((By.XPATH, Betting_Record_Element.betting_record))
        WebDriverWait(self.driver, 10).until(betting_record)
        print("<li>" + "Click on 'Betting Record' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Betting_Record_Element.betting_record).click()
        ibc = EC.presence_of_element_located((By.XPATH, Betting_Record_IBC_Betting_Record_Element.IBC))
        WebDriverWait(self.driver, 10).until(ibc)
        General_Actions.Scroll_Page_to_Bottom(self)
        print("<li>" + "Select 'IBC Betting Record'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Betting_Record_IBC_Betting_Record_Element.IBC).click()
        ibc_page = self.driver.title
        self.assertEqual(ibc_page, "Ibc", "User is not able to navigate to IBC Betting Record Page.")

class IGS_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_IGS(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Report' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Report_Element.report).click()
        betting_record = EC.presence_of_element_located((By.XPATH, Betting_Record_Element.betting_record))
        WebDriverWait(self.driver, 10).until(betting_record)
        print("<li>" + "Click on 'Betting Record' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Betting_Record_Element.betting_record).click()
        igs = EC.presence_of_element_located((By.XPATH, Betting_Record_IGS_Betting_Record_Element.IGS))
        WebDriverWait(self.driver, 10).until(igs)
        General_Actions.Scroll_Page_to_Bottom(self)
        print("<li>" + "Select 'IGS Betting Record'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Betting_Record_IGS_Betting_Record_Element.IGS).click()
        igs_page = self.driver.title
        self.assertEqual(igs_page, "Igs", "User is not able to navigate to IGS Betting record Page.")

class M8_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_M8(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Report' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Report_Element.report).click()
        betting_record = EC.presence_of_element_located((By.XPATH, Betting_Record_Element.betting_record))
        WebDriverWait(self.driver, 10).until(betting_record)
        print("<li>" + "Click on 'Betting Record' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Betting_Record_Element.betting_record).click()
        M8 = EC.presence_of_element_located((By.XPATH, Betting_Record_M8_Betting_Record_Element.M8))
        WebDriverWait(self.driver, 10).until(M8)
        General_Actions.Scroll_Page_to_Bottom(self)
        print("<li>" + "Select 'M8 Betting Record'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Betting_Record_M8_Betting_Record_Element.M8).click()
        M8_page = self.driver.title
        self.assertEqual(M8_page, "M8", "User is not able to navigate to M8 Betting Recoord Page.")

class Nextspin_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Nextspin(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Report' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Report_Element.report).click()
        betting_record = EC.presence_of_element_located((By.XPATH, Betting_Record_Element.betting_record))
        WebDriverWait(self.driver, 10).until(betting_record)
        print("<li>" + "Click on 'Betting Record' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Betting_Record_Element.betting_record).click()
        nextspin = EC.presence_of_element_located((By.XPATH, Betting_Record_Nextspin_Betting_Record_Element.nextspin))
        WebDriverWait(self.driver, 10).until(nextspin)
        General_Actions.Scroll_Page_to_Bottom(self)
        print("<li>" + "Select 'NEXTSPIN Betting Record'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Betting_Record_Nextspin_Betting_Record_Element.nextspin).click()
        nextspin_page = self.driver.title
        self.assertEqual(nextspin_page, "Nextspin", "User is not able to navigate to NEXTSPIN Betting Record Page.")

class WM_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_WM(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Report' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Report_Element.report).click()
        betting_record = EC.presence_of_element_located((By.XPATH, Betting_Record_Element.betting_record))
        WebDriverWait(self.driver, 10).until(betting_record)
        print("<li>" + "Click on 'Betting Record' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Betting_Record_Element.betting_record).click()
        wm = EC.presence_of_element_located((By.XPATH, Betting_Record_WM_Betting_Record_Element.WM))
        WebDriverWait(self.driver, 10).until(wm)
        General_Actions.Scroll_Page_to_Bottom(self)
        print("<li>" + "Select 'WM Betting Record'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Betting_Record_WM_Betting_Record_Element.WM).click()
        wm_page = self.driver.title
        self.assertEqual(wm_page, "Wm", "User is not able to navigate to WM Betting Record Page.")