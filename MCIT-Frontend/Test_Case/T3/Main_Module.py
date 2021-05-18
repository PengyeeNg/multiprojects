import unittest
from Elements.T3.main_page import MainpageElement
from Setup.T3 import Base_Setup
from Actions.T3.main_page import MainpageActions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class MainModule(Base_Setup.BSetup):

    def test_TC_Main_01_Navigate_to_Main_Page(self):
        print("<b> Expected Results: Able to access to main page without breaking. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)

    def test_TC_Main_02_Navigate_to_AboutUs(self):
        print("<b> Expected Results: Able to access to About Us without breaking. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Scroll_to_Main_Page_Bottom(self)
        print("<li>" + "Click on About Us" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.about_us_link).click()
        # Wait page loads
        wait_page_load = EC.presence_of_element_located((By.XPATH, MainpageElement.bottom_link_title))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        # assert self.driver.find_element_by_css_selector(MainpageElement.bottom_link_title).text == "本地化".decode().encode('utf-8')
        link_title = self.driver.find_element_by_xpath(MainpageElement.bottom_link_title).is_displayed()
        # about_us = "关于我们".decode('utf-8')
        self.assertTrue(link_title, "User is not able to access to About Us.")

    def test_TC_Main_03_Navigate_to_MobileBetting(self):
        print("<b> Expected Results: Able to access to Mobile Betting without breaking. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Scroll_to_Main_Page_Bottom(self)
        print("<li>" + "Click on Mobile Betting" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.mobile_betting_link).click()
        # Wait page loads
        wait_page_load = EC.visibility_of_element_located((By.CLASS_NAME, MainpageElement.mobile_betting_qr))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        mobile_betting_qr = self.driver.find_element_by_class_name(MainpageElement.mobile_betting_qr).is_displayed()
        self.assertTrue(mobile_betting_qr, "User is not able to access to Mobile Betting.")

    def test_TC_Main_04_Navigate_to_FAQ(self):
        print("<b> Expected Results: Able to access to FAQ without breaking. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Scroll_to_Main_Page_Bottom(self)
        print("<li>" + "Click on FAQ" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.faq_link).click()
        # Wait page loads
        wait_page_load = EC.presence_of_element_located((By.XPATH, MainpageElement.bottom_link_title))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        link_title = self.driver.find_element_by_xpath(MainpageElement.bottom_link_title).is_displayed()
        self.assertTrue(link_title, "User is not able to access to FAQ.")

    def test_TC_Main_05_Navigate_to_DepositHelp(self):
        print("<b> Expected Results: Able to access to Deposit Help without breaking. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Scroll_to_Main_Page_Bottom(self)
        print("<li>" + "Click on Deposite Help" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.deposit_help_link).click()
        # Wait page loads
        wait_page_load = EC.presence_of_element_located((By.XPATH, MainpageElement.bottom_link_title))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        link_title = self.driver.find_element_by_xpath(MainpageElement.bottom_link_title).is_displayed()
        self.assertTrue(link_title, "User is not able to access to Deposit Help.")

    def test_TC_Main_06_Navigate_to_WithdrawalHelp(self):
        print("<b> Expected Results: Able to access to Withdrawal Help without breaking. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Scroll_to_Main_Page_Bottom(self)
        print("<li>" + "Click on Withdrawal Help" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.withdrawal_help_link).click()
        # Wait page loads
        wait_page_load = EC.presence_of_element_located((By.XPATH, MainpageElement.bottom_link_title))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        link_title = self.driver.find_element_by_xpath(MainpageElement.bottom_link_title).is_displayed()
        self.assertTrue(link_title, "User is not able to access to Withdrawal Help.")

    def test_TC_Main_07_Access_to_LatestAnnouncement(self):
        print("<b> Expected Results: Able to access to the latest announcement via main page </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        print("<li>" + "Click on marquee announcement" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(MainpageElement.marquee_announcement).click()
        # Wait page loads
        wait_announcement_load = EC.element_to_be_clickable((By.CLASS_NAME, MainpageElement.marquee_announcement_modal))
        WebDriverWait(self.driver, 20).until(wait_announcement_load)
        announcement_modal = self.driver.find_element_by_class_name(MainpageElement.marquee_announcement_modal).is_displayed()
        self.assertTrue(announcement_modal, "User is not able to access to Latest Announcement.")

    def test_TC_Main_08_Access_to_AboutUsDetails(self):
        print("<b> Expected Results: Able to access to About Us details. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Scroll_to_Main_Page_Bottom(self)
        print("<li>" + "Click on About Us" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.about_us_link).click()
        # Wait page loads
        wait_page_load = EC.presence_of_element_located((By.XPATH, MainpageElement.about_us_details))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        about_us_details = self.driver.find_element_by_xpath(MainpageElement.about_us_details).text
        self.assertNotEqual(about_us_details, "", "Unable to read About Us Details")

    def test_TC_Main_09_Access_to_FAQDetails(self):
        print("<b> Expected Results: Able to access to FAQ details. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Scroll_to_Main_Page_Bottom(self)
        print("<li>" + "Click on About Us" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.about_us_link).click()
        print("<li>" + "Click on FAQ from the side bar" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.faq_button).click()
        # Wait page loads
        wait_page_load = EC.presence_of_element_located((By.XPATH, MainpageElement.faq_details))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        faq_details = self.driver.find_element_by_xpath(MainpageElement.faq_details).text
        self.assertNotEqual(faq_details, "", "Unable to read FAQ Details")

    def test_TC_Main_10_Access_to_LoginRegistrationDetails(self):
        print("<b> Expected Results: Able to access to Login and Registration details. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Scroll_to_Main_Page_Bottom(self)
        print("<li>" + "Click on About Us" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.about_us_link).click()
        print("<li>" + "Click on Login and Registration from the side bar" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.loginNregistration_button).click()
        # Wait page loads
        wait_page_load = EC.presence_of_element_located((By.XPATH, MainpageElement.loginNregistration_details))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        loginregistration_details = self.driver.find_element_by_xpath(MainpageElement.loginNregistration_details).text
        self.assertNotEqual(loginregistration_details, "", "Unable to read Login and Registration Details")

    def test_TC_Main_11_Access_to_BasicTermsDetails(self):
        print("<b> Expected Results: Able to access to Basic Terms details. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Scroll_to_Main_Page_Bottom(self)
        print("<li>" + "Click on About Us" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.about_us_link).click()
        print("<li>" + "Click on Basic Terms from the side bar" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.basic_term_button).click()
        # Wait page loads
        wait_page_load = EC.presence_of_element_located((By.XPATH, MainpageElement.basic_term_details))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        basicterms_details = self.driver.find_element_by_xpath(MainpageElement.basic_term_details).text
        self.assertNotEqual(basicterms_details, "", "Unable to read Login and Registration Details")

    def test_TC_Main_12_Access_to_DepositProcessDetails(self):
        print("<b> Expected Results: Able to access to Deposit Process details. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Scroll_to_Main_Page_Bottom(self)
        print("<li>" + "Click on About Us" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.about_us_link).click()
        print("<li>" + "Click on Deposit Process from the side bar" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.deposit_process_button).click()
        # Wait page loads
        wait_page_load = EC.presence_of_element_located((By.XPATH, MainpageElement.deposit_process_details))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        depositprocess_details = self.driver.find_element_by_xpath(MainpageElement.deposit_process_details).text
        self.assertNotEqual(depositprocess_details, "", "Unable to read Deposit Process Details")

    def test_TC_Main_13_Access_to_QuickDepositDetails(self):
        print("<b> Expected Results: Able to access to Quick Deposit details. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Scroll_to_Main_Page_Bottom(self)
        print("<li>" + "Click on About Us" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.about_us_link).click()
        print("<li>" + "Click on Deposit Process from the side bar" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.deposit_process_button).click()
        print("<li>" + "Click on Quick Deposit from the tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.quick_deposit_tab).click()
        # Wait page loads
        wait_page_load = EC.presence_of_element_located((By.XPATH, MainpageElement.quick_deposit_details))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        quickdeposit_details = self.driver.find_element_by_xpath(MainpageElement.quick_deposit_details).text
        self.assertNotEqual(quickdeposit_details, "", "Unable to read Quick Deposit Details")

    def test_TC_Main_14_Access_to_OnlineBankingDetails(self):
        print("<b> Expected Results: Able to access to Online Banking details. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Scroll_to_Main_Page_Bottom(self)
        print("<li>" + "Click on About Us" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.about_us_link).click()
        print("<li>" + "Click on Deposit Process from the side bar" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.deposit_process_button).click()
        print("<li>" + "Click on Online Banking from the tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.online_banking_tab).click()
        # Wait page loads
        wait_page_load = EC.presence_of_element_located((By.XPATH, MainpageElement.online_banking_details))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        onlinebanking_details = self.driver.find_element_by_xpath(MainpageElement.online_banking_details).text
        self.assertNotEqual(onlinebanking_details, "", "Unable to read Online Banking Details")

    def test_TC_Main_15_Access_to_AlipayScancodeDetails(self):
        print("<b> Expected Results: Able to access to Alipay Scancode details. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Scroll_to_Main_Page_Bottom(self)
        print("<li>" + "Click on About Us" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.about_us_link).click()
        print("<li>" + "Click on Deposit Process from the side bar" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.deposit_process_button).click()
        print("<li>" + "Click on Alipay Scancode from the tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.alipay_scancode_tab).click()
        # Wait page loads
        wait_page_load = EC.presence_of_element_located((By.XPATH, MainpageElement.alipay_scancode_details))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        alipay_details = self.driver.find_element_by_xpath(MainpageElement.alipay_scancode_details).text
        self.assertNotEqual(alipay_details, "", "Unable to read Alipay Scancode Details")

    def test_TC_Main_16_Access_to_WechatScancodeDetails(self):
        print("<b> Expected Results: Able to access to Wechat Scancode details. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Scroll_to_Main_Page_Bottom(self)
        print("<li>" + "Click on About Us" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.about_us_link).click()
        print("<li>" + "Click on Deposit Process from the side bar" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.deposit_process_button).click()
        print("<li>" + "Click on Wechat Scancode from the tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.wechat_scancode_tab).click()
        # Wait page loads
        wait_page_load = EC.presence_of_element_located((By.XPATH, MainpageElement.wechat_scancode_details))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        alipay_details = self.driver.find_element_by_xpath(MainpageElement.wechat_scancode_details).text
        self.assertNotEqual(alipay_details, "", "Unable to read Wechat Scancode Details")

    def test_TC_Main_17_Access_to_WithdrawalCommonQuestionDetails(self):
        print("<b> Expected Results: Able to access to Withdrawal Common Question details. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Scroll_to_Main_Page_Bottom(self)
        print("<li>" + "Click on About Us" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.about_us_link).click()
        print("<li>" + "Click on Withdrawal Process from the side bar" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.withdrawal_process_button).click()
        # Wait page loads
        wait_page_load = EC.presence_of_element_located((By.XPATH, MainpageElement.withdrawal_process_details))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        alipay_details = self.driver.find_element_by_xpath(MainpageElement.withdrawal_process_details).text
        self.assertNotEqual(alipay_details, "", "Unable to read Withdrawal Common Question Details")

    def test_TC_Main_18_Access_to_WithdrawalProcessDetails(self):
        print("<b> Expected Results: Able to access to Withdrawal Process details. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Scroll_to_Main_Page_Bottom(self)
        print("<li>" + "Click on About Us" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.about_us_link).click()
        print("<li>" + "Click on Withdrawal Process from the side bar" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.withdrawal_process_button).click()
        print("<li>" + "Click on Withdrawal Process from the tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.withdrawal_process_tab).click()
        # Wait page loads
        wait_page_load = EC.presence_of_element_located((By.XPATH, MainpageElement.withdrawal_process_tab_details))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        alipay_details = self.driver.find_element_by_xpath(MainpageElement.withdrawal_process_tab_details).text
        self.assertNotEqual(alipay_details, "", "Unable to read Withdrawal Process Details")

    def test_TC_Main_19_Access_to_TransferHelpDetails(self):
        print("<b> Expected Results: Able to access to Transfer Help details. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Scroll_to_Main_Page_Bottom(self)
        print("<li>" + "Click on About Us" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.about_us_link).click()
        print("<li>" + "Click on Transfer Process from the side bar" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.moneytransfer_process_button).click()
        # Wait page loads
        wait_page_load = EC.presence_of_element_located((By.XPATH, MainpageElement.moneytransfer_process_details))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        alipay_details = self.driver.find_element_by_xpath(MainpageElement.moneytransfer_process_details).text
        self.assertNotEqual(alipay_details, "", "Unable to read Transfer Help Details")

    def test_TC_Main_20_Access_to_TransferProcessDetails(self):
        print("<b> Expected Results: Able to access to Transfer Process details. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Scroll_to_Main_Page_Bottom(self)
        print("<li>" + "Click on About Us" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.about_us_link).click()
        print("<li>" + "Click on Transfer Process from the side bar" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.moneytransfer_process_button).click()
        print("<li>" + "Click on Transfer Process from the tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.moneytransfer_process_tab).click()
        # Wait page loads
        wait_page_load = EC.presence_of_element_located((By.XPATH, MainpageElement.moneytransfer_process_tab_details))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        alipay_details = self.driver.find_element_by_xpath(MainpageElement.moneytransfer_process_tab_details).text
        self.assertNotEqual(alipay_details, "", "Unable to read Transfer Process Details")

    def test_TC_Main_21_Access_to_AccountSecurityDetails(self):
        print("<b> Expected Results: Able to access to Account Security details. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Scroll_to_Main_Page_Bottom(self)
        print("<li>" + "Click on About Us" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.about_us_link).click()
        print("<li>" + "Click on Account Security from the side bar" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.account_security_button).click()
        # Wait page loads
        wait_page_load = EC.presence_of_element_located((By.XPATH, MainpageElement.account_security_details))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        alipay_details = self.driver.find_element_by_xpath(MainpageElement.account_security_details).text
        self.assertNotEqual(alipay_details, "", "Unable to read Transfer Help Details")

    def test_TC_Main_22_Access_to_BettingRulesandRegulationDetails(self):
        print("<b> Expected Results: Able to access to Betting Rules and Regulation details. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Scroll_to_Main_Page_Bottom(self)
        print("<li>" + "Click on About Us" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.about_us_link).click()
        print("<li>" + "Click on Account Security from the side bar" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.account_security_button).click()
        print("<li>" + "Click on Betting Rules and Regulation from the tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.betting_rulesandregulation_tab).click()
        # Wait page loads
        wait_page_load = EC.presence_of_element_located((By.XPATH, MainpageElement.betting_rulesandregulation_details))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        alipay_details = self.driver.find_element_by_xpath(MainpageElement.betting_rulesandregulation_details).text
        self.assertNotEqual(alipay_details, "", "Unable to read Betting Rules and Regulation Details")

    def test_TC_Main_23_Access_to_BettingResponsibilityDetails(self):
        print("<b> Expected Results: Able to access to Betting Responsibility details. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Scroll_to_Main_Page_Bottom(self)
        print("<li>" + "Click on About Us" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.about_us_link).click()
        print("<li>" + "Click on Account Security from the side bar" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.account_security_button).click()
        print("<li>" + "Click on Betting Responsibility from the tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.betting_responsibility_tab).click()
        # Wait page loads
        wait_page_load = EC.presence_of_element_located((By.XPATH, MainpageElement.betting_responsibility_details))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        alipay_details = self.driver.find_element_by_xpath(MainpageElement.betting_responsibility_details).text
        self.assertNotEqual(alipay_details, "", "Unable to read Betting Responsibility Details")

    def test_TC_Main_24_Access_to_RulesandRegulationDetails(self):
        print("<b> Expected Results: Able to access to Rules and Regulation details. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Scroll_to_Main_Page_Bottom(self)
        print("<li>" + "Click on About Us" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.about_us_link).click()
        print("<li>" + "Click on Account Security from the side bar" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.account_security_button).click()
        print("<li>" + "Click on Rules and Regulation from the tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.rulesandregulation_tab).click()
        # Wait page loads
        wait_page_load = EC.presence_of_element_located((By.XPATH, MainpageElement.rulesandregulation_details))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        alipay_details = self.driver.find_element_by_xpath(MainpageElement.rulesandregulation_details).text
        self.assertNotEqual(alipay_details, "", "Unable to read Rules and Regulation Details")

    def test_TC_Main_25_Access_to_AccountPrivacyAgreementDetails(self):
        print("<b> Expected Results: Able to access to Account Privacy Agreement details. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Scroll_to_Main_Page_Bottom(self)
        print("<li>" + "Click on About Us" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.about_us_link).click()
        print("<li>" + "Click on Account Security from the side bar" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.account_security_button).click()
        print("<li>" + "Click on Account Privacy and Agreement from the tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.user_privacy_agreement_tab).click()
        # Wait page loads
        wait_page_load = EC.presence_of_element_located((By.XPATH, MainpageElement.user_privacy_agreement_details))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        alipay_details = self.driver.find_element_by_xpath(MainpageElement.user_privacy_agreement_details).text
        self.assertNotEqual(alipay_details, "", "Unable to read Account Privacy and Agreement Details")

    def test_TC_Main_26_Access_to_OnlineProblemDetails(self):
        print("<b> Expected Results: Able to access to Online Problem details. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Scroll_to_Main_Page_Bottom(self)
        print("<li>" + "Click on About Us" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.about_us_link).click()
        print("<li>" + "Click on Online Problem from the side bar" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.online_problem_button).click()
        # Wait page loads
        wait_page_load = EC.presence_of_element_located((By.XPATH, MainpageElement.online_problem_details))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        alipay_details = self.driver.find_element_by_xpath(MainpageElement.online_problem_details).text
        self.assertNotEqual(alipay_details, "", "Unable to read Online Problem Details")

    def TC_Main_27_Access_to_AgencyCooperationDetails(self):
        print("<b> Expected Results: Able to access to Agency Cooperation details. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Scroll_to_Main_Page_Bottom(self)
        print("<li>" + "Click on About Us" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.about_us_link).click()
        print("<li>" + "Click on Agency Cooperation from the side bar" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.agency_cooperation_button).click()
        # Wait page loads
        wait_page_load = EC.presence_of_element_located((By.XPATH, MainpageElement.agency_cooperation_details))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        alipay_details = self.driver.find_element_by_xpath(MainpageElement.agency_cooperation_details).text
        self.assertNotEqual(alipay_details, "", "Unable to read Agency Cooperation Details")


if __name__ == '__main__':
    unittest.main()
