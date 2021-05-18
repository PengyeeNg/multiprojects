import unittest
from Setup.T1 import Base_Setup
from Actions.T1.login_page import LoginpageActions
from Actions.T1.main_page import MainpageActions
from Actions.T1.providers_page import ProvidersActions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Elements.T1.providers_page import ProvidersElement
from Input_Data.T1.providers_page import ProvidersData

class ProvidersSPAModule(Base_Setup.BSetup):

    def test_TC_Providers_SPA_01_Enter_Game(self):
        print("<b> Expected Results: Able to enter game page. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        MainpageActions.Access_to_Providers_Page(self)
        ProvidersActions.Navigate_to_Spade_Gaming(self)
        self.driver.implicitly_wait(10)
        window_before = self.driver.window_handles[0]

        # Assert
        # for i in range(1, 2, 1):
        for j in range(10):
            wait_page_load = EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div/div[2]/ul/li["+str(ProvidersData.loopranspa)+"]/a/p"))
            WebDriverWait(self.driver, 10).until(wait_page_load)
        game_title = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div/div[2]/ul/li["+str(ProvidersData.loopranspa)+"]/a/p").text
        print("<li>" + "Click on Spade Gaming Game in the list: " + game_title + "</li>" + "<br>")
        wait_page_load = EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div/div[2]/ul/li["+str(ProvidersData.loopranspa)+"]/a/img"))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        games = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div/div[2]/ul/li["+str(ProvidersData.loopranspa)+"]/a/img").click()
        ProvidersActions.Assert_Quick_Transfer_Modal_Dialog(self)
        ProvidersActions.Quick_Transfer_Enter_Game(self)
        waitnewpage = EC.new_window_is_opened(self.driver.window_handles)
        WebDriverWait(self.driver, 30).until(waitnewpage)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.implicitly_wait(10)
        ProvidersActions.Assert_New_Gaming_Page(self)
        # Switch back to Provider Page
        # self.driver.switch_to.window(self.driver.window_handles[0])
        # Close Quick transfer Modal Dialog
        # ProvidersActions.Providers_Close_Quick_Transfer_Modal_Dialogs(self)


    def test_TC_Providers_SPA_02_Quick_Transfer(self):
        print("<b> Expected Results: Able to perform quick transfer. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        MainpageActions.Access_to_Providers_Page(self)
        ProvidersActions.Navigate_to_Spade_Gaming(self)
        self.driver.implicitly_wait(10)

        # Assert
        # for i in range(1, 2, 1):
        for j in range(10):
            wait_page_load = EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div/div[2]/ul/li["+str(ProvidersData.loopranspa)+"]/a/p"))
            WebDriverWait(self.driver, 10).until(wait_page_load)
        game_title = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div/div[2]/ul/li[" + str(ProvidersData.loopranspa) + "]/a/p").text
        print("<li>" + "Click on Spade Gaming Game in the list: " + game_title + "</li>" + "<br>")
        wait_page_load = EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div/div[2]/ul/li[" + str(ProvidersData.loopranspa) + "]/a/img"))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        games = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div/div[2]/ul/li[" + str(ProvidersData.loopranspa) + "]/a/img").click()
        ProvidersActions.Assert_Quick_Transfer_Modal_Dialog(self)
        # Find the initial amount
        ini_amount = self.driver.find_element_by_css_selector(ProvidersElement.credit_amount).text
        print("Initial Amount: " + str(ini_amount) + "<br>")
        ProvidersActions.Quick_Transfer(self)
        # Close Quick transfer Modal Dialog
        ProvidersActions.Providers_Close_Quick_Transfer_Modal_Dialogs(self)
        # Refresh
        self.driver.refresh()
        wait_page_load = EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div/div[2]/ul/li[" + str(ProvidersData.loopranspa) + "]/a/img"))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        # Find the finial amount
        final_amount = self.driver.find_element_by_css_selector(ProvidersElement.credit_amount).text
        print("Final Amount: " + str(final_amount) + "<br>")
        self.assertTrue(ini_amount > final_amount, "Unable to perform quick transfer")

    def test_TC_Providers_SPA_03_Enter_Game_BeforeLogin(self):
        print("<b> Expected Results: Navigated to Login Page. </b>" + "<br>")
        MainpageActions.Access_to_Mainpage(self)
        MainpageActions.Access_to_Providers_Page(self)
        ProvidersActions.Navigate_to_Spade_Gaming(self)
        self.driver.implicitly_wait(10)

        # Assert
        # for i in range(1, 7, 1):
        for j in range(10):
            wait_page_load = EC.presence_of_element_located((By.XPATH,"/html/body/div/div/div/div[2]/div[2]/div/div[2]/ul/li[" + str(ProvidersData.loopranspa) + "]/a/p"))
            WebDriverWait(self.driver, 10).until(wait_page_load)
        game_title = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div/div[2]/ul/li[" + str(ProvidersData.loopranspa) + "]/a/p").text
        print("<li>" + "Click on Spade Game in the list: " + game_title + "</li>" + "<br>")
        wait_page_load = EC.element_to_be_clickable((By.XPATH,"/html/body/div/div/div/div[2]/div[2]/div/div[2]/ul/li[" + str(ProvidersData.loopranspa) + "]/a/img"))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        games = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div/div[2]/ul/li[" + str(ProvidersData.loopranspa) + "]/a/img").click()
        # Assert
        ProvidersActions.Assert_Navigated_to_LoginPage(self)


if __name__ == '__main__':
    unittest.main()
