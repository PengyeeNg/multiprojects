import unittest
from selenium.webdriver import ActionChains
from Actions.T3.livevideo_page import LiveVideopageActions
from Actions.T3.login_page import LoginpageActions
from Elements.T3.livevideo_page import LiveVideoElement
from Setup.T3 import Base_Setup
from Actions.T3.main_page import MainpageActions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Input_Data.T3.livevideo_page import LiveVideoData

class LiveVideoModule(Base_Setup.BSetup):

    def TC_LiveVideo_01_Navigate_to_LiveVideo_Page(self):
        print("<b> Expected Results: Able to access to Live Video page without breaking. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        LiveVideopageActions.Access_to_LiveVideo_Page(self)
        # Wait page loads
        wait_page_load = EC.visibility_of_element_located((By.XPATH, LiveVideoElement.live_video_game))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        live_video_game = self.driver.find_element_by_xpath(LiveVideoElement.live_video_game).is_displayed()
        self.assertTrue(live_video_game, "User is not able to access to Live Video Page.")

    def TC_LiveVideo_02_Navigate_to_LiveVideoGame_BeforeLogin(self):
        print("<b> Expected Results: Login Reminder modal dialog is displayed when accessing Live Video game without valid login. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        LiveVideopageActions.Access_to_LiveVideo_Page(self)
        # game_title = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div/div[2]/div[" + str(LiveVideoData.loopranlivevideo_game_pg1) + "]/div/button/div/p").text
        print("<li>" + "Click on a Live Video Game in the list: " + str(LiveVideoData.loopranlivevideo_game_pg1) + "</li>" + "<br>")
        select_game = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div/div[2]/div[" + str(LiveVideoData.loopranlivevideo_game_pg1) + "]/div/button/div/p").click()
        # Wait modal dialog load
        wait_page_load = EC.element_to_be_clickable((By.CLASS_NAME, LiveVideoElement.login_reminder_confirm_button))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        login_reminder_modal_dialog = self.driver.find_element_by_class_name(LiveVideoElement.login_reminder_confirm_button).is_displayed()
        self.assertTrue(login_reminder_modal_dialog, "Login reminder is not displayed.")

    def test_TC_LiveVideo_03_Navigate_to_LiveVideoGame_AfterLogin(self):
        print("<b> Expected Results: Quick Transfer modal dialog is displayed when accessing Big Gaming game with valid login.. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        LiveVideopageActions.Access_to_LiveVideo_Page(self)
        game_title = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div/div[2]/div[" + str(LiveVideoData.loopranlivevideo_game_pg1) + "]/div/button/div/p").text
        print("<li>" + "Click on a Live Video Game in the list: " + str(LiveVideoData.loopranlivevideo_game_pg1) + "</li>" + "<br>")
        select_game = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div/div[2]/div[" + str(LiveVideoData.loopranlivevideo_game_pg1) + "]/div/button/div/p").click()
        # Wait modal dialog load
        # wait_page_load = EC.element_to_be_clickable((By.CLASS_NAME, LiveVideoElement.))
        # WebDriverWait(self.driver, 20).until(wait_page_load)
        # login_reminder_modal_dialog = self.driver.find_element_by_class_name(LiveVideoElement.).is_displayed()
        # self.assertTrue(login_reminder_modal_dialog, "Quick Transfer is not displayed.")

if __name__ == '__main__':
    unittest.main()
