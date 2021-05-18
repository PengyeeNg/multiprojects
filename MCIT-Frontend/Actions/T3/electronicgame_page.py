from Setup.T3 import Base_Setup
from Elements.T3.electronicgame_page import ElectronicGameElement
from Input_Data.T3.electronicgame_page import ElectronicGameData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import requests
import time

class ElectronicGamepageActions(Base_Setup.BSetup):

    def Click_Next(self):
        for j in range(0, 3, 1):
            self.driver.find_element_by_xpath(ElectronicGameElement.next_button).click()
            self.driver.implicitly_wait(10)

    def Access_to_ElectronicGame_Tab(self):
        print("<li>" + "Click on Electronic Game tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(ElectronicGameElement.electronicgame_tab).click()
        # Wait modal dialog load
        wait_page_load = EC.element_to_be_clickable((By.XPATH, ElectronicGameElement.next_button))
        WebDriverWait(self.driver, 20).until(wait_page_load)


    def Access_to_EvolutionGaming_Page(self):
        print("<li>" + "Click on Evolution Gaming tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(ElectronicGameElement.evo_gaming_button).click()

    def Access_to_SpadeGaming_Page(self):
        print("<li>" + "Click on Spade Gaming tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(ElectronicGameElement.spade_gaming_button).click()

    def Access_to_CMD_Page(self):
        print("<li>" + "Click on CMD tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(ElectronicGameElement.cmd_button).click()

    def Access_to_SBO_Page(self):
        print("<li>" + "Click on SBO tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(ElectronicGameElement.sbo_button).click()

    def Access_to_BigGaming_Page(self):
        print("<li>" + "Click on Big Gaming tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(ElectronicGameElement.big_gaming_button).click()

    def Access_to_IBC_Page(self):
        print("<li>" + "Click on IBC tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(ElectronicGameElement.ibc_button).click()

    def Access_to_M8Sports_Page(self):
        print("<li>" + "Click on M8 Sports tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(ElectronicGameElement.m8sports_button).click()

    def Access_to_IGS_Page(self):
        print("<li>" + "Click on IGS tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(ElectronicGameElement.igs_button).click()

    def Access_to_WMCasino_Page(self):
        print("<li>" + "Click on WM Casino tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(ElectronicGameElement.wmcasino_button).click()

    def Access_to_NextSpin_Page(self):
        print("<li>" + "Click on NextSpin tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(ElectronicGameElement.nextspin_button).click()

    def Assert_Login_Reminder(self):
        # Wait modal dialog load
        wait_page_load = EC.element_to_be_clickable((By.CLASS_NAME, ElectronicGameElement.login_reminder_confirm_button))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        login_reminder_modal_dialog = self.driver.find_element_by_class_name(ElectronicGameElement.login_reminder_confirm_button).is_displayed()
        self.assertTrue(login_reminder_modal_dialog, "Login reminder is not displayed.")

    def Assert_Quick_Transfer(self):
        # Wait modal dialog load
        wait_page_load = EC.element_to_be_clickable((By.CLASS_NAME, ElectronicGameElement.enter_the_game_button))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        quick_transfer = self.driver.find_element_by_class_name(ElectronicGameElement.enter_the_game_button).is_displayed()
        self.assertTrue(quick_transfer, "Quick Transfer Modal Dialog is not displayed.")

    def Enter_Game(self):
        # Verify Old Tab
        window_before = self.driver.window_handles[0]
        print("<li>" + "Click on Enter Game button" + "</li>" + "<br>")
        wait_enter_game = EC.element_to_be_clickable((By.CLASS_NAME, ElectronicGameElement.enter_the_game_button))
        WebDriverWait(self.driver, 20).until(wait_enter_game)
        click_enter = self.driver.find_element_by_class_name(ElectronicGameElement.enter_the_game_button).click()
        self.driver.implicitly_wait(10)
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
        ini_exist_amount = self.driver.find_element_by_xpath(ElectronicGameElement.ini_exist_amount).text
        print("Initial Amount in Account: " + str(ini_exist_amount) + "<br>")
        ini_game_amount = self.driver.find_element_by_xpath(ElectronicGameElement.ini_game_amount).text
        print("Initial Amount in Game: " + str(ini_game_amount) + "<br>")
        print("<li>" + "Insert Transfer Amount: " + ElectronicGameData.quick_transfer_amount + "</li>" + "<br>")
        self.driver.find_element_by_id(ElectronicGameElement.quick_transfer_amount_field).send_keys(ElectronicGameData.quick_transfer_amount)
        print("<li>" + "Click on Quick Transfer button" + "</li>" + "<br>")
        wait_page_load = EC.element_to_be_clickable((By.CLASS_NAME, ElectronicGameElement.quick_transfer_button))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_class_name(ElectronicGameElement.quick_transfer_button).click()
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
        final_exist_amount = self.driver.find_element_by_xpath(ElectronicGameElement.ini_exist_amount).text
        print("Final Amount in Account: " + str(final_exist_amount) + "<br>")
        final_game_amount = self.driver.find_element_by_xpath(ElectronicGameElement.ini_game_amount).text
        print("Final Amount in Game: " + str(final_game_amount) + "<br>")
        self.assertTrue(ini_exist_amount > final_exist_amount, "Unable to perform quick transfer")
        self.assertTrue(final_game_amount > ini_game_amount, "Unable to perform quick transfer")




