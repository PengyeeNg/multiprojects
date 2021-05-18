import unittest
from Input_Data.promotion_page import Promotion_Mission_Data
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import SetUp.Base_SetUp
from Actions.main_page import General_Actions
from Elements.promotion_page import Promotion_Mission_Element
from Elements.main_page import General_Element
from Actions.promotion_page import Promotion_Mission_Actions

class Promotion_Mission(SetUp.Base_SetUp.BSetUp):

    def test_TC_Promotion_Mission_01_Lock_Member_Promotion(self):
        Promotion_Mission_Actions.Navigate_Promotion_Mission(self)
        # Scroll page to the bottom
        scroll_to_bottom = self.driver.find_element_by_class_name(Promotion_Mission_Element.scroll_to_bottom)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll_to_bottom)
        actions.perform()
        # Move the slidebar
        slide_bar = self.driver.find_element_by_class_name(Promotion_Mission_Element.slide_bar)
        move = ActionChains(self.driver)
        move.click_and_hold(slide_bar).move_by_offset(300, 0).release().perform()
        self.driver.implicitly_wait(30)
        # Wait till button is clickable
        wait_lock_button = EC.element_to_be_clickable((By.CLASS_NAME, Promotion_Mission_Element.lock_button))
        WebDriverWait(self.driver, 10).until(wait_lock_button)
        print("<li>" + "Click on Lock button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Promotion_Mission_Element.lock_button).click()
        # Assert Change dialog is displayed
        wait_lock_change_dialog_box = EC.presence_of_element_located((By.XPATH, Promotion_Mission_Element.lock_change_submit_button))
        WebDriverWait(self.driver, 10).until(wait_lock_change_dialog_box)
        lock_change_dialog_box = self.driver.find_element_by_xpath(Promotion_Mission_Element.lock_change_submit_button).is_displayed()
        self.assertTrue(lock_change_dialog_box, "User is not able to access to lock Member Promotion.")
        print("Expected Results: Change dialog box popped out." + "<br>")

    def test_TC_Promotion_Mission_02_Cancel_Member_Promotion(self):
        Promotion_Mission_Actions.Navigate_Promotion_Mission(self)
        # Scroll page to the bottom
        scroll_to_bottom = self.driver.find_element_by_class_name(Promotion_Mission_Element.scroll_to_bottom)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll_to_bottom)
        actions.perform()
        # Move the slidebar
        slide_bar = self.driver.find_element_by_class_name(Promotion_Mission_Element.slide_bar)
        move = ActionChains(self.driver)
        move.click_and_hold(slide_bar).move_by_offset(300, 0).release().perform()
        self.driver.implicitly_wait(30)
        # Wait till button is clickable
        wait_cancel_button = EC.element_to_be_clickable((By.CLASS_NAME, Promotion_Mission_Element.cancel_promotion_button))
        WebDriverWait(self.driver, 10).until(wait_cancel_button)
        print("<li>" + "Click on Delete button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Promotion_Mission_Element.cancel_promotion_button).click()
        # Assert Change dialog is displayed
        wait_lock_change_dialog_box = EC.presence_of_element_located((By.XPATH, Promotion_Mission_Element.lock_change_submit_button))
        WebDriverWait(self.driver, 10).until(wait_lock_change_dialog_box)
        lock_change_dialog_box = self.driver.find_element_by_xpath(Promotion_Mission_Element.lock_change_submit_button).is_displayed()
        self.assertTrue(lock_change_dialog_box, "User is not able to access to cancel Member Promotion.")
        print("Expected Results: Cancel dialog box popped out." + "<br>")

    def test_TC_Promotion_Mission_03_Search_Member_Promotion(self):
        Promotion_Mission_Actions.Navigate_Promotion_Mission(self)
        print("<li>" + "Insert Member Name = ABCDEFGSELENIUM" + "</li>" + "<br>")
        self.driver.find_element_by_id(Promotion_Mission_Element.member_filter_field).send_keys(Promotion_Mission_Data.member_name_filter)
        print("<li>" + "Click on Search button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(General_Element.filter_search_button).click()
        # Assert
        General_Actions.Assert_Filter_Results(self)

    def test_TC_List_Promotion_Mission_04_Table_Sorting_Member_Promotion(self):
        Promotion_Mission_Actions.Navigate_Promotion_Mission(self)
        print("<li>" + "Click on Target header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Promotion_Mission_Element.target_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Target Date header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Promotion_Mission_Element.target_date_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Transfer in header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Promotion_Mission_Element.transfer_in_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Transfer Out header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Promotion_Mission_Element.transfer_out_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Check Date header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Promotion_Mission_Element.check_date_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Status header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Promotion_Mission_Element.status_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Lock header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Promotion_Mission_Element.lock_header_sorting).click()
        self.driver.implicitly_wait(30)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Member Promotion", "Page breaks after clicking table sorting.")
        print("Expected Results: Page does not break after clicking table sorting." + "<br>")

    def test_TC_List_Promotion_Mission_05_View_All_Member_Promotion(self):
        Promotion_Mission_Actions.Navigate_Promotion_Mission(self)
        General_Actions.view_all(self)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Member Promotion", "Page breaks after clicking All button.")
        print("Expected Results: Page does not break after clicking All button." + "<br>")

if __name__ == '__main__':
    unittest.main()
