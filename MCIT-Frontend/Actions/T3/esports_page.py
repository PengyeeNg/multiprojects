from Setup.T3 import Base_Setup
from Elements.T3.esports_page import ESportsElement
from Input_Data.T3.esports_page import ESportsData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import requests
import time

class EsportspageActions(Base_Setup.BSetup):

    def Access_to_E_Sports_Tab(self):
        print("<li>" + "Click on E Sports tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(ESportsElement.esports_tab).click()
        # Wait modal dialog load
        wait_page_load = EC.presence_of_element_located((By.XPATH, ESportsElement.cmd_game))
        WebDriverWait(self.driver, 20).until(wait_page_load)

    def Access_to_CMD_Page(self):
        print("<li>" + "Click on CMD" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(ESportsElement.cmd_game).click()

    def Access_to_SportsBook_Page(self):
        print("<li>" + "Click on Sports Book" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(ESportsElement.sportsbook_game).click()

    def Access_to_VirtualSports_Page(self):
        print("<li>" + "Click on Virtual Sports" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(ESportsElement.virtualsports_game).click()

    def Access_to_IBC_Page(self):
        print("<li>" + "Click on IBC" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(ESportsElement.ibc_game).click()

    def Access_to_M8Sports_Page(self):
        print("<li>" + "Click on M8 Sports" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(ESportsElement.m8_sports).click()

    def Assert_Login_Reminder(self):
        # Wait modal dialog load
        wait_page_load = EC.element_to_be_clickable((By.CLASS_NAME, ESportsElement.login_reminder_confirm_button))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        login_reminder_modal_dialog = self.driver.find_element_by_class_name(ESportsElement.login_reminder_confirm_button).is_displayed()
        self.assertTrue(login_reminder_modal_dialog, "Login reminder is not displayed.")

    def Assert_Quick_Transfer(self):
        # Wait modal dialog load
        wait_page_load = EC.element_to_be_clickable((By.CLASS_NAME, ESportsElement.enter_the_game_button))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        quick_transfer = self.driver.find_element_by_class_name(ESportsElement.enter_the_game_button).is_displayed()
        self.assertTrue(quick_transfer, "Quick Transfer Modal Dialog is not displayed.")

    def Enter_Game(self):
        # Verify Old Tab
        window_before = self.driver.window_handles[0]
        print("<li>" + "Click on Enter Game button" + "</li>" + "<br>")
        wait_enter_game = EC.element_to_be_clickable((By.CLASS_NAME, ESportsElement.enter_the_game_button))
        WebDriverWait(self.driver, 20).until(wait_enter_game)
        click_enter = self.driver.find_element_by_class_name(ESportsElement.enter_the_game_button).click()
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
        ini_exist_amount = self.driver.find_element_by_xpath(ESportsElement.ini_exist_amount).text
        print("Initial Amount in Account: " + str(ini_exist_amount) + "<br>")
        ini_game_amount = self.driver.find_element_by_xpath(ESportsElement.ini_game_amount).text
        print("Initial Amount in Game: " + str(ini_game_amount) + "<br>")
        print("<li>" + "Insert Transfer Amount: " + ESportsData.quick_transfer_amount + "</li>" + "<br>")
        self.driver.find_element_by_id(ESportsElement.quick_transfer_amount_field).send_keys(ESportsData.quick_transfer_amount)
        time.sleep(1)
        print("<li>" + "Click on Quick Transfer button" + "</li>" + "<br>")
        wait_page_load = EC.element_to_be_clickable((By.CLASS_NAME, ESportsElement.quick_transfer_button))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_class_name(ESportsElement.quick_transfer_button).click()
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
        final_exist_amount = self.driver.find_element_by_xpath(ESportsElement.ini_exist_amount).text
        print("Final Amount in Account: " + str(final_exist_amount) + "<br>")
        final_game_amount = self.driver.find_element_by_xpath(ESportsElement.ini_game_amount).text
        print("Final Amount in Game: " + str(final_game_amount) + "<br>")
        self.assertTrue(ini_exist_amount > final_exist_amount, "Unable to perform quick transfer")
        self.assertTrue(final_game_amount > ini_game_amount, "Unable to perform quick transfer")


