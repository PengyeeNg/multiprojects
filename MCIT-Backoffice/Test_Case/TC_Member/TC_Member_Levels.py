import unittest
import SetUp.Base_SetUp
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Actions.main_page import General_Actions
from Actions.member_page import Member_Levels_Actions
from Elements.member_page import Member_Levels_Element

class Member_Levels(SetUp.Base_SetUp.BSetUp):

    def test_TC_Member_Levels_01_Add_Member_Levels(self):
        Member_Levels_Actions.Navigate_Member_Levels(self)
        print("<li>" + "Click on add button" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Levels_Element.add_member_level_button).click()
        # Wait till the page Load
        wait_load_page = EC.presence_of_element_located((By.ID, Member_Levels_Element.add_member_level_submit_button))
        WebDriverWait(self.driver, 10).until(wait_load_page)
        # Assert page is loaded
        add_member_levels_page = self.driver.title
        self.assertEqual(add_member_levels_page, "Member Levels", "User is not able to navigate to Add Member Levels Page.")
        print("Expected Results: Navigated to Add Member Levels page." + "<br>")

    def test_TC_Member_Levels_02_Edit_Member_Levels(self):
        Member_Levels_Actions.Navigate_Member_Levels(self)
        print("<li>" + "Click on edit button" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Levels_Element.edit_member_level_edit_button).click()
        # Wait till the page Load
        wait_load_page = EC.presence_of_element_located((By.ID, Member_Levels_Element.add_member_level_submit_button))
        WebDriverWait(self.driver, 10).until(wait_load_page)
        # Assert page is loaded
        edit_member_levels_page = self.driver.title
        self.assertEqual(edit_member_levels_page, "Member Levels", "User is not able to navigate to Edit Member Levels Page.")
        print("Expected Results: Navigated to Edit Member Levels page." + "<br>")

    def test_TC_Member_Levels_03_Delete_Member_Levels(self):
        Member_Levels_Actions.Navigate_Member_Levels(self)
        print("<li>" + "Click on delete button" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Levels_Element.delete_member_level_button).click()
        # Wait and assert delete confirmation dialog box displayed
        General_Actions.Assert_Delete_Confirmation_Dialog(self)

    def test_TC_Member_Levels_04_Setting_Rebate(self):
        Member_Levels_Actions.Navigate_Member_Levels(self)
        print("<li>" + "Click on Setting Rebate button" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Levels_Element.setting_rebate_button).click()
        # Wait till prompt page displayed
        wait_load_prompt = EC.presence_of_element_located((By.XPATH, Member_Levels_Element.setting_rebate_submit_button))
        WebDriverWait(self.driver, 10).until(wait_load_prompt)
        # Assert prompt page displayed
        edit_prompt = self.driver.find_element_by_xpath(Member_Levels_Element.setting_rebate_submit_button).is_displayed()
        self.assertTrue(edit_prompt, "Edit Dialog Box is not displayed.")
        print("Expected Results: Edit Dialog Box popped out." + "<br>")

    def test_TC_Member_Levels_05_View_All_Member_Levels(self):
        Member_Levels_Actions.Navigate_Member_Levels(self)
        print("<li>" + "Click on All button" + "</li>" + "<br>")
        self.driver.find_element_by_id(Member_Levels_Element.all_button_member_levels).click()
        self.driver.implicitly_wait(30)
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Member Levels", "Page breaks after clicking All button.")
        print("Expected Results: Page does not break after clicking All button." + "<br>")


if __name__ == '__main__':
    unittest.main()
