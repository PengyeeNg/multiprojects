import unittest
from Actions.T3.promotions_page import PromotionspageActions
from Setup.T3 import Base_Setup
from Actions.T3.main_page import MainpageActions


class PromotionsModule(Base_Setup.BSetup):

    def test_TC_DownloadCenter_01_Navigate_to_DownloadCenterPage(self):
        print("<b> Expected Results: Able to access to promotions page without breaking. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        PromotionspageActions.Access_to_Promotions(self)


if __name__ == '__main__':
    unittest.main()
