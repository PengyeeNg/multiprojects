import unittest
from Actions.T3.user_page import UserpageActions
from Setup.T3 import Base_Setup
from Elements.T3.user_page import UserElement


class BettingRecordModule(Base_Setup.BSetup):

    def test_TC_BettingRecord_01_Navigate_to_Betting_Record_Page(self):
        print("<b> Expected Results: Able to access to betting record page. </b>" + "<br>")
        UserpageActions.Access_to_Betting_Record(self)

    def test_TC_BettingRecord_02_Choose_Game_Platform(self):
        print("<b> Expected Results: Able to choose game platform. </b>" + "<br>")
        UserpageActions.Access_to_Betting_Record(self)
        print("<li>" + "Click on Choose a Game Platform button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(UserElement.betting_record_choose_game_platform).click()
        print("<li>" + "Select a platform: Video All" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserElement.betting_record_game_platform_video_all).click()


if __name__ == '__main__':
    unittest.main()
