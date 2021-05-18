import unittest
import SetUp.Base_SetUp
from Actions.referral_page import Member_Map_Actions
from Elements.referral_page import Member_Map_Element
from Elements.referral_page import Referral_Element
from Input_Data.referral_page import Referral_Data
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class Member_Map(SetUp.Base_SetUp.BSetUp):

    def test_TC_Member_Map_01_Filter_Member_Map(self):
        Member_Map_Actions.Navigate_New_Member_Map(self)
        self.driver.find_element_by_id(Member_Map_Element.username_filter_field).send_keys(Referral_Data.username_filter)
        self.driver.find_element_by_class_name(Referral_Element.search_filter_button).click()
        # Wait filter
        wait_filter = EC.invisibility_of_element_located((By.CLASS_NAME, Member_Map_Element.filter_no_result))
        WebDriverWait(self.driver, 10).until(wait_filter)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Relationship Member Map", "Page breaks after clicking Search button.")
        print("Expected Results: Page does not break after clicking Search button." + "<br>")

    def test_TC_Member_Map_02_Transfer_Member(self):
        Member_Map_Actions.Navigate_New_Member_Map(self)
        self.driver.find_element_by_id(Member_Map_Element.transfer_username_filter_field).send_keys(Referral_Data.transfer_username_filter)
        self.driver.find_element_by_id(Member_Map_Element.transfer_membership_number_field).send_keys(Referral_Data.transfer_membership_number_filter)
        self.driver.find_element_by_class_name(Member_Map_Element.transfer_button).click()
        # Wait filter
        wait_transfer_failed_alert = EC.presence_of_element_located((By.ID, Member_Map_Element.transfer_failed_alert))
        WebDriverWait(self.driver, 10).until(wait_transfer_failed_alert)
        # Assert
        transfer_failed_alert = self.driver.find_element_by_id(Member_Map_Element.transfer_failed_alert).is_displayed()
        self.assertTrue(transfer_failed_alert, "Transfer failed is not detected")
        print("Expected Results: Transfer failed: This Member Cannot Find." + "<br>")


if __name__ == '__main__':
    unittest.main()
