import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import SetUp.Base_SetUp
from Actions.main_page import General_Actions
from Actions.promotion_page import List_Promotion_Actions
from Elements.promotion_page import List_Promotion_Element
from selenium.webdriver.support.select import Select

class List_Promotion(SetUp.Base_SetUp.BSetUp):

    def TC_List_Promotion_01_Add_Promotion(self):
        List_Promotion_Actions.Navigate_List_Promotion(self)
        print("<li>" + "Click on add icon" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(List_Promotion_Element.add_promotion_button).click()
        # Wait till page load
        wait_page_load = EC.presence_of_element_located((By.CLASS_NAME, List_Promotion_Element.add_promotion_page_element))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        # Assert
        add_promotion_page = self.driver.title
        self.assertEqual(add_promotion_page, "Add Promotion", "User is not able to access to Add Promotion Page.")
        print("Expected Results: Navigated to Add Promotion page." + "<br>")

    def TC_List_Promotion_02_Edit_Promotion(self):
        List_Promotion_Actions.Navigate_List_Promotion(self)
        print("<li>" + "Click on edit icon" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(List_Promotion_Element.edit_promotion_button).click()
        # Wait till page load
        wait_page_load = EC.presence_of_element_located((By.CLASS_NAME, List_Promotion_Element.add_promotion_page_element))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        # Assert
        add_promotion_page = self.driver.title
        self.assertEqual(add_promotion_page, "Add Promotion", "User is not able to access to Edit Promotion Page.")
        print("Expected Results: Navigated to Edit Promotion page." + "<br>")

    def test_TC_List_Promotion_03_Delete_Promotion(self):
        List_Promotion_Actions.Navigate_List_Promotion(self)
        print("<li>" + "Click on edit icon" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(List_Promotion_Element.delete_promotion_button).click()
        General_Actions.Assert_Delete_Confirmation_Dialog(self)

    def TC_List_Promotion_04_Search_Promotion(self):
        List_Promotion_Actions.Navigate_List_Promotion(self)
        print("<li>" + "Select Status" + "</li>" + "<br>")
        status_dropdown = Select(self.driver.find_element_by_id(List_Promotion_Element.status_filter_dropdown))
        # Select Floating Ratio
        status_dropdown.select_by_visible_text("Floating Ratio")
        print("<li>" + "Click on Search button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(List_Promotion_Element.filter_search_button).click()
        self.driver.implicitly_wait(100)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Deposit Bonus Strategy", "Page breaks after clicking on filter search button.")
        print("Expected Results: Page does not break after clicking on filter search button." + "<br>")

    def TC_List_Promotion_05_Table_Sorting_Promotion(self):
        List_Promotion_Actions.Navigate_List_Promotion(self)
        print("<li>" + "Click on Bonus Method header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(List_Promotion_Element.bonus_method_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Activity Type header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(List_Promotion_Element.activity_type_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Bonus Quota header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(List_Promotion_Element.bonus_quota_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Topup Amount More Than Or Equal To header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(List_Promotion_Element.topup_amount_more_than_or_equal_to_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Topup Amount Less Than Or Equal To header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(List_Promotion_Element.topup_amount_less_than_or_equal_to_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Turn Over header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(List_Promotion_Element.turn_over_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Start Date header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(List_Promotion_Element.start_date_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Close Date header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(List_Promotion_Element.close_date_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Remark header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(List_Promotion_Element.remark_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Provider header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(List_Promotion_Element.provider_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Status header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(List_Promotion_Element.status_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Auto Approval header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(List_Promotion_Element.auto_approval_header_sorting).click()
        self.driver.implicitly_wait(30)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Deposit Bonus Strategy", "Page breaks after clicking table sorting.")
        print("Expected Results: Page does not break after clicking table sorting." + "<br>")

    def TC_List_Promotion_06_View_All_Deposit_Bonus_Strategy(self):
        List_Promotion_Actions.Navigate_List_Promotion(self)
        print("<li>" + "Click on All button" + "</li>" + "<br>")
        self.driver.find_element_by_id(List_Promotion_Element.view_all_button).click()
        self.driver.implicitly_wait(30)
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Deposit Bonus Strategy", "Page breaks after clicking All button.")
        print("Expected Results: Page does not break after clicking All button." + "<br>")

    def TC_List_Promotion_07_Navigate_Back_from_Add_Promotion_Page(self):
        List_Promotion_Actions.Navigate_List_Promotion(self)
        print("<li>" + "Click on add icon" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(List_Promotion_Element.add_promotion_button).click()
        # Wait till page load
        wait_page_load = EC.presence_of_element_located((By.CLASS_NAME, List_Promotion_Element.add_promotion_page_element))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        print("<li>" + "Click on Deposit Bonus Strategy Link" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(List_Promotion_Element.deposit_bonus_strategy_navigation_link).click()
        # Assert
        deposit_bonus_strategy_page = self.driver.title
        self.assertEqual(deposit_bonus_strategy_page, "Deposit Bonus Strategy", "User is not able to access to Deposit Bonus Strategy Page.")
        print("Expected Results: Navigated to Deposit Bonus Strategy page." + "<br>")

    def TC_List_Promotion_08_Navigate_Back_from_Edit_Promotion_Page(self):
        List_Promotion_Actions.Navigate_List_Promotion(self)
        print("<li>" + "Click on edit icon" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(List_Promotion_Element.edit_promotion_button).click()
        # Wait till page load
        wait_page_load = EC.presence_of_element_located((By.CLASS_NAME, List_Promotion_Element.add_promotion_page_element))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        print("<li>" + "Click on Deposit Bonus Strategy Link" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(List_Promotion_Element.deposit_bonus_strategy_navigation_link).click()
        # Assert
        deposit_bonus_strategy_page = self.driver.title
        self.assertEqual(deposit_bonus_strategy_page, "Deposit Bonus Strategy", "User is not able to access to Deposit Bonus Strategy Page.")
        print("Expected Results: Navigated to Deposit Bonus Strategy page." + "<br>")

if __name__ == '__main__':
    unittest.main()
