import unittest
import SetUp.Base_SetUp
from Actions.login_page import Login_Actions
from Actions.main_page import MainPage_Actions
from Elements.main_page import MainPage_Element
from Elements.login_page import Login_Element
from Input_Data.main_page import Main_Data
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class Main(SetUp.Base_SetUp.BSetUp):

    def test_TC_Main_01_Change_Password(self):

        Login_Actions.valid_login_flow(self)
        MainPage_Actions.navigated_change_password_page(self)
        print("<li>" + "Insert Old Password" + "</li>" + "<br>")
        self.driver.find_element_by_id(MainPage_Element.old_password).send_keys(Main_Data.old_password)
        print("<li>" + "Insert New Password" + "</li>" + "<br>")
        self.driver.find_element_by_id(MainPage_Element.new_password).send_keys(Main_Data.new_password)
        print("<li>" + "Insert Retype Password" + "</li>" + "<br>")
        self.driver.find_element_by_id(MainPage_Element.retype_password).send_keys(Main_Data.retype_password)
        print("<li>" + "Click on 'Change' button" + "</li>" + "<br>")
        MainPage_Actions.click_change_button(self)
        logo_available = EC.presence_of_element_located((By.XPATH, Login_Element.page_logo))
        WebDriverWait(self.driver, 10).until(logo_available)
        sign_in_page = self.driver.title
        self.assertEqual(sign_in_page, "Sign In", "User is not able to navigate to Sign In Page after changing password.")
        print("<li>" + "Insert username" + "</li>" + "<br>")
        Login_Actions.insert_username(self)
        print("<li>" + "Insert new password" + "</li>" + "<br>")
        self.driver.find_element_by_id(Login_Element.password).send_keys(Main_Data.new_password)
        print("<li>" + "Click on log in button" + "</li>" + "<br>")
        Login_Actions.click_log_in_button(self)
        # Assertion
        logo_available = EC.presence_of_element_located((By.XPATH, MainPage_Element.main_page_title))
        WebDriverWait(self.driver, 10).until(logo_available)
        main_page = self.driver.find_element_by_xpath(MainPage_Element.main_page_title).is_displayed()
        self.assertTrue(main_page, "User is not able to access to Backoffice Main Page with new password.")
        print("Expected Results: User is able to login to Backoffice Main Page with changed password." + "<br>")

    # Change back to old password
        # print("<li>" + "Click on the username dropdown" + "</li>" + "<br>")
        MainPage_Actions.click_username_dropdown(self)
        # print("<li>" + "Click on 'Change Password' button" + "</li>" + "<br>")
        MainPage_Actions.click_change_password(self)
        # Verify navigate to change password page
        change_password = EC.presence_of_element_located((By.XPATH, MainPage_Element.change_button))
        WebDriverWait(self.driver, 10).until(change_password)
        change_password_page = self.driver.find_element_by_xpath(MainPage_Element.change_button).is_displayed()
        self.assertTrue(change_password_page, "User is not able to access to Change Password Page.")
        # print("<li>" + "Insert Old Password" + "</li>" + "<br>")
        self.driver.find_element_by_id(MainPage_Element.old_password).send_keys(Main_Data.new_password)
        # print("<li>" + "Insert New Password" + "</li>" + "<br>")
        self.driver.find_element_by_id(MainPage_Element.new_password).send_keys(Main_Data.old_password)
        # print("<li>" + "Insert Retype Password" + "</li>" + "<br>")
        self.driver.find_element_by_id(MainPage_Element.retype_password).send_keys(Main_Data.old_password)
        # print("<li>" + "Click on 'Change' button" + "</li>" + "<br>")
        MainPage_Actions.click_change_button(self)
        logo_available = EC.presence_of_element_located((By.XPATH, Login_Element.page_logo))
        WebDriverWait(self.driver, 10).until(logo_available)
        sign_in_page = self.driver.title
        self.assertEqual(sign_in_page, "Sign In","User is not able to navigate to Sign In Page after changing password.")
        # print("<li>" + "Insert username" + "</li>" + "<br>")
        Login_Actions.insert_username(self)
        # print("<li>" + "Insert new password" + "</li>" + "<br>")
        self.driver.find_element_by_id(Login_Element.password).send_keys(Main_Data.old_password)
        # print("<li>" + "Click on log in button" + "</li>" + "<br>")
        Login_Actions.click_log_in_button(self)
        # Assertion
        logo_available = EC.presence_of_element_located((By.XPATH, MainPage_Element.main_page_title))
        WebDriverWait(self.driver, 10).until(logo_available)
        main_page = self.driver.find_element_by_xpath(MainPage_Element.main_page_title).is_displayed()
        self.assertTrue(main_page, "User is not able to access to Backoffice Main Page with new password.")


    def test_TC_Main_02_Change_Password_Incorrect_Old_Password(self):

        Login_Actions.valid_login_flow(self)
        MainPage_Actions.navigated_change_password_page(self)
        print("<li>" + "Insert wrong Old Password" + "</li>" + "<br>")
        self.driver.find_element_by_id(MainPage_Element.old_password).send_keys(Main_Data.wrong_old_password)
        print("<li>" + "Insert New Password" + "</li>" + "<br>")
        self.driver.find_element_by_id(MainPage_Element.new_password).send_keys(Main_Data.new_password)
        print("<li>" + "Insert Retype Password" + "</li>" + "<br>")
        self.driver.find_element_by_id(MainPage_Element.retype_password).send_keys(Main_Data.retype_password)
        print("<li>" + "Click on 'Change' button" + "</li>" + "<br>")
        MainPage_Actions.click_change_button(self)
        # Assertion
        wrong_old_password_prompt = EC.presence_of_element_located((By.CSS_SELECTOR, MainPage_Element.incorrect_old_password_prompt))
        WebDriverWait(self.driver, 10).until(wrong_old_password_prompt)
        wrong_old_password_message = self.driver.find_element_by_css_selector(MainPage_Element.incorrect_old_password_prompt).text
        self.assertEqual(wrong_old_password_message, "Incorrect old password.", "Unable to detect wrong old password.")
        print("Expected Results: Error prompted without proceeding to Backoffice Sign In Page." + "<br>")

    def test_TC_Main_03_Change_Password_Incorrect_Retype_Password(self):
        Login_Actions.valid_login_flow(self)
        MainPage_Actions.navigated_change_password_page(self)
        print("<li>" + "Insert Old Password" + "</li>" + "<br>")
        self.driver.find_element_by_id(MainPage_Element.old_password).send_keys(Main_Data.old_password)
        print("<li>" + "Insert New Password" + "</li>" + "<br>")
        self.driver.find_element_by_id(MainPage_Element.new_password).send_keys(Main_Data.new_password)
        print("<li>" + "Insert wrong Retype Password" + "</li>" + "<br>")
        self.driver.find_element_by_id(MainPage_Element.retype_password).send_keys(Main_Data.wrong_retype_password)
        print("<li>" + "Click on 'Change' button" + "</li>" + "<br>")
        MainPage_Actions.click_change_button(self)
        # Assertion
        wrong_retype_password_prompt = EC.presence_of_element_located((By.CSS_SELECTOR, MainPage_Element.incorrect_retype_password_prompt))
        WebDriverWait(self.driver, 10).until(wrong_retype_password_prompt)
        wrong_retype_password_message = self.driver.find_element_by_css_selector(MainPage_Element.incorrect_retype_password_prompt).is_displayed()
        self.assertTrue(wrong_retype_password_message, "Unable to detect wrong retype password.")
        print("Expected Results: Error prompted without proceeding to Backoffice Sign In Page." + "<br>")

    def test_TC_Main_04_Change_Password_Empty_Old_Password(self):
        Login_Actions.valid_login_flow(self)
        MainPage_Actions.navigated_change_password_page(self)
        print("<li>" + "Insert New Password" + "</li>" + "<br>")
        self.driver.find_element_by_id(MainPage_Element.new_password).send_keys(Main_Data.new_password)
        print("<li>" + "Insert Retype Password" + "</li>" + "<br>")
        self.driver.find_element_by_id(MainPage_Element.retype_password).send_keys(Main_Data.retype_password)
        print("<li>" + "Click on 'Change' button" + "</li>" + "<br>")
        MainPage_Actions.click_change_button(self)
        # Assertion
        blank_old_password_prompt = EC.presence_of_element_located((By.CSS_SELECTOR, MainPage_Element.blank_old_password_prompt))
        WebDriverWait(self.driver, 10).until(blank_old_password_prompt)
        blank_old_password_message = self.driver.find_element_by_css_selector(MainPage_Element.blank_old_password_prompt).text
        self.assertEqual(blank_old_password_message, "Old Password cannot be blank.", "Unable to detect blank old password.")
        print("Expected Results: Error prompted without proceeding to Backoffice Sign In Page." + "<br>")

    def test_TC_Main_05_Change_Password_Empty_New_Password(self):
        Login_Actions.valid_login_flow(self)
        MainPage_Actions.navigated_change_password_page(self)
        print("<li>" + "Insert Old Password" + "</li>" + "<br>")
        self.driver.find_element_by_id(MainPage_Element.old_password).send_keys(Main_Data.old_password)
        print("<li>" + "Insert Retype Password" + "</li>" + "<br>")
        self.driver.find_element_by_id(MainPage_Element.retype_password).send_keys(Main_Data.retype_password)
        print("<li>" + "Click on 'Change' button" + "</li>" + "<br>")
        MainPage_Actions.click_change_button(self)
        # Assertion
        blank_new_password_prompt = EC.presence_of_element_located((By.CSS_SELECTOR, MainPage_Element.blank_new_password_prompt))
        WebDriverWait(self.driver, 10).until(blank_new_password_prompt)
        blank_new_password_message = self.driver.find_element_by_css_selector(MainPage_Element.blank_new_password_prompt).text
        self.assertEqual(blank_new_password_message, "New Password cannot be blank.", "Unable to detect blank new password.")
        print("Expected Results: Error prompted without proceeding to Backoffice Sign In Page." + "<br>")

    def test_TC_Main_06_Change_Password_Empty_Retype_Password(self):
        Login_Actions.valid_login_flow(self)
        MainPage_Actions.navigated_change_password_page(self)
        print("<li>" + "Insert Old Password" + "</li>" + "<br>")
        self.driver.find_element_by_id(MainPage_Element.old_password).send_keys(Main_Data.old_password)
        print("<li>" + "Insert New Password" + "</li>" + "<br>")
        self.driver.find_element_by_id(MainPage_Element.new_password).send_keys(Main_Data.new_password)
        print("<li>" + "Click on 'Change' button" + "</li>" + "<br>")
        MainPage_Actions.click_change_button(self)
        # Assertion
        blank_retype_password_prompt = EC.presence_of_element_located((By.CSS_SELECTOR, MainPage_Element.blank_retype_password_prompt))
        WebDriverWait(self.driver, 10).until(blank_retype_password_prompt)
        blank_retype_password_message = self.driver.find_element_by_css_selector(MainPage_Element.blank_retype_password_prompt).text
        self.assertEqual(blank_retype_password_message, "Retype Password cannot be blank.", "Unable to detect blank retype password.")
        print("Expected Results: Error prompted without proceeding to Backoffice Sign In Page." + "<br>")

    def test_TC_Main_07_Online_Member(self):
        Login_Actions.valid_login_flow(self)
        # Assert number of online member on icon
        # number_of_online_member = self.driver.find_element_by_css_selector(MainPage_Element.number_online_member).text
        # self.assertEqual(number_of_online_member, "0", "Number of online member is incorrect")
        print("<li>" + "Click on the online member dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainPage_Element.online_member_icon).click()
        online_member_menu = EC.presence_of_element_located((By.XPATH, MainPage_Element.online_member_menu))
        WebDriverWait(self.driver, 10).until(online_member_menu)
        online_member_dropdown = self.driver.find_element_by_xpath(MainPage_Element.online_member_menu).is_displayed()
        self.assertTrue(online_member_dropdown , "User is not able to access to online member dropdown.")
        print("<li>" + "Click on the dropdown menu" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainPage_Element.online_member_dropdown).click()
        total_online_member = self.driver.find_element_by_css_selector(MainPage_Element.total_online_member).text
        if total_online_member == 0:
            no_results_found = self.driver.find_element_by_css_selector(MainPage_Element.no_online_member).text
            self.assertEqual(no_results_found, "No results found.", "Member List is not shown.")
            # Assertion- Member List Page
            member_list_page = self.driver.title
            self.assertEqual(member_list_page, "Member List", "User is not able to navigate to Member List Page.")
            print("Expected Results: Navigated to Member List page and showed the list of online member." + "<br>")
        else:
            load_number_online_member = EC.text_to_be_present_in_element((By.CSS_SELECTOR, MainPage_Element.number_online_member), total_online_member)
            WebDriverWait(self.driver, 10).until(load_number_online_member)
            # Assertion- Member List Page
            member_list_page = self.driver.title
            self.assertEqual(member_list_page, "Member List", "User is not able to navigate to Member List Page.")
            print("Expected Results: Navigated to Member List page and showed the list of online member." + "<br>")

    def test_TC_Main_08_Notification(self):
        Login_Actions.valid_login_flow(self)
        # Assert number of online member on icon
        print("<li>" + "Click on the notification dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainPage_Element.notification_icon).click()
        notification_menu = EC.presence_of_element_located((By.XPATH, MainPage_Element.notification_menu))
        WebDriverWait(self.driver, 10).until(notification_menu)
        notification_dropdown = self.driver.find_element_by_xpath(MainPage_Element.notification_menu).is_displayed()
        self.assertTrue(notification_dropdown , "User is not able to access to notification dropdown.")
        # chong zhi records
        print("<li>" + "Click on cong zhi records" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainPage_Element.chong_zhi_records).click()
        deposit_management_page = self.driver.title
        self.assertEqual(deposit_management_page, "Deposit Management", "User is not able to navigate to Deposit Management Page.")
        # withdrawal records
        self.driver.find_element_by_xpath(MainPage_Element.notification_icon).click()
        notification_menu = EC.presence_of_element_located((By.XPATH, MainPage_Element.notification_menu))
        WebDriverWait(self.driver, 10).until(notification_menu)
        print("<li>" + "Click on withdrawal records" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainPage_Element.withdrawal_records).click()
        withdrawal_management_page = self.driver.title
        self.assertEqual(withdrawal_management_page, "Withdrawal Management","User is not able to navigate to Withdrawal Management Page.")
        # new file records
        self.driver.find_element_by_xpath(MainPage_Element.notification_icon).click()
        notification_menu = EC.presence_of_element_located((By.XPATH, MainPage_Element.notification_menu))
        WebDriverWait(self.driver, 10).until(notification_menu)
        print("<li>" + "Click on new file records" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainPage_Element.new_file_records).click()
        file_page = self.driver.title
        self.assertEqual(file_page, "File","User is not able to navigate to File Page.")
        # bank balance records
        self.driver.find_element_by_xpath(MainPage_Element.notification_icon).click()
        notification_menu = EC.presence_of_element_located((By.XPATH, MainPage_Element.notification_menu))
        WebDriverWait(self.driver, 10).until(notification_menu)
        print("<li>" + "Click on bank balance records" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainPage_Element.bank_balance_records).click()
        receiving_account_management_page = self.driver.title
        self.assertEqual(receiving_account_management_page, "Receiving Account Management", "User is not able to navigate to Receiving Account Management Page.")
        self.driver.find_element_by_xpath(MainPage_Element.notification_icon).click()
        notification_menu = EC.presence_of_element_located((By.XPATH, MainPage_Element.notification_menu))
        WebDriverWait(self.driver, 10).until(notification_menu)
        print("Expected Results: A dropdown column displayed with number of notification according to different records and able to navigate to respective pages." + "<br>")


if __name__ == '__main__':
    unittest.main()
