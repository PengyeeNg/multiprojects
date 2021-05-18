import unittest
import HtmlTestRunner
import shutil
from SetUp.Base_SetUp import BSetUp
from Input_Data.Browser import Test_Evidence_Path
from Test_Case.TC_Login import Login
from Test_Case.TC_Main import Main
from Test_Case.TC_Member import TC_Member_Edit, TC_Member_Levels, TC_Member_Log
from Test_Case.TC_Page_Navigation.administration_page import Navigate_Administration_Modules
from Test_Case.TC_Page_Navigation.announcement_page import Navigate_Announcement_Modules
from Test_Case.TC_Page_Navigation.bank_page import Navigate_Bank_Modules
from Test_Case.TC_Page_Navigation.department_page import Navigate_Department_Modules
from Test_Case.TC_Page_Navigation.deposit_withdraw_page import Navigate_Deposit_Withdraw_Modules
from Test_Case.TC_Page_Navigation.login_page import Navigate_Login_Modules
from Test_Case.TC_Page_Navigation.member_page import Navigate_Member_Modules
from Test_Case.TC_Page_Navigation.promotion_page import Navigate_Promotion_Modules
from Test_Case.TC_Page_Navigation.rebate_page import Navigate_Rebate_Modules
from Test_Case.TC_Page_Navigation.referral_page import Navigate_Referral_Modules
from Test_Case.TC_Page_Navigation.report_page import Navigate_Report_Modules
from Test_Case.TC_Page_Navigation.system_setting_page import Navigate_System_Setting_Modules
from Test_Case.TC_Promotion import TC_List_Promotion, TC_Promotion_Banner, TC_Promotion_Statistic, TC_Promotion_Mission
from Test_Case.TC_Deposit_Withdraw import TC_Deposit, TC_Deposit_History, TC_Withdrawal, TC_Withdraw_History, TC_Adjust_Balance, TC_Account_Transaction_Record, TC_Bonus, TC_Commission_Record, TC_Adjustment_Record, TC_Turn_Over_Amount_Record, TC_Wallet_Transfer
from Test_Case.TC_Rebate import TC_Rebate_Setting, TC_Rebate_Record, TC_Provider_Report, TC_Member_Report
from Test_Case.TC_Referral import TC_Member_Map
from Test_Case.TC_Announcement import TC_Member_Message
from Test_Case.TC_Report import TC_Overall, TC_Affiliate, TC_Cash_Flow, TC_Merchant_Win_Loss, TC_Merchant_Daily_Win_Loss, TC_Outstanding
from Test_Case.TC_Report.TC_Betting_Record import TC_Evo_Betting_Record, TC_SPA_Betting_Record, TC_Mega_Betting_Record, TC_XE88_Betting_Record, TC_Joker_Betting_Record, TC_Playtech_Betting_Record, TC_CMD_Betting_Record, TC_BG_Betting_Record, TC_IBC_Betting_Record, TC_IBC_Betting_Record, TC_IGS_Betting_Record, TC_M8_Betting_Record, TC_NextSpin_Betting_Record, TC_WM_Betting_Record

# Get all tests
suite_PN_01 = unittest.TestLoader().loadTestsFromTestCase(Navigate_Announcement_Modules)
suite_PN_02 = unittest.TestLoader().loadTestsFromTestCase(Navigate_Bank_Modules)
suite_PN_03 = unittest.TestLoader().loadTestsFromTestCase(Navigate_Department_Modules)
suite_PN_04 = unittest.TestLoader().loadTestsFromTestCase(Navigate_Deposit_Withdraw_Modules)
suite_PN_05 = unittest.TestLoader().loadTestsFromTestCase(Navigate_Login_Modules)
suite_PN_06 = unittest.TestLoader().loadTestsFromTestCase(Navigate_Member_Modules)
suite_PN_07 = unittest.TestLoader().loadTestsFromTestCase(Navigate_Promotion_Modules)
suite_PN_08 = unittest.TestLoader().loadTestsFromTestCase(Navigate_Rebate_Modules)
suite_PN_09 = unittest.TestLoader().loadTestsFromTestCase(Navigate_Referral_Modules)
suite_PN_10 = unittest.TestLoader().loadTestsFromTestCase(Navigate_Report_Modules)
suite_PN_11 = unittest.TestLoader().loadTestsFromTestCase(Navigate_System_Setting_Modules)
suite_PN_12 = unittest.TestLoader().loadTestsFromTestCase(Navigate_Administration_Modules)
suite01 = unittest.TestLoader().loadTestsFromTestCase(Login)
suite02 = unittest.TestLoader().loadTestsFromTestCase(Main)
suite03_01 = unittest.TestLoader().loadTestsFromTestCase(TC_Member_Edit.Member_Edit)
suite03_02 = unittest.TestLoader().loadTestsFromTestCase(TC_Member_Levels.Member_Levels)
suite03_03 = unittest.TestLoader().loadTestsFromTestCase(TC_Member_Log.Member_Log)
suite04_01 = unittest.TestLoader().loadTestsFromTestCase(TC_List_Promotion.List_Promotion)
suite04_02 = unittest.TestLoader().loadTestsFromTestCase(TC_Promotion_Banner.Promotion_Banner)
suite04_03 = unittest.TestLoader().loadTestsFromTestCase(TC_Promotion_Statistic.Promotion_Statistic)
suite04_04 = unittest.TestLoader().loadTestsFromTestCase(TC_Promotion_Mission.Promotion_Mission)
suite05_01 = unittest.TestLoader().loadTestsFromTestCase(TC_Deposit.Deposit)
suite05_02 = unittest.TestLoader().loadTestsFromTestCase(TC_Deposit_History.Deposit_History)
suite05_03 = unittest.TestLoader().loadTestsFromTestCase(TC_Withdrawal.Withdrawal)
suite05_04 = unittest.TestLoader().loadTestsFromTestCase(TC_Withdraw_History.Withdraw_History)
suite05_05 = unittest.TestLoader().loadTestsFromTestCase(TC_Adjust_Balance.Adjust_Balance)
suite05_06 = unittest.TestLoader().loadTestsFromTestCase(TC_Account_Transaction_Record.Account_Transaction_Record)
suite05_07 = unittest.TestLoader().loadTestsFromTestCase(TC_Bonus.Bonus)
suite05_08 = unittest.TestLoader().loadTestsFromTestCase(TC_Commission_Record.Commission_Record)
suite05_09 = unittest.TestLoader().loadTestsFromTestCase(TC_Adjustment_Record.Adjustment_Record)
suite05_10 = unittest.TestLoader().loadTestsFromTestCase(TC_Turn_Over_Amount_Record.Turn_Over_Amount_Record)
suite05_11 = unittest.TestLoader().loadTestsFromTestCase(TC_Wallet_Transfer.Wallet_Transfer)
suite06_01 = unittest.TestLoader().loadTestsFromTestCase(TC_Rebate_Setting.Rebate_Setting)
suite06_02 = unittest.TestLoader().loadTestsFromTestCase(TC_Rebate_Record.Rebate_Record)
suite06_03 = unittest.TestLoader().loadTestsFromTestCase(TC_Provider_Report.Provider_Report)
suite06_04 = unittest.TestLoader().loadTestsFromTestCase(TC_Member_Report.Member_Report)
suite07_01 = unittest.TestLoader().loadTestsFromTestCase(TC_Overall.Overall)
suite07_02 = unittest.TestLoader().loadTestsFromTestCase(TC_Affiliate.Affiliate)
suite07_03 = unittest.TestLoader().loadTestsFromTestCase(TC_Cash_Flow.Cash_Flow)
suite07_04 = unittest.TestLoader().loadTestsFromTestCase(TC_Merchant_Win_Loss.Merchant_Win_Loss)
suite07_05 = unittest.TestLoader().loadTestsFromTestCase(TC_Merchant_Daily_Win_Loss.Merchant_Daily_Win_Loss)
suite07_06 = unittest.TestLoader().loadTestsFromTestCase(TC_Outstanding.Outstanding)
suite07_07_01 = unittest.TestLoader().loadTestsFromTestCase(TC_Evo_Betting_Record.Evo_Betting_Record)
suite07_07_02 = unittest.TestLoader().loadTestsFromTestCase(TC_SPA_Betting_Record.SPA_Betting_Record)
suite07_07_03 = unittest.TestLoader().loadTestsFromTestCase(TC_Mega_Betting_Record.Mega_Betting_Record)
suite07_07_04 = unittest.TestLoader().loadTestsFromTestCase(TC_XE88_Betting_Record.XE88_Betting_Record)
suite07_07_05 = unittest.TestLoader().loadTestsFromTestCase(TC_Joker_Betting_Record.Joker_Betting_Record)
suite07_07_06 = unittest.TestLoader().loadTestsFromTestCase(TC_Playtech_Betting_Record.Playtech_Betting_Record)
suite07_07_07 = unittest.TestLoader().loadTestsFromTestCase(TC_CMD_Betting_Record.CMD_Betting_Record)
suite07_07_08 = unittest.TestLoader().loadTestsFromTestCase(TC_BG_Betting_Record.BG_Betting_Record)
suite07_07_09 = unittest.TestLoader().loadTestsFromTestCase(TC_IBC_Betting_Record.IBC_Betting_Record)
suite07_07_10 = unittest.TestLoader().loadTestsFromTestCase(TC_IGS_Betting_Record.IGS_Betting_Record)
suite07_07_11 = unittest.TestLoader().loadTestsFromTestCase(TC_M8_Betting_Record.M8_Betting_Record)
suite07_07_12 = unittest.TestLoader().loadTestsFromTestCase(TC_NextSpin_Betting_Record.NextSpin_Betting_Record)
suite07_07_13 = unittest.TestLoader().loadTestsFromTestCase(TC_WM_Betting_Record.WM_Betting_Record)
suite08 = unittest.TestLoader().loadTestsFromTestCase(TC_Member_Map.Member_Map)
suite09 = unittest.TestLoader().loadTestsFromTestCase(TC_Member_Message.Member_Mesage)


# Create test suites
PNTestSuite = unittest.TestSuite([suite_PN_01, suite_PN_02, suite_PN_03, suite_PN_04, suite_PN_05, suite_PN_06, suite_PN_07, suite_PN_08, suite_PN_09, suite_PN_10, suite_PN_11])  # Sanity Test- Page Navigation
TestSuite_01 = unittest.TestSuite([suite07_07_02, suite07_07_03, suite07_07_04, suite07_07_05, suite07_07_06, suite07_07_07, suite07_07_08, suite07_07_09, suite07_07_10, suite07_07_11, suite07_07_12, suite07_07_13])
TestSuite_02 = unittest.TestSuite(suite07_07_11)

# Generate test report
report = Test_Evidence_Path.report_path
html_runner = HtmlTestRunner.HTMLTestRunner(
    output=report,
    report_title='MCIT-Backoffice Test Report',
    report_name='BackOffice_Test_Report',
    combine_reports=True,
    )

# run the test suites
html_runner.run(TestSuite_02)

# Remove test evidence Folder
shutil.rmtree(BSetUp.screenshot_path)
