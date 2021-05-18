import unittest
from selenium.webdriver import ActionChains
from Actions.T3.electronicgame_page import ElectronicGamepageActions
from Actions.T3.login_page import LoginpageActions
from Elements.T3.electronicgame_page import ElectronicGameElement
from Setup.T3 import Base_Setup
from Actions.T3.main_page import MainpageActions
from Input_Data.T3.electronicgame_page import ElectronicGameData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class ElectronicGameSPAModule(Base_Setup.BSetup):

    def test_TC_SPA_01_Navigate_to_SpadeGaming_BeforeLogin(self):
        print("<b> Expected Results: Login Reminder modal dialog is displayed when accessing Spade Gaming game without valid login. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        ElectronicGamepageActions.Access_to_ElectronicGame_Tab(self)
        ElectronicGamepageActions.Access_to_SpadeGaming_Page(self)
        game_position = self.driver.find_element_by_xpath(ElectronicGameElement.spa_game)
        actions = ActionChains(self.driver)
        actions.move_to_element(game_position).perform()
        print("<li>" + "Click on a Spade Gaming game in the list: " + str(ElectronicGameData.loopranspa) + "</li>" + "<br>")
        wait_page_load = EC.element_to_be_clickable((By.XPATH, ElectronicGameElement.spa_game))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        select_game = self.driver.find_element_by_xpath(ElectronicGameElement.spa_game).click()
        ElectronicGamepageActions.Assert_Login_Reminder(self)


    def test_TC_SPA_02_Navigate_to_SpadeGaming_AfterLogin(self):
        print("<b> Expected Results: Quick Transfer modal dialog is displayed when accessing Spade Gaming game with valid login. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        ElectronicGamepageActions.Access_to_ElectronicGame_Tab(self)
        ElectronicGamepageActions.Access_to_SpadeGaming_Page(self)
        game_position = self.driver.find_element_by_xpath(ElectronicGameElement.spa_game)
        actions = ActionChains(self.driver)
        actions.move_to_element(game_position).perform()
        print("<li>" + "Click on a Spade Gaming game in the list: " + str(ElectronicGameData.loopranspa) + "</li>" + "<br>")
        wait_page_load = EC.element_to_be_clickable((By.XPATH, ElectronicGameElement.spa_game))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        select_game = self.driver.find_element_by_xpath(ElectronicGameElement.spa_game).click()
        ElectronicGamepageActions.Assert_Quick_Transfer(self)

    def test_TC_SPA_03_Enter_Game(self):
        print("<b> Expected Results: Able to access to gaming page. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        ElectronicGamepageActions.Access_to_ElectronicGame_Tab(self)
        ElectronicGamepageActions.Access_to_SpadeGaming_Page(self)
        game_position = self.driver.find_element_by_xpath(ElectronicGameElement.spa_game)
        actions = ActionChains(self.driver)
        actions.move_to_element(game_position).perform()
        print("<li>" + "Click on a Spade Gaming game in the list: " + str(ElectronicGameData.loopranspa) + "</li>" + "<br>")
        wait_page_load = EC.element_to_be_clickable((By.XPATH, ElectronicGameElement.spa_game))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        select_game = self.driver.find_element_by_xpath(ElectronicGameElement.spa_game).click()
        ElectronicGamepageActions.Assert_Quick_Transfer(self)
        ElectronicGamepageActions.Enter_Game(self)

    def test_TC_SPA_04_Quick_Transfer(self):
        print("<b> Expected Results: Able to perform quick transfer. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        ElectronicGamepageActions.Access_to_ElectronicGame_Tab(self)
        ElectronicGamepageActions.Access_to_SpadeGaming_Page(self)
        game_position = self.driver.find_element_by_xpath(ElectronicGameElement.spa_game)
        actions = ActionChains(self.driver)
        actions.move_to_element(game_position).perform()
        print("<li>" + "Click on a Spade Gaming game in the list: " + str(ElectronicGameData.loopranspa) + "</li>" + "<br>")
        wait_page_load = EC.element_to_be_clickable((By.XPATH, ElectronicGameElement.spa_game))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        select_game = self.driver.find_element_by_xpath(ElectronicGameElement.spa_game).click()
        ElectronicGamepageActions.Assert_Quick_Transfer(self)
        ElectronicGamepageActions.Quick_Transfer(self)


if __name__ == '__main__':
    unittest.main()
