import unittest
import HtmlTestRunner
import shutil
from Setup.T3.Base_Setup import BSetup
from Input_Data.T3.Browser import TestEvidencePath
from Test_Case.T3 import Main_Module
from Test_Case.T3 import Login_Module
from Test_Case.T3 import Sign_Up_Module
from Test_Case.T3 import Live_Video_Module
from Test_Case.T3.Electronic_Game_Module.Big_Gaming import Big_Gaming
from Test_Case.T3.Electronic_Game_Module.CMD import CMD
from Test_Case.T3.Electronic_Game_Module.Evolution_Gaming import Evolution_Gaming
from Test_Case.T3.Electronic_Game_Module.IBC import IBC
from Test_Case.T3.Electronic_Game_Module.IGS import IGS
from Test_Case.T3.Electronic_Game_Module.M8_Sports import M8_Sports
from Test_Case.T3.Electronic_Game_Module.NextSpin import NextSpin
from Test_Case.T3.Electronic_Game_Module.SBO import SBO
from Test_Case.T3.Electronic_Game_Module.Spade_Gaming import Spade_Gaming
from Test_Case.T3.Electronic_Game_Module.WM_Casino import WM_Casino
from Test_Case.T3.ESport_Module.CMD import ESportsCMD
from Test_Case.T3.ESport_Module.IBC import ESportsIBC
from Test_Case.T3.ESport_Module.M8_Sports import ESportsM8_Sports
from Test_Case.T3.ESport_Module.Sports_Book import ESportsSports_Book
from Test_Case.T3.ESport_Module.Virtual_Sports import ESportsVirtual_Sports
from Test_Case.T3 import Promotions_Module
from Test_Case.T3 import Download_Center_Module
from Test_Case.T3.User_Module import Announcement
from Test_Case.T3.User_Module import Betting_Record
from Test_Case.T3.User_Module import Deposit_Area
from Test_Case.T3.User_Module import Funding_Records
from Test_Case.T3.User_Module import Member_Agent
from Test_Case.T3.User_Module import Personal_Information
from Test_Case.T3.User_Module import Quota_Conversion
from Test_Case.T3.User_Module import Withdrawal_Area

# Get all tests
suite_01 = unittest.TestLoader().loadTestsFromTestCase(Main_Module.MainModule)
suite_02 = unittest.TestLoader().loadTestsFromTestCase(Login_Module.LoginModule)
suite_03 = unittest.TestLoader().loadTestsFromTestCase(Sign_Up_Module.SignUpModule)
suite_04 = unittest.TestLoader().loadTestsFromTestCase(Live_Video_Module.LiveVideoModule)
suite_05_01 = unittest.TestLoader().loadTestsFromTestCase(Big_Gaming.ElectronicGameBIGModule)
suite_05_02 = unittest.TestLoader().loadTestsFromTestCase(CMD.ElectronicGameCMDModule)
suite_05_03 = unittest.TestLoader().loadTestsFromTestCase(Evolution_Gaming.ElectronicGameEVOModule)
suite_05_04 = unittest.TestLoader().loadTestsFromTestCase(IBC.ElectronicGameIBCModule)
suite_05_05 = unittest.TestLoader().loadTestsFromTestCase(IGS.ElectronicGameIGSModule)
suite_05_06 = unittest.TestLoader().loadTestsFromTestCase(M8_Sports.ElectronicGameM8Module)
suite_05_07 = unittest.TestLoader().loadTestsFromTestCase(NextSpin.ElectronicGameNextSpinModule)
suite_05_08 = unittest.TestLoader().loadTestsFromTestCase(SBO.ElectronicGameSBOModule)
suite_05_09 = unittest.TestLoader().loadTestsFromTestCase(Spade_Gaming.ElectronicGameSPAModule)
suite_05_10 = unittest.TestLoader().loadTestsFromTestCase(WM_Casino.ElectronicGameWMModule)
suite_06_01 = unittest.TestLoader().loadTestsFromTestCase(ESportsCMD.ESportsCMDModule)
suite_06_02 = unittest.TestLoader().loadTestsFromTestCase(ESportsIBC.ESportsIBCModule)
suite_06_03 = unittest.TestLoader().loadTestsFromTestCase(ESportsM8_Sports.ESportsM8Module)
suite_06_04 = unittest.TestLoader().loadTestsFromTestCase(ESportsSports_Book.ESportsSportsBookModule)
suite_06_05 = unittest.TestLoader().loadTestsFromTestCase(ESportsVirtual_Sports.ESportsVirtualSportsModule)
suite_07 = unittest.TestLoader().loadTestsFromTestCase(Promotions_Module.PromotionsModule)
suite_08 = unittest.TestLoader().loadTestsFromTestCase(Download_Center_Module.DownloadCenterModule)
suite_09_01 = unittest.TestLoader().loadTestsFromTestCase(Announcement.AnnouncementModule)
suite_09_02 = unittest.TestLoader().loadTestsFromTestCase(Betting_Record.BettingRecordModule)
suite_09_03 = unittest.TestLoader().loadTestsFromTestCase(Deposit_Area.DepositAreaModule)
suite_09_04 = unittest.TestLoader().loadTestsFromTestCase(Funding_Records.FundingRecordsModule)
suite_09_05 = unittest.TestLoader().loadTestsFromTestCase(Member_Agent.MemberAgentModule)
suite_09_06 = unittest.TestLoader().loadTestsFromTestCase(Personal_Information.PersonalInformationModule)
suite_09_07 = unittest.TestLoader().loadTestsFromTestCase(Quota_Conversion.QuotaConversionModule)
suite_09_08 = unittest.TestLoader().loadTestsFromTestCase(Withdrawal_Area.WithdrawalAreaModule)


# Create test suites
Test_01 = unittest.TestSuite(suite_09_08)

# Generate test report
report = TestEvidencePath.report_path


html_runner = HtmlTestRunner.HTMLTestRunner(
    output=report,
    report_title='MCIT-Frontend Test Report',
    report_name='FrontendT3_Test_Report',
    combine_reports=True,
    )

# run the test suites
html_runner.run(Test_01)

# Remove test evidence Folder
shutil.rmtree(BSetup.screenshot_path)
