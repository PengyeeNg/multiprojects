import unittest
from Actions.T3.user_page import UserpageActions
from Elements.T3.user_page import UserElement
from Input_Data.T3.user_page import UserData
from Setup.T3 import Base_Setup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

class QuotaConversionModule(Base_Setup.BSetup):

    def TC_QuotaConversion_01_Navigate_to_AnnouncementPage(self):
        print("<b> Expected Results: Able to access to announcement page. </b>" + "<br>")
        UserpageActions.Access_to_Quota_Conversion(self)

    def TC_QuotaConversion_02_Access_to_Withdrawal_Page(self):
        print("<b> Expected Results: Able to access to Withdrawal page from Announcement. </b>" + "<br>")
        UserpageActions.Access_to_Quota_Conversion(self)
        print("<li>" + "Click on Withdrawal button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(UserElement.quotaconversion_withdrawal_button).click()
        # Wait page load
        wait_page_load = EC.presence_of_element_located((By.XPATH, UserElement.withdrawal_area_element))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        page_loaded = self.driver.find_element_by_xpath(UserElement.withdrawal_area_element).is_displayed()
        self.assertTrue(page_loaded, "User is not able to access to Withdrawal Page from Announcement.")

    def TC_QuotaConversion_03_Access_to_Deposit_Page(self):
        print("<b> Expected Results: Able to access to Deposit page from Announcement. </b>" + "<br>")
        UserpageActions.Access_to_Quota_Conversion(self)
        print("<li>" + "Click on Deposit button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(UserElement.quotaconversion_deposit_button).click()
        # Wait page load
        wait_page_load = EC.presence_of_element_located((By.XPATH, UserElement.deposit_area_element))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        page_loaded = self.driver.find_element_by_xpath(UserElement.deposit_area_element).is_displayed()
        self.assertTrue(page_loaded, "User is not able to access to Withdrawal Page from Announcement.")

    def test_TC_QuotaConversion_04_Perform_Transfer(self):
        print("<b> Expected Results: Able to perform transfer. </b>" + "<br>")
        UserpageActions.Access_to_Quota_Conversion(self)
        time.sleep(5)
        # Find initial amount
        ini_accamount = self.driver.find_element_by_xpath(UserElement.quotaconversion_accamount).text
        ini_evoamount = self.driver.find_element_by_xpath(UserElement.quotaconversion_evoamount).text
        print("Initial Acc Amount: " + str(ini_accamount) + "<br>")
        print("Initial Evo Amount: " + str(ini_evoamount) + "<br>")
        print("<li>" + "Insert transfer amount: " + str(UserData.announcement_transfer_amount) + "</li>" + "<br>")
        self.driver.find_element_by_id(UserElement.quotaconversion_amount_field).send_keys(UserData.announcement_transfer_amount)
        time.sleep(1)
        print("<li>" + "Click on Confirm Transfer button" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserElement.quotaconversion_confirm_transfer_button).click()
        # Wait till alert is present
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        # Switch the control to the Alert window
        registration_prompt = self.driver.switch_to.alert
        # Retrieve the message on the Alert window
        prompt_message = registration_prompt.text
        print("Alert shows following message: " + prompt_message + "<br>")
        # self.assertNotEqual(prompt_message, "Error", "Errors occured.")
        # Assert
        time.sleep(5)
        # Find final amount
        final_accamount = self.driver.find_element_by_xpath(UserElement.quotaconversion_accamount).text
        final_evoamount = self.driver.find_element_by_xpath(UserElement.quotaconversion_evoamount).text
        print("Final Acc Amount: " + str(final_accamount) + "<br>")
        print("Final Evo Amount: " + str(final_evoamount) + "<br>")
        self.assertTrue(final_evoamount > ini_evoamount, "Unable to perform transfer.")
        self.assertTrue(final_accamount < ini_accamount, "Unable to perform transfer.")







if __name__ == '__main__':
    unittest.main()

