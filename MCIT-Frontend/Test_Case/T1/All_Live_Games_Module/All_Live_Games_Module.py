import unittest
from Setup.T1 import Base_Setup
from Actions.T1.alllivegames_page import AllLiveGamesActions
from Actions.T1.main_page import MainpageActions
from Actions.T1.login_page import LoginpageActions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Input_Data.T1.main_page import MainData

class AllLiveGamesModule(Base_Setup.BSetup):

    def test_TC_AllLiveGames_01_Access_to_AllLiveGames_AfterLogin(self):
        print("<b> Expected Results: Quick Transfer modal dialog is displayed. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        MainpageActions.Access_to_AllLiveGames_Page(self)
        # for i in range(1, 2, 1):
        for j in range(1, 5, 1):
            wait_page_load = EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div/div[2]/ul/li[" + str(MainData.loopranalllive) + "]/a/p"))
            WebDriverWait(self.driver, 10).until(wait_page_load)
        game_title = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div/div[2]/ul/li[" + str(MainData.loopranalllive) + "]/a/p").text
        print("<li>" + "Click on All Live Games in the list: " + game_title + "</li>" + "<br>")
        wait_page_load = EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div/div[2]/ul/li[" + str(MainData.loopranalllive) + "]/a/img"))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        games = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div/div[2]/ul/li[" + str(MainData.loopranalllive) + "]/a/img").click()
        # Assert
        AllLiveGamesActions.Assert_Quick_Transfer_Modal_Dialog(self)

    def test_TC_AllLiveGames_02_Access_to_AllLiveGames_BeforeLogin(self):
        print("<b> Expected Results: Navigated to Login Page after clicking on All Live Games without valid login. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Access_to_AllLiveGames_Page(self)
        # Assert
        # for i in range(1, 2, 1):
        for j in range(1, 5, 1):
            wait_page_load = EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div/div[2]/ul/li[" + str(MainData.loopranalllive) + "]/a/p"))
            WebDriverWait(self.driver, 10).until(wait_page_load)
        game_title = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div/div[2]/ul/li[" + str(MainData.loopranalllive) + "]/a/p").text
        print("<li>" + "Click on All Live Games in the list: " + game_title + "</li>" + "<br>")
        wait_page_load = EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div/div[2]/ul/li[" + str(MainData.loopranalllive) + "]/a/img"))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        games = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div/div[2]/ul/li[" + str(MainData.loopranalllive) + "]/a/img").click()
        MainpageActions.Assert_Navigated_to_LoginPage(self)


if __name__ == '__main__':
    unittest.main()
