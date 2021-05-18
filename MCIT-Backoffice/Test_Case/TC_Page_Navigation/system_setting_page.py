import unittest
import SetUp.Base_SetUp
from Actions.system_setting_page import Qr_Code_Actions
from Actions.system_setting_page import Parameter_Settings_Actions
from Actions.system_setting_page import Task_Management_Actions
from Actions.system_setting_page import Homepage_Carousel_Actions
from Actions.system_setting_page import Third_Party_Settings_Actions
from Actions.system_setting_page import File_Management_Actions
from Actions.system_setting_page import CMS_Actions
from Actions.system_setting_page import Fronted_Registration_Settings_Actions
from Actions.system_setting_page import Game_Maintenance_Actions
from Actions.system_setting_page import Bet_Limit_Setting_Actions


class Navigate_System_Setting_Modules(SetUp.Base_SetUp.BSetUp):

    def test_TC_System_Setting_01_Navigate_QR_Code_Page(self):
        Qr_Code_Actions.Navigate_Qr_Code(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_System_Setting_02_Navigate_Parameter_Settings_Page(self):
        Parameter_Settings_Actions.Navigate_Parameter_Settings(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_System_Setting_03_Navigate_Task_Management_Page(self):
        Task_Management_Actions.Navigate_Task_Management(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_System_Setting_04_Navigate_Homepage_Carousel_Page(self):
        Homepage_Carousel_Actions.Navigate_Homepage_Carousel(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_System_Setting_05_Navigate_Third_Party_Settings_Page(self):
        Third_Party_Settings_Actions.Navigate_Third_Party_Settings(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_System_Setting_06_Navigate_File_Management_Page(self):
        File_Management_Actions.Navigate_File_Management(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_System_Setting_07_Navigate_CMS_Page(self):
        CMS_Actions.Navigate_CMS(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_System_Setting_08_Navigate_Frontend_Registration_Settings_Page(self):
        Fronted_Registration_Settings_Actions.Navigate_Frontend_Registration_Settings(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_System_Setting_09_Navigate_Game_Maintenance_Page(self):
        Game_Maintenance_Actions.Navigate_Game_Maintenance(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_System_Setting_10_Navigate_Bet_Limit_Setting_Page(self):
        Bet_Limit_Setting_Actions.Navigate_Bet_Limit_Setting(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")


if __name__ == '__main__':
    unittest.main()
