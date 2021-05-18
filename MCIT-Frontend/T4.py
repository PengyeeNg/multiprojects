import unittest
import HtmlTestRunner
import shutil
from Setup.T4.Base_Setup import BSetup
from Input_Data.T4.Browser import TestEvidencePath
from Test_Case.T4 import Main_Module
from Test_Case.T4 import Login_Module
from Test_Case.T4 import Register_Module
from Test_Case.T4.User_Module import Account, Notification, Referrer, Profile
from Test_Case.T4.Providers_Module.Casino import Casino_Big_Gaming, Casino_Evolution_Gaming, Casino_SBO, Casino_WM_Casino
from Test_Case.T4.Providers_Module.Slot import Slot_Big_Gaming, Slot_IGS, Slot_SBO, Slot_Spade_Gaming
from Test_Case.T4.Providers_Module.Sport import Sport_CMD, Sport_IBC, Sport_M8_Sports, Sport_SBO


# Get all tests
suite_01 = unittest.TestLoader().loadTestsFromTestCase(Main_Module.MainModule)
suite_02 = unittest.TestLoader().loadTestsFromTestCase(Login_Module.LoginModule)
suite_03 = unittest.TestLoader().loadTestsFromTestCase(Register_Module.RegisterModule)
suite_04_01 = unittest.TestLoader().loadTestsFromTestCase(Account.UserAccountModule)
suite_04_02 = unittest.TestLoader().loadTestsFromTestCase(Profile.UserProfileModule)
suite_04_03 = unittest.TestLoader().loadTestsFromTestCase(Notification.UserNotificationModule)
suite_04_04 = unittest.TestLoader().loadTestsFromTestCase(Referrer.UserReferrerModule)
suite_05_01 = unittest.TestLoader().loadTestsFromTestCase(Casino_Big_Gaming.CasinoBIGModule)
suite_05_02 = unittest.TestLoader().loadTestsFromTestCase(Casino_Evolution_Gaming.CasinoEVOModule)
suite_05_03 = unittest.TestLoader().loadTestsFromTestCase(Casino_SBO.CasinoSBOModule)
suite_05_04 = unittest.TestLoader().loadTestsFromTestCase(Casino_WM_Casino.CasinoWMModule)
suite_06_01 = unittest.TestLoader().loadTestsFromTestCase(Slot_Big_Gaming.SlotBIGModule)
suite_06_02 = unittest.TestLoader().loadTestsFromTestCase(Slot_IGS.SlotIGSModule)
suite_06_03 = unittest.TestLoader().loadTestsFromTestCase(Slot_SBO.SlotSBOModule)
suite_06_04 = unittest.TestLoader().loadTestsFromTestCase(Slot_Spade_Gaming.SlotSPAModule)
suite_07_01 = unittest.TestLoader().loadTestsFromTestCase(Sport_CMD.SportCMDModule)
suite_07_02 = unittest.TestLoader().loadTestsFromTestCase(Sport_IBC.SportIBCModule)
suite_07_03 = unittest.TestLoader().loadTestsFromTestCase(Sport_M8_Sports.SportM8Module)
suite_07_04 = unittest.TestLoader().loadTestsFromTestCase(Sport_SBO.SportSBOModule)

# Create test suites
Test_01 = unittest.TestSuite([suite_05_01, suite_05_02, suite_05_03, suite_05_04, suite_06_01, suite_06_02, suite_06_03, suite_06_04, suite_07_01, suite_07_02, suite_07_03, suite_07_04])

# Generate test report
report = TestEvidencePath.report_path


html_runner = HtmlTestRunner.HTMLTestRunner(
    output=report,
    report_title='MCIT-Frontend Test Report',
    report_name='FrontendT4_Test_Report',
    combine_reports=True,
    )

# run the test suites
html_runner.run(Test_01)

# Remove test evidence Folder
shutil.rmtree(BSetup.screenshot_path)