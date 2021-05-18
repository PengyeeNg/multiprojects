import unittest
import SetUp.Base_SetUp
from Actions.report_page import Overall_Actions
from Actions.report_page import Affiliate_Actions
from Actions.report_page import Cash_Flow_Actions
from Actions.report_page import Merchant_Win_Loss_Actions
from Actions.report_page import Merchant_Daily_Win_Loss_Actions
from Actions.report_page import Outstanding_Actions
from Actions.report_page import Evo_Actions
from Actions.report_page import SPA_Actions
from Actions.report_page import Mega_Actions
from Actions.report_page import XE88_Actions
from Actions.report_page import Joker_Actions
from Actions.report_page import Playtech_Actions
from Actions.report_page import CMD_Actions
from Actions.report_page import BG_Actions
from Actions.report_page import IBC_Actions
from Actions.report_page import IGS_Actions
from Actions.report_page import M8_Actions
from Actions.report_page import Nextspin_Actions
from Actions.report_page import WM_Actions


class Navigate_Report_Modules(SetUp.Base_SetUp.BSetUp):

    def test_TC_Report_01_Navigate_Overall_Page(self):
        Overall_Actions.Navigate_Overall(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Report_02_Navigate_Affiliate_Page(self):
        Affiliate_Actions.Navigate_Affiliate(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Report_03_Navigate_Cash_Flow_Page(self):
        Cash_Flow_Actions.Navigate_Cash_Flow(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Report_04_Navigate_Merchant_Win_Loss_Page(self):
        Merchant_Win_Loss_Actions.Navigate_Merchant_Win_loss(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Report_05_Navigate_Merchant_Daily_Win_Loss(self):
        Merchant_Daily_Win_Loss_Actions.Navigate_Merchant_Daily_Win_Loss(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Report_06_Navigate_Outstanding_Page(self):
        Outstanding_Actions.Navigate_Outstanding(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Report_07_Navigate_Evo_Page(self):
        Evo_Actions.Navigate_Evo(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Report_08_Navigate_SPA_Page(self):
        SPA_Actions.Navigate_SPA(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Report_09_Navigate_Mega_Page(self):
        Mega_Actions.Navigate_Mega(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Report_10_Navigate_XE88_Page(self):
        XE88_Actions.Navigate_XE88(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Report_11_Navigate_Joker_Page(self):
        Joker_Actions.Navigate_Joker(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Report_12_Navigate_Playtech_Page(self):
        Playtech_Actions.Navigate_Playtech(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Report_13_Navigate_CMD_Page(self):
        CMD_Actions.Navigate_CMD(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Report_14_Navigate_BG_Page(self):
        BG_Actions.Navigate_BG(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Report_15_Navigate_IBC_Page(self):
        IBC_Actions.Navigate_IBC(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Report_16_Navigate_IGS_Page(self):
        IGS_Actions.Navigate_IGS(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Report_17_Navigate_M8_Page(self):
        M8_Actions.Navigate_M8(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Report_18_Navigate_Nextspin_Page(self):
        Nextspin_Actions.Navigate_Nextspin(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Report_19_Navigate_WM_Page(self):
        WM_Actions.Navigate_WM(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")


if __name__ == '__main__':
    unittest.main()
