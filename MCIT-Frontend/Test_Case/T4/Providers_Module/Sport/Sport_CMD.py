import unittest
from Actions.T4.login_page import LoginpageActions
from Actions.T4.providers_page import ProvidersActions
from Setup.T4 import Base_Setup
from Actions.T4.main_page import MainpageActions
import time


class SportCMDModule(Base_Setup.BSetup):

    def test_TC_SportCMD_01_Navigate_to_CMD_BeforeLogin(self):
        print("<b> Expected Results: Navigate to login page when accessing CMD game without valid login. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Access_to_Sport(self)
        ProvidersActions.Access_to_SportCMD_Page(self)
        ProvidersActions.Click_on_SportCMD_Game(self)
        time.sleep(2)
        ProvidersActions.Assert_Login_Page(self)

    def test_TC_SportCMD_02_Navigate_to_CMD_AfterLogin(self):
        print("<b> Expected Results: Quick Transfer modal dialog is displayed when accessing CMD game with valid login. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        MainpageActions.Access_to_Sport(self)
        ProvidersActions.Access_to_SportCMD_Page(self)
        ProvidersActions.Click_on_SportCMD_Game(self)
        time.sleep(2)
        ProvidersActions.Assert_Quick_Transfer(self)

    def test_TC_SportCMD_03_Enter_Game(self):
        print("<b> Expected Results: Able to access to gaming page. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        MainpageActions.Access_to_Sport(self)
        ProvidersActions.Access_to_SportCMD_Page(self)
        ProvidersActions.Click_on_SportCMD_Game(self)
        time.sleep(2)
        ProvidersActions.Enter_Game(self)

    def test_TC_SportCMD_04_Quick_Transfer(self):
        print("<b> Expected Results: Able to perform quick transfer. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        MainpageActions.Access_to_Sport(self)
        ProvidersActions.Access_to_SportCMD_Page(self)
        ProvidersActions.Click_on_SportCMD_Game(self)
        time.sleep(2)
        ProvidersActions.Quick_Transfer(self)


if __name__ == '__main__':
    unittest.main()
