import unittest
from Actions.T3.esports_page import EsportspageActions
from Actions.T3.login_page import LoginpageActions
from Setup.T3 import Base_Setup
from Actions.T3.main_page import MainpageActions


class ESportsVirtualSportsModule(Base_Setup.BSetup):

    def test_TC_ESportsVirtualSports_01_Navigate_to_VirtualSports_BeforeLogin(self):
        print("<b> Expected Results: Login Reminder modal dialog is displayed when accessing Virtual Sports game without valid login. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        EsportspageActions.Access_to_E_Sports_Tab(self)
        EsportspageActions.Access_to_VirtualSports_Page(self)
        EsportspageActions.Assert_Login_Reminder(self)

    def test_TC_ESportsVirtualSports_02_Navigate_to_VirtualSports_AfterLogin(self):
        print("<b> Expected Results: Quick Transfer modal dialog is displayed when accessing Virtual Sports game with valid login. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        EsportspageActions.Access_to_E_Sports_Tab(self)
        EsportspageActions.Access_to_VirtualSports_Page(self)
        EsportspageActions.Assert_Quick_Transfer(self)

    def test_TC_ESportsVirtualSports_03_Enter_Game(self):
        print("<b> Expected Results: Able to access to gaming page. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        EsportspageActions.Access_to_E_Sports_Tab(self)
        EsportspageActions.Access_to_VirtualSports_Page(self)
        EsportspageActions.Assert_Quick_Transfer(self)
        EsportspageActions.Enter_Game(self)

    def test_TC_ESportsVirtualSports_04_Quick_Transfer(self):
        print("<b> Expected Results: Able to perform quick transfer. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        EsportspageActions.Access_to_E_Sports_Tab(self)
        EsportspageActions.Access_to_VirtualSports_Page(self)
        EsportspageActions.Assert_Quick_Transfer(self)
        EsportspageActions.Quick_Transfer(self)


if __name__ == '__main__':
    unittest.main()