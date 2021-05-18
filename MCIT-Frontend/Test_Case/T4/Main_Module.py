import unittest
from Setup.T4 import Base_Setup
from Actions.T4.main_page import MainpageActions

class MainModule(Base_Setup.BSetup):

    def test_TC_Main_01_Navigate_to_Main_Page(self):
        print("<b> Expected Results: Able to access to main page without breaking. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)

    def test_TC_Main_02_Access_to_Casino_Page_viaCasinoTab(self):
        print("<b> Expected Results: Able to access to Casino page. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Access_to_Casino(self)

    def test_TC_Main_03_Access_to_Slot_Page_viaSlotTab(self):
        print("<b> Expected Results: Able to access to Slot page. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Access_to_Slot(self)

    def test_TC_Main_04_Access_to_Sport_Page_viaSportTab(self):
        print("<b> Expected Results: Able to access to Sport page. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Access_to_Sport(self)

    def test_TC_Main_05_Access_to_Promo_Page_viaPromoTab(self):
        print("<b> Expected Results: Able to access to Promo page. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Access_to_Promo(self)

    def test_TC_Main_06_Access_to_Casino_Page_viaLiveCasino(self):
        print("<b> Expected Results: Able to access to Casino page. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Navigate_to_Live_Casino(self)

    def test_TC_Main_07_Access_to_SlotGames_Page_viaSlotGames(self):
        print("<b> Expected Results: Able to access to Slot Games page. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Navigate_to_Slot_Games(self)

    def test_TC_Main_08_Access_to_Sports_Page_viaSports(self):
        print("<b> Expected Results: Able to access to Sports page. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Navigate_to_Sports(self)



if __name__ == '__main__':
    unittest.main()
