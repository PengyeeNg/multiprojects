from selenium.webdriver import ActionChains

import SetUp.Base_SetUp
from Elements.main_page import MainPage_Element
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Elements.main_page import General_Element
from Elements.member_page import Member_Element
from selenium.webdriver.common.by import By

class MainPage_Actions(SetUp.Base_SetUp.BSetUp):
    def find_pagename(self):
        self.driver.find_element_by_xpath(MainPage_Element.main_page_title)

    def click_username_dropdown(self):
        self.driver.find_element_by_xpath(MainPage_Element.username_dropdown).click()

    def click_change_password(self):
        self.driver.find_element_by_xpath(MainPage_Element.change_password_button).click()

    def navigated_change_password_page(self):
        print("<li>" + "Click on the username dropdown" + "</li>" + "<br>")
        MainPage_Actions.click_username_dropdown(self)
        print("<li>" + "Click on 'Change Password' button" + "</li>" + "<br>")
        MainPage_Actions.click_change_password(self)
        # Verify navigate to change password page
        change_password = EC.presence_of_element_located((By.XPATH, MainPage_Element.change_button))
        WebDriverWait(self.driver, 10).until(change_password)
        change_password_page = self.driver.find_element_by_xpath(MainPage_Element.change_button).is_displayed()
        self.assertTrue(change_password_page, "User is not able to access to Change Password Page.")

    def click_change_button(self):
        self.driver.find_element_by_xpath(MainPage_Element.change_button).click()

class General_Actions(SetUp.Base_SetUp.BSetUp):
    def view_all(self):
        # Wait till button is clickable
        wait_all_button = EC.element_to_be_clickable((By.CLASS_NAME, General_Element.all_button))
        WebDriverWait(self.driver, 30).until(wait_all_button)
        print("<li>" + "Click on All button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(General_Element.all_button).click()
        self.driver.implicitly_wait(30)
        # Wait till the text changed
        # load_data = EC.text_to_be_present_in_element((By.ID, General_Element.all_button, "Page"))
        # WebDriverWait(self.driver, 50).until(load_data)
        # Assert All changed to Page
        # page_button = self.driver.find_element_by_id(General_Element.all_button).Text
        # self.assertEqual(page_button, "Page", "User is not able to view all")
        # print("Expected Results: Page does not break after clicking All button." + "<br>")

    def Assert_Delete_Confirmation_Dialog(self):
        # Wait till delete confirmation dialog box displayed
        wait_load_dialog = EC.presence_of_element_located((By.CLASS_NAME, General_Element.delete_confirmation_dialog_box))
        WebDriverWait(self.driver, 15).until(wait_load_dialog)
        # Assert Delete Confirmation is displayed
        delete_confirmation = self.driver.find_element_by_class_name(General_Element.delete_confirmation_dialog_box).is_displayed()
        self.assertTrue(delete_confirmation, "Delete Confirmation Dialog Box is not displayed.")
        print("Expected Results: Delete Confirmation Dialog Box is displayed." + "<br>")

    def Assert_Filter_Results(self):
        # Verify filter results
        filtered_results = EC.text_to_be_present_in_element((By.CSS_SELECTOR, Member_Element.filtered_results), "No results found.")
        WebDriverWait(self.driver, 10).until(filtered_results)
        print("Expected Results: Filtered results = No results found." + "<br>")

    def Scroll_Page_to_Bottom(self):
        # Scroll page to the bottom
        scroll_to_bottom = self.driver.find_element_by_class_name(General_Element.scroll_to_bottom)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll_to_bottom)
        actions.perform()



