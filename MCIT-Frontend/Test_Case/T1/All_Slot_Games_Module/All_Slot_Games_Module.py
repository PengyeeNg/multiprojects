import unittest
from Setup.T1 import Base_Setup
from Actions.T1.allslotgames_page import AllSlotGamesActions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Actions.T1.login_page import LoginpageActions
from Actions.T1.main_page import MainpageActions
from Input_Data.T1.main_page import MainData

class AllSlotGamesModule(Base_Setup.BSetup):

    def test_TC_AllSlotGames_01_Access_to_AllSlotGames_AfterLogin(self):
        print("<b> Expected Results: Quick Transfer modal dialog is displayed. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        MainpageActions.Access_to_AllSlotGames_Page(self)
        # for i in range(1, 2, 1):
        for j in range(1, 5, 1):
            wait_page_load = EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div/div[2]/ul/li[" + str(MainData.loopranallslot) + "]/a/p"))
            WebDriverWait(self.driver, 10).until(wait_page_load)
        game_title = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div/div[2]/ul/li[" + str(MainData.loopranallslot) + "]/a/p").text
        print("<li>" + "Click on All Live Games in the list: " + game_title + "</li>" + "<br>")
        wait_page_load = EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div/div[2]/ul/li[" + str(MainData.loopranallslot) + "]/a/img"))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        games = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div/div[2]/ul/li[" + str(MainData.loopranallslot) + "]/a/img").click()
        # Assert
        AllSlotGamesActions.Assert_Quick_Transfer_Modal_Dialog(self)

    def test_TC_AllSlotGames_02_Access_to_AllSlotGames_BeforeLogin(self):
        print("<b> Expected Results: Navigated to Login Page after clicking on All Slot Games without valid login. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Access_to_AllSlotGames_Page(self)
        # Assert
        #for i in range(1, 2, 1):
        for j in range(1, 5, 1):
            wait_page_load = EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div/div[2]/ul/li[" + str(MainData.loopranallslot) + "]/a/p"))
            WebDriverWait(self.driver, 10).until(wait_page_load)
        game_title = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div/div[2]/ul/li[" + str(MainData.loopranallslot) + "]/a/p").text
        print("<li>" + "Click on All Live Games in the list: " + game_title + "</li>" + "<br>")
        wait_page_load = EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div/div[2]/ul/li[" + str(MainData.loopranallslot) + "]/a/img"))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        games = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div/div[2]/ul/li[" + str(MainData.loopranallslot) + "]/a/img").click()
        MainpageActions.Assert_Navigated_to_LoginPage(self)


if __name__ == '__main__':
    unittest.main()

