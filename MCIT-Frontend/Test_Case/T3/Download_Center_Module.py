import unittest
from Actions.T3.download_center_page import DownloadCenterpageActions
from Setup.T3 import Base_Setup
from Actions.T3.main_page import MainpageActions


class DownloadCenterModule(Base_Setup.BSetup):

    def test_TC_DownloadCenter_01_Navigate_to_DownloadCenterPage(self):
        print("<b> Expected Results: Able to access to download center page without breaking. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        DownloadCenterpageActions.Access_to_Download_Center(self)


if __name__ == '__main__':
    unittest.main()
