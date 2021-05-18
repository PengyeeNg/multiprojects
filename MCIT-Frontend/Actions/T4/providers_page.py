from Setup.T4 import Base_Setup
from Elements.T4.providers_page import CasinoElement
from Elements.T4.providers_page import SportElement
from Elements.T4.providers_page import SlotElement
from Elements.T4.providers_page import ProvidersElement
from Input_Data.T4.providers_page import ProvidersData
from Input_Data.T4.providers_page import SlotData
from Input_Data.T4.providers_page import SportData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import requests
import time

class ProvidersActions(Base_Setup.BSetup):


    def Access_to_CasinoEvo_Page(self):
        print("<li>" + "Click on Evolution Gaming" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(CasinoElement.evo_gaming_button).click()

    def Click_on_CasinoEvo_Game(self):
        print("<li>" + "Click on an Evolution Gaming game in the list" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(CasinoElement.single_game_button).click()

    def Access_to_CasinoSBO_Page(self):
        print("<li>" + "Click on SBO" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(CasinoElement.sbo_button).click()

    def Click_on_CasinoSBO_Game(self):
        print("<li>" + "Click on a SBO game in the list" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(CasinoElement.single_game_button).click()

    def Access_to_CasinoBigGaming_Page(self):
        print("<li>" + "Click on Big Gaming" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(CasinoElement.big_gaming_button).click()

    def Click_on_CasinoBigGaming_Game(self):
        print("<li>" + "Click on a Big Gaming game in the list" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(CasinoElement.single_game_button).click()

    def Access_to_CasinoWM_Casino_Page(self):
        print("<li>" + "Click on WM Casino" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(CasinoElement.wm_casino_button).click()

    def Click_on_CasinoWM_Game(self):
        print("<li>" + "Click on a WM Casino game in the list" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(CasinoElement.single_game_button).click()

    def Access_to_SlotSPA_Page(self):
        print("<li>" + "Click on Spade Gaming" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(SlotElement.spade_gaming_button).click()

    def Click_on_SlotSPA_Game(self):
        print("<li>" + "Click on a Spade Gaming game in the list" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(SlotElement.single_game).click()

    def Access_to_SlotSBO_Page(self):
        print("<li>" + "Click on SBO" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(SlotElement.sbo_gaming_button).click()

    def Click_on_SlotSBO_Game(self):
        print("<li>" + "Click on a SBO game in the list: " + str(SlotData.loopran_sbo) + "</li>" + "<br>")
        self.driver.find_element_by_xpath(SlotElement.sbo_game).click()

    def Access_to_SlotBigGaming_Page(self):
        print("<li>" + "Click on Big Gaming" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(SlotElement.big_gaming_button).click()

    def Click_on_SlotBigGaming_Game(self):
        print("<li>" + "Click on a Big Gaming game in the list: " + str(SlotData.loopran_big) + "</li>" + "<br>")
        self.driver.find_element_by_xpath(SlotElement.big_game).click()

    def Access_to_SlotIGS_Page(self):
        print("<li>" + "Click on IGS" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(SlotElement.igs_button).click()

    def Click_on_SlotIGS_Game(self):
        print("<li>" + "Click on an IGS game in the list: " + str(SlotData.loopran_igs) + "</li>" + "<br>")
        self.driver.find_element_by_xpath(SlotElement.igs_game).click()

    def Access_to_SportCMD_Page(self):
        print("<li>" + "Click on CMD" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(SportElement.cmd_button).click()

    def Click_on_SportCMD_Game(self):
        print("<li>" + "Click on a CMD game in the list" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(SportElement.single_game).click()

    def Access_to_SportSBO_Page(self):
        print("<li>" + "Click on SBO" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(SportElement.sbo_button).click()

    def Click_on_SportSBO_Game(self):
        print("<li>" + "Click on a SBO game in the list: " + str(SportData.loopran_sbo) + "</li>" + "<br>")
        self.driver.find_element_by_xpath(SportElement.sbo_game).click()

    def Access_to_SportIBC_Page(self):
        print("<li>" + "Click on IBC" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(SportElement.ibc_button).click()

    def Click_on_SportIBC_Game(self):
        print("<li>" + "Click on an IBC game in the list" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(SportElement.single_game).click()

    def Access_to_SportM8_Page(self):
        print("<li>" + "Click on M8 Sports" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(SportElement.m8_sports_button).click()

    def Click_on_SportM8_Game(self):
        print("<li>" + "Click on a M8 Sports game in the list" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(SportElement.single_game).click()

    def Assert_Login_Page(self):
        # Wait modal dialog load
        wait_page_load = EC.presence_of_element_located((By.CLASS_NAME, ProvidersElement.log_in_button))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        loginpage = self.driver.find_element_by_class_name(ProvidersElement.log_in_button).is_displayed()
        self.assertTrue(loginpage, "User is not being navigated to login page.")

    def Assert_Quick_Transfer(self):
        # Wait modal dialog load
        wait_page_load = EC.element_to_be_clickable((By.XPATH, ProvidersElement.enter_the_game_button))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        quick_transfer = self.driver.find_element_by_xpath(ProvidersElement.enter_the_game_button).is_displayed()
        self.assertTrue(quick_transfer, "Quick Transfer Modal Dialog is not displayed.")

    def Enter_Game(self):
        # Verify Old Tab
        window_before = self.driver.window_handles[0]
        print("<li>" + "Click on Enter Game button" + "</li>" + "<br>")
        wait_enter_game = EC.element_to_be_clickable((By.XPATH, ProvidersElement.enter_the_game_button))
        WebDriverWait(self.driver, 20).until(wait_enter_game)
        click_enter = self.driver.find_element_by_xpath(ProvidersElement.enter_the_game_button).click()
        waitnewpage = EC.new_window_is_opened(self.driver.window_handles)
        WebDriverWait(self.driver, 30).until(waitnewpage)
        # Verify New Tab
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.implicitly_wait(10)
        # Assert Gaming Page
        game_url = self.driver.current_url
        r = requests.get(game_url)
        page_status = r.status_code
        print("The gaming page status is: " + str(page_status) + "<br>")
        self.assertEqual(page_status, 200, "Unable to access to gaming page.")

    def Quick_Transfer(self):
        # Find the initial amount
        ini_exist_amount = self.driver.find_element_by_xpath(ProvidersElement.main_wallet_amount).text
        print("Initial Amount in Account: " + str(ini_exist_amount) + "<br>")
        ini_game_amount = self.driver.find_element_by_xpath(ProvidersElement.game_amount).text
        print("Initial Amount in Game: " + str(ini_game_amount) + "<br>")
        print("<li>" + "Insert Transfer Amount: " + ProvidersData.quick_transfer_amount + "</li>" + "<br>")
        self.driver.find_element_by_xpath(ProvidersElement.transfer_amount_field).send_keys(ProvidersData.quick_transfer_amount)
        time.sleep(1)
        print("<li>" + "Click on Quick Transfer button" + "</li>" + "<br>")
        wait_page_load = EC.element_to_be_clickable((By.CLASS_NAME, ProvidersElement.quick_transfer_button))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_class_name(ProvidersElement.quick_transfer_button).click()
        # Switch the control to the Alert window
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        registration_prompt = self.driver.switch_to.alert
        # Retrieve the message on the Alert window
        prompt_message = registration_prompt.text
        print("Alert shows following message: " + prompt_message + "<br>")
        # Click on the OK button (Accept)
        print("<li>" + "Click on OK button" + "</li>" + "<br>")
        registration_prompt.accept()
        # Wait page to load
        time.sleep(5)
        # Find the final amount
        final_exist_amount = self.driver.find_element_by_xpath(ProvidersElement.main_wallet_amount).text
        print("Final Amount in Account: " + str(final_exist_amount) + "<br>")
        final_game_amount = self.driver.find_element_by_xpath(ProvidersElement.game_amount).text
        print("Final Amount in Game: " + str(final_game_amount) + "<br>")
        self.assertTrue(ini_exist_amount > final_exist_amount, "Unable to perform quick transfer")
        self.assertTrue(final_game_amount > ini_game_amount, "Unable to perform quick transfer")
