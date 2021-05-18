import unittest
import SetUp.Base_SetUp
from Actions.rebate_page import Rebate_Setting_Actions
from Actions.rebate_page import Rebate_Actions
from Elements.rebate_page import Rebate_Setting_Element
from Elements.rebate_page import Rebate_Element
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Input_Data.rebate_page import Rebate_Data
from selenium.webdriver.common.keys import Keys


class Rebate_Setting(SetUp.Base_SetUp.BSetUp):

    def test_TC_Rebate_01_Create_Rebate(self):
        Rebate_Setting_Actions.Navigate_Rebate_Setting(self)
        window_before = self.driver.window_handles[0]
        print("<li>" + "Click on Add button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Rebate_Setting_Element.add_rebate_button).click()
        # get the window handle after a new window has opened
        window_after = self.driver.window_handles[1]
        # switch on to new child window
        self.driver.switch_to.window(window_after)
        self.driver.maximize_window()
        # Wait till page load
        wait_page_load = EC.presence_of_element_located((By.CLASS_NAME, Rebate_Setting_Element.create_rebate_submit_button))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        # Assert
        add_announcement_page = self.driver.title
        self.assertEqual(add_announcement_page, "Create Rebate", "User is not able to access to Create Rebate Page.")
        print("Expected Results: Create Rebate page displayed in new tab." + "<br>")

    def test_TC_Rebate_02_Update_Rebate(self):
        Rebate_Setting_Actions.Navigate_Rebate_Setting(self)
        print("<li>" + "Click on Edit button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Rebate_Setting_Element.edit_rebate_button).click()
        # Wait till page load
        wait_page_load = EC.presence_of_element_located((By.CLASS_NAME, Rebate_Setting_Element.update_rebate_submit_button))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        # Assert
        add_announcement_page = self.driver.title
        self.assertEqual(add_announcement_page, "Update Rebate", "User is not able to access to Update Rebate Page.")
        print("Expected Results: Navigated to Edit Rebate page." + "<br>")

    def test_TC_Rebate_03_View_All_Rebate(self):
        Rebate_Setting_Actions.Navigate_Rebate_Setting(self)
        Rebate_Actions.View_All(self)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Rebate setting", "Page breaks after clicking All button.")
        print("Expected Results: Page does not break after clicking All button." + "<br>")

    def test_TC_Rebate_04_Filter_Rebate(self):
        Rebate_Setting_Actions.Navigate_Rebate_Setting(self)
        self.driver.find_element_by_id(Rebate_Setting_Element.start_date_filter_field).send_keys(Rebate_Data.start_date_filter)
        self.driver.find_element_by_id(Rebate_Setting_Element.start_date_filter_field).send_keys(Keys.RETURN)
        self.driver.find_element_by_id(Rebate_Setting_Element.close_date_filter_field).send_keys(Rebate_Data.close_date_filter)
        self.driver.find_element_by_id(Rebate_Setting_Element.close_date_filter_field).send_keys(Keys.RETURN)
        self.driver.find_element_by_class_name(Rebate_Element.search_filter_button).click()
        self.driver.implicitly_wait(30)
        # Assert
        Rebate_Actions.Assert_Search_results(self)

    def test_TC_Rebate_05_Table_Sorting_Rebate(self):
        Rebate_Setting_Actions.Navigate_Rebate_Setting(self)
        print("<li>" + "Click on Code header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Rebate_Setting_Element.code_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Provider header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Rebate_Setting_Element.provider_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Percentage header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Rebate_Setting_Element.percentage_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Created Time header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Rebate_Setting_Element.created_time_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Category header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Rebate_Setting_Element.category_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Status header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Rebate_Setting_Element.status_header_sorting).click()
        self.driver.implicitly_wait(30)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Rebate setting", "Page breaks after clicking table sorting.")
        print("Expected Results: Page does not break after clicking table sorting." + "<br>")

if __name__ == '__main__':
    unittest.main()
