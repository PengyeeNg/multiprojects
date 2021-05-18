import unittest
import SetUp.Base_SetUp
from Actions.deposit_withdraw_page import Wallet_Transfer_Actions
from Actions.deposit_withdraw_page import Deposit_Withdraw_Actions
from Elements.deposit_withdraw_page import Wallet_Transfer_Element
from Elements.deposit_withdraw_page import Deposit_Withdraw_Element
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Input_Data.deposit_withdraw_page import Deposit_Withdraw_Data


class Wallet_Transfer(SetUp.Base_SetUp.BSetUp):

    def test_TC_Wallet_Transfer_01_Add_Wallet_Transfer(self):
        Wallet_Transfer_Actions.Navigate_Wallet_Transfer(self)
        print("<li>" + "Click on 'New' button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Wallet_Transfer_Element.new_button).click()
        # wait till page loads
        zhang_hu_page = EC.presence_of_element_located((By.ID, Wallet_Transfer_Element.zhang_hu_page_element))
        WebDriverWait(self.driver, 10).until(zhang_hu_page)
        # Assert
        zhang_hu_form = self.driver.find_element_by_id(Wallet_Transfer_Element.zhang_hu_page_element).is_displayed()
        self.assertTrue(zhang_hu_form, "User is not able to navigate to Zhang Hu page.")
        print("Expected Results: Navigated to Zhang Hu page." + "<br>")

    def test_TC_Wallet_Transfer_02_Filter_Wallet_Transfer(self):
        Wallet_Transfer_Actions.Navigate_Wallet_Transfer(self)
        print("<li>" + "Click on add icon at the end of filter column" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Deposit_Withdraw_Element.filter_add_button).click()
        wait_filter_column_expand = EC.presence_of_element_located((By.XPATH, Wallet_Transfer_Element.filter_search_button))
        WebDriverWait(self.driver, 10).until(wait_filter_column_expand)
        print("<li>" + "Insert User ID" + "</li>" + "<br>")
        self.driver.find_element_by_id(Wallet_Transfer_Element.user_id_filter_field).send_keys(Deposit_Withdraw_Data.user_id_filter)
        print("<li>" + "Click on Search button" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Wallet_Transfer_Element.filter_search_button).click()
        # Assert
        Deposit_Withdraw_Actions.Assert_Search_results(self)

    def test_TC_Wallet_Transfer_03_Table_Sorting_Wallet_Transfer(self):
        Wallet_Transfer_Actions.Navigate_Wallet_Transfer(self)
        print("<li>" + "Click on User ID header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Wallet_Transfer_Element.user_id_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Type header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Wallet_Transfer_Element.type_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Provider header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Wallet_Transfer_Element.provider_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Amount header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Wallet_Transfer_Element.amount_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Status header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Wallet_Transfer_Element.status_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Bonus Amount header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Wallet_Transfer_Element.bonus_amount_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Related Activity header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Wallet_Transfer_Element.related_activity_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Created Time header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Wallet_Transfer_Element.created_time_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Error header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Wallet_Transfer_Element.error_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Result Message header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Wallet_Transfer_Element.result_message_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Remark header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Wallet_Transfer_Element.remark_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Edited Time header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Wallet_Transfer_Element.edited_time_header_sorting).click()
        self.driver.implicitly_wait(30)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Wallet transfer", "Page breaks after clicking table sorting.")
        print("Expected Results: Page does not break after clicking table sorting." + "<br>")



if __name__ == '__main__':
    unittest.main()
