import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import SetUp.Base_SetUp
from Actions.main_page import General_Actions
from Actions.promotion_page import Promotion_Banner_Actions
from Elements.promotion_page import Promotion_Banner_Element
from Input_Data.promotion_page import Promotion_Banner_Data

class Promotion_Banner(SetUp.Base_SetUp.BSetUp):

    def TC_List_Promotion_Banner_01_Add_Activity_Announcement_List(self):
        Promotion_Banner_Actions.Navigate_Promotion_Banner(self)
        window_before = self.driver.window_handles[0]
        print("<li>" + "Click on add icon" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Promotion_Banner_Element.add_announcement_button).click()
        # get the window handle after a new window has opened
        window_after = self.driver.window_handles[1]
        # switch on to new child window
        self.driver.switch_to.window(window_after)
        self.driver.maximize_window()
        # Wait till page load
        wait_page_load = EC.presence_of_element_located((By.CLASS_NAME, Promotion_Banner_Element.add_announcement_page_element))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        # Assert
        add_announcement_page = self.driver.title
        self.assertEqual(add_announcement_page, "New", "User is not able to access to Add Announcement Page.")
        print("Expected Results: Add Activity Announcement page displayed in new tab." + "<br>")

    def TC_List_Promotion_Banner_02_Edit_Activity_Announcement_List(self):
        Promotion_Banner_Actions.Navigate_Promotion_Banner(self)
        print("<li>" + "Click on edit icon" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Promotion_Banner_Element.edit_announcement_icon).click()
        # Wait till page load
        wait_page_load = EC.presence_of_element_located((By.CLASS_NAME, Promotion_Banner_Element.add_announcement_page_element))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        # Assert
        add_announcement_page = self.driver.title
        self.assertEqual(add_announcement_page, "New", "User is not able to access to Edit Announcement Page.")
        print("Expected Results: Navigated to Edit Activity Announcement page." + "<br>")

    def TC_List_Promotion_Banner_03_Delete_Activity_Announcement_List(self):
        Promotion_Banner_Actions.Navigate_Promotion_Banner(self)
        print("<li>" + "Click on delete icon" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Promotion_Banner_Element.delete_announcement_icon).click()
        # Assert
        General_Actions.Assert_Delete_Confirmation_Dialog(self)
        print("Expected Results: Delete Confirmation Dialog Box popped out." + "<br>")

    def TC_List_Promotion_Banner_04_Search_Activity_Announcement_List(self):
        Promotion_Banner_Actions.Navigate_Promotion_Banner(self)
        print("<li>" + "Insert Title" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Promotion_Banner_Element.title_filter_field).send_keys(Promotion_Banner_Data.title_filter)
        print("<li>" + "Click on Search button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Promotion_Banner_Element.search_filter_button).click()
        # Assert
        General_Actions.Assert_Filter_Results(self)

    def TC_List_Promotion_Banner_05_Table_Sorting_Activity_Announcement_List(self):
        Promotion_Banner_Actions.Navigate_Promotion_Banner(self)
        print("<li>" + "Click on ID header" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Promotion_Banner_Element.id_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Title header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Promotion_Banner_Element.title_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on State header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Promotion_Banner_Element.state_header_sorting).click()
        self.driver.implicitly_wait(30)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Activity Announcement List", "Page breaks after clicking table sorting.")
        print("Expected Results: Page does not break after clicking table sorting." + "<br>")

    def TC_Promotion_Banner_06_Reset_Filter(self):
        Promotion_Banner_Actions.Navigate_Promotion_Banner(self)
        print("<li>" + "Insert Title" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Promotion_Banner_Element.title_filter_field).send_keys(Promotion_Banner_Data.title_filter)
        print("<li>" + "Click on Reset button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Promotion_Banner_Element.reset_filter_button).click()
        # Assert Field is Empty
        empty_field = self.driver.find_element_by_class_name(Promotion_Banner_Element.title_filter_field).text
        self.assertEqual(empty_field, "", "Use is not able to reset search.")
        print("Expected Results: Title removed from Title field." + "<br>")

    def Promotion_Banner_07_Navigated_Back_from_Add_promotion_Page(self):
        Promotion_Banner_Actions.Navigate_Promotion_Banner(self)
        window_before = self.driver.window_handles[0]
        print("<li>" + "Click on add icon" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Promotion_Banner_Element.add_announcement_button).click()
        # get the window handle after a new window has opened
        window_after = self.driver.window_handles[1]
        # switch on to new child window
        self.driver.switch_to.window(window_after)
        self.driver.maximize_window()
        # Wait till page load
        wait_page_load = EC.presence_of_element_located((By.CLASS_NAME, Promotion_Banner_Element.add_announcement_page_element))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        print("<li>" + "Click on New List Navigation Link" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Promotion_Banner_Element.new_list_navigation_link).click()
        # Assert
        activity_announcement_page = self.driver.title
        self.assertEqual(activity_announcement_page, "Activity Announcement List", "User is not able to access to Activity Announcement List Page.")
        print("Expected Results: Navigated to Activity Announcement List page." + "<br>")

    def test_TC_Promotion_Banner_08_Navigated_Back_from_Edit_promotion_Page(self):
        Promotion_Banner_Actions.Navigate_Promotion_Banner(self)
        print("<li>" + "Click on edit icon" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Promotion_Banner_Element.edit_announcement_icon).click()
        # Wait till page load
        wait_page_load = EC.presence_of_element_located((By.CLASS_NAME, Promotion_Banner_Element.add_announcement_page_element))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        print("<li>" + "Click on New List Navigation Link" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Promotion_Banner_Element.new_list_navigation_link).click()
        # Assert
        activity_announcement_page = self.driver.title
        self.assertEqual(activity_announcement_page, "Activity Announcement List","User is not able to access to Activity Announcement List Page.")
        print("Expected Results: Navigated to Activity Announcement List page." + "<br>")


if __name__ == '__main__':
    unittest.main()
