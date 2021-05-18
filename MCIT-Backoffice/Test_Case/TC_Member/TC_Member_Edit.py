import unittest
import SetUp.Base_SetUp
from Actions.member_page import Member_Edit_Actions
from Actions.member_page import Member_Actions
from Elements.member_page import Member_Edit_Element
from Elements.member_page import Member_Element
from Input_Data.member_page import Member_Edit_Data
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Actions.main_page import General_Actions

class Member_Edit(SetUp.Base_SetUp.BSetUp):

    def test_TC_Member_Edit_01_Valid_Navigate_Member_List(self):
        Member_Edit_Actions.Navigate_Member_Edit(self)
        print("Expected Results: Navigated to Backoffice Sign In Page." + "<br>")

    def test_TC_Member_Edit_02_Member_List_Filtered_by_Member_Name(self):
        Member_Edit_Actions.Navigate_Member_Edit(self)
        Member_Actions.Filter_by_Name(self)

    def test_TC_Member_Edit_06_Edit_Status(self):
        Member_Edit_Actions.Navigate_Member_Edit(self)
        print("<li>" + "Click on the status of a user" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Edit_Element.activate_status_button).click()
        # Wait till 'Change' dialog box pop out
        wait_change_dialog_box = EC.presence_of_element_located((By.ID, Member_Edit_Element.status_renew_button))
        WebDriverWait(self.driver, 10).until(wait_change_dialog_box)
        # Assert Dialog box is displayed
        change_dialog_box = self.driver.find_element_by_id(Member_Edit_Element.status_change_dialog_box).is_displayed()
        self.assertTrue(change_dialog_box, "User is not able to change user status.")
        print("Expected Results: A 'Change' dialog box popped out." + "<br>")

    def test_TC_Member_Edit_07_Add_Member_Bank_Information(self):
        Member_Edit_Actions.Navigate_Member_Edit(self)
        print("<li>" + "Click on 'Bank' button" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Edit_Element.check_bank_button).click()
        # Assert navigated to Member Bank Card Management Page
        member_bank_card_management_page = self.driver.title
        self.assertEqual(member_bank_card_management_page, "Member Bank Card Management", "User is not able to navigate to Member Bank Card Management Page.")
        print("<li>" + "Click on 'Add Bank Card' button" + "</li>" + "<br>")
        wait_add_bank_card_button = EC.presence_of_element_located((By.XPATH, Member_Edit_Element.add_bank_card_button))
        WebDriverWait(self.driver, 10).until(wait_add_bank_card_button)
        self.driver.find_element_by_xpath(Member_Edit_Element.add_bank_card_button).click()
        # Assert navigated to Add Member Bank Information Page
        add_member_bank_information_page = self.driver.title
        self.assertEqual(add_member_bank_information_page, "Add Member Bank Information", "User is not able to navigate to Add Member Bank Information Page.")
        print("<li>" + "Insert bank user name" + "</li>" + "<br>")
        self.driver.find_element_by_id(Member_Edit_Element.bank_username_field).send_keys(Member_Edit_Data.bank_username)
        print("<li>" + "Select Bank ID" + "</li>" + "<br>")
        bank_id_dropdown = Select(self.driver.find_element_by_id(Member_Edit_Element.bank_id_field))
        # Select Maybank
        bank_id_dropdown.select_by_visible_text("Maybank")
        print("<li>" + "Insert bank account" + "</li>" + "<br>")
        self.driver.find_element_by_id(Member_Edit_Element.bank_account_field).send_keys(Member_Edit_Data.bank_account)
        print("<li>" + "Insert bank address" + "</li>" + "<br>")
        self.driver.find_element_by_id(Member_Edit_Element.bank_address_field).send_keys(Member_Edit_Data.bank_address)
        print("<li>" + "Click on 'Editor' button" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Edit_Element.add_button).click()
        # Wait till navigated to Member List
        wait_check_bank_button = EC.presence_of_element_located((By.XPATH, Member_Edit_Element.check_bank_button))
        WebDriverWait(self.driver, 10).until(wait_check_bank_button)
        print("<li>" + "Click back the 'Bank' button of the user" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Edit_Element.check_bank_button).click()
        # Assert navigated to Member Bank Card Management Page
        member_bank_card_management_page = self.driver.title
        self.assertEqual(member_bank_card_management_page, "Member Bank Card Management","User is not able to navigate to Member Bank Card Management Page.")
        # Assert the bank information is added
        added_bank_username = self.driver.find_element_by_xpath(Member_Edit_Element.last_row_bank_username).text
        added_branch_name = self.driver.find_element_by_xpath(Member_Edit_Element.last_row_branch_name).text
        added_bank_account = self.driver.find_element_by_xpath(Member_Edit_Element.last_row_bank_account).text
        added_bank_address = self.driver.find_element_by_xpath(Member_Edit_Element.last_row_bank_address).text
        self.assertEqual(added_bank_username, "BankName1","Bank username is not added.")
        self.assertEqual(added_branch_name, "Maybank", "Branch name is not added.")
        self.assertEqual(added_bank_account, "12345678901", "Bank account is not added.")
        self.assertEqual(added_bank_address, "Kuala Lumpur, Malaysia", "Bank address is not added.")
        print("Expected Results: Navigated to Member Bank Card Management Page with new added bank information" + "<br>")

    def test_TC_Member_Edit_08_Edit_Member_Bank_Information(self):
        Member_Edit_Actions.Navigate_Member_Edit(self)
        print("<li>" + "Click on 'Bank' button" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Edit_Element.check_bank_button).click()
        # Assert navigated to Member Bank Card Management Page
        member_bank_card_management_page = self.driver.title
        self.assertEqual(member_bank_card_management_page, "Member Bank Card Management", "User is not able to navigate to Member Bank Card Management Page.")
        print("<li>" + "Click on 'Editor' button" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Edit_Element.edit_button).click()
        # Wait till navigated to Edit Member Bank Card
        wait_edit_bank_button = EC.presence_of_element_located((By.XPATH, Member_Edit_Element.add_button))
        WebDriverWait(self.driver, 10).until(wait_edit_bank_button)
        # Assert navigated to Edit Member Bank Card
        edit_member_bank_card_page = self.driver.title
        self.assertEqual(edit_member_bank_card_page, "Edit Member Bank Card","User is not able to navigate to Edit Member Bank Card Page.")
        print("<li>" + "Edit Bank Username" + "</li>" + "<br>")
        self.driver.find_element_by_id(Member_Edit_Element.bank_username_field).clear()
        self.driver.find_element_by_id(Member_Edit_Element.bank_username_field).send_keys(Member_Edit_Data.edited_bank_username)
        print("<li>" + "Click on 'Editor' button" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Edit_Element.add_button).click()
        wait_member_list_page = EC.presence_of_element_located((By.XPATH, Member_Edit_Element.check_bank_button))
        WebDriverWait(self.driver, 10).until(wait_member_list_page)
        print("<li>" + "Click back the 'Bank' button of the user" + "</li>" + "<br>")
        # Assert navigated to Member List Page
        member_list_page = self.driver.title
        self.assertEqual(member_list_page, "Member List","User is not able to navigate to Member List Page.")
        self.driver.find_element_by_xpath(Member_Edit_Element.check_bank_button).click()
        # Assert navigated to Member Bank Card Management Page
        member_bank_card_management_page = self.driver.title
        self.assertEqual(member_bank_card_management_page, "Member Bank Card Management", "User is not able to navigate to Member Bank Card Management Page.")
        # Assert Bank Username is edited
        added_bank_username = self.driver.find_element_by_xpath(Member_Edit_Element.last_row_bank_username).text
        self.assertEqual(added_bank_username, "BankNameEdited", "Bank username is not edited.")
        print("Expected Results: Navigated to Member Bank Card Management Page with edited bank information" + "<br>")

    def test_TC_Member_Edit_09_Delete_Member_Bank_Information(self):
        Member_Edit_Actions.Navigate_Member_Edit(self)
        print("<li>" + "Click on 'Bank' button" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Edit_Element.check_bank_button).click()
        # Assert navigated to Member Bank Card Management Page
        member_bank_card_management_page = self.driver.title
        self.assertEqual(member_bank_card_management_page, "Member Bank Card Management", "User is not able to navigate to Member Bank Card Management Page.")
        print("<li>" + "Click on 'Delete' button" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Edit_Element.delete_button).click()
        # Assert Dialog box is displayed
        delete_confirmation_dialog_box = self.driver.find_element_by_xpath(Member_Edit_Element.delete_confirmation_dialog_box).is_displayed()
        self.assertTrue(delete_confirmation_dialog_box, "User is not able to delete bank information.")
        print("Expected Results: Delete Confirmation dialog box popped out." + "<br>")

    def test_TC_Member_Edit_10_Game_balance(self):
        Member_Edit_Actions.Navigate_Member_Edit(self)
        print("<li>" + "Click on 'Game Balance' button" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Edit_Element.game_balance_button).click()
        # Wait till game balance list displayed
        game_balance_list = EC.presence_of_element_located((By.XPATH, Member_Edit_Element.game_balance_list))
        WebDriverWait(self.driver, 10).until(game_balance_list)
        # Assert
        game_balance_dialog_box = self.driver.find_element_by_xpath(Member_Edit_Element.game_balance_dialog_box).is_displayed()
        self.assertTrue(game_balance_dialog_box, "User is not able to view game balance.")
        print("Expected Results: Game balance dialog box popped out." + "<br>")

    def test_TC_Member_Edit_11_Edit_Member_Information(self):
        Member_Edit_Actions.Navigate_Member_Edit_Setting(self)
        print("<li>" + "Click on 'Member Information Edit' button'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Edit_Element.member_information_edit_button).click()
        # Assert
        member_information_edit_page = self.driver.title
        self.assertEqual(member_information_edit_page, "Member Information Edit", "User is not able to navigate to Member Information Edit Page.")
        print("Expected Results: Navigated to Member Information Edit Page." + "<br>")

    def test_TC_Member_Edit_12_Adjust(self):
        Member_Edit_Actions.Navigate_Member_Edit_Setting(self)
        print("<li>" + "Click on 'Adjust' button'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Edit_Element.adjust_button).click()
        # Assert
        adjust_page = self.driver.title
        self.assertEqual(adjust_page, "Adjust", "User is not able to navigate to Adjust Page.")
        print("Expected Results: Navigated to Adjust Page." + "<br>")

    def test_TC_Member_Edit_13_Adjust_Turn_Over_Amount(self):
        Member_Edit_Actions.Navigate_Member_Edit_Setting(self)
        print("<li>" + "Click on 'Adjust Turn Over Amount' button'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Edit_Element.adjust_turn_over_amount_button).click()
        # Assert
        adjust_page = self.driver.title
        self.assertEqual(adjust_page, "Operate Member Turn Over Amount", "User is not able to navigate to Operate Member Turn Over Amount Page.")
        print("Expected Results: Navigated to Operate Member Turn Over Amount Page." + "<br>")

    def test_TC_Member_Edit_14_Reset_Password(self):
        Member_Edit_Actions.Navigate_Member_Edit_Setting(self)
        print("<li>" + "Click on 'Reset Password' button'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Edit_Element.reset_password_button).click()
        # Assert
        change_member_password_page = self.driver.title
        self.assertEqual(change_member_password_page, "Change Member Password", "User is not able to navigate to Change Member Password Page.")
        print("Expected Results: Navigated to Change Member Password Page." + "<br>")

    def test_TC_Member_Edit_15_Adjust_Turn_Over_Amount_Provider(self):
        Member_Edit_Actions.Navigate_Member_Edit_Setting(self)
        # get the window handle after the window has opened
        window_before = self.driver.window_handles[0]
        print("<li>" + "Click on 'Adjust Turn Over Amount Provider' button'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Edit_Element.adjust_turn_over_amount_provider_button).click()
        # get the window handle after a new window has opened
        window_after = self.driver.window_handles[1]
        # switch on to new child window
        self.driver.switch_to.window(window_after)
        self.driver.maximize_window()
        # wait till new window is display
        adjust_turn_over_amount_provider = EC.presence_of_element_located((By.XPATH, Member_Edit_Element.inquire_button))
        WebDriverWait(self.driver, 10).until(adjust_turn_over_amount_provider)
        # Assert New Window is displayed
        adjust_turn_over_amount_provider_window = self.driver.find_element_by_xpath(Member_Edit_Element.inquire_button).is_displayed()
        self.assertTrue(adjust_turn_over_amount_provider_window, "User is not able to access to Adjust Turn Over Amount Provider Page.")
        print("Expected Results: New window popped out." + "<br>")

    def test_TC_Member_Edit_16_Member_Finance(self):
        Member_Edit_Actions.Navigate_Member_Edit_Setting(self)
        print("<li>" + " Click on 'Member Finance' button " + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Edit_Element.member_finance_button).click()
        # Assert Member Finance Dialog is displayed
        wait_member_finance_dialog_box = EC.presence_of_element_located((By.XPATH, Member_Edit_Element.game_history_tab))
        WebDriverWait(self.driver, 10).until(wait_member_finance_dialog_box)
        member_finance_dialog_box = self.driver.find_element_by_xpath(Member_Edit_Element.game_history_tab).is_displayed()
        self.assertTrue(member_finance_dialog_box, "User is not able to access to Member Finance Page.")

        # Game History
        # Member_Edit_Actions.Assert_Tab_Element(self)

        print("<li>" + " Click on 'Transfer History' tab " + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Edit_Element.transfer_history_tab).click()
        # Transfer History
        # Member_Edit_Actions.Assert_Tab_Element(self)

        print("<li>" + " Click on 'Bonus History' tab " + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Edit_Element.bonus_history_tab).click()
        # Bonus History
        # Member_Edit_Actions.Assert_Tab_Element(self)

        print("<li>" + " Click on 'Rebate History' tab " + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Edit_Element.rebate_history_tab).click()
        # Rebate History
        # Member_Edit_Actions.Assert_Tab_Element(self)

        print("<li>" + " Click on 'Deposit History' tab " + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Edit_Element.deposit_history_tab).click()
        # Deposit History
        # Member_Edit_Actions.Assert_Tab_Element(self)

        print("<li>" + " Click on 'Withdraw History' tab " + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Edit_Element.withdraw_history_tab).click()
        # Withdraw History
        # Member_Edit_Actions.Assert_Tab_Element(self)

        print("Expected Results: Tabs are displayed." + "<br>")

    def test_TC_Member_Edit_17_Export_Member_List(self):
        Member_Edit_Actions.Navigate_Member_Edit(self)
        print("<li>" + "Click on add icon at the end of Filter column" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Element.filter_add_icon).click()
        member_name_field = EC.presence_of_element_located((By.ID, Member_Element.member_name_field))
        WebDriverWait(self.driver, 10).until(member_name_field)
        print("<li>" + "Click on 'Export' button" + "</li>" + "<br>")
        self.driver.find_element_by_id(Member_Edit_Element.export_button).click()
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Member List","Page breaks after clicking export button.")
        print("Expected Results: Page does not break after clicking export button." + "<br>")

    def test_TC_Member_Edit_18_Table_Sorting(self):
        Member_Edit_Actions.Navigate_Member_Edit(self)
        print("<li>" + "Click on Username header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Edit_Element.username_filter).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Affiliate header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Edit_Element.affiliate_filter).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Name header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Edit_Element.name_filter).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Balance header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Edit_Element.balance_filter).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Member Level ID header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Edit_Element.member_level_id_filter).click()
        self.driver.implicitly_wait(30)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Member List", "Page breaks after clicking table sorting.")
        print("Expected Results: Page does not break after clicking table sorting." + "<br>")

    def test_TC_Member_Edit_19_View_All_Member_List(self):
        Member_Edit_Actions.Navigate_Member_Edit(self)
        General_Actions.view_all(self)
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Member List", "Page breaks after clicking All button.")
        print("Expected Results: Page does not break after clicking All button." + "<br>")

    def test_TC_Member_Edit_20_Navigate_Back_from_Adjust_Page(self):
        Member_Edit_Actions.Navigate_Member_Edit_Setting(self)
        print("<li>" + "Click on 'Adjust' button'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Edit_Element.adjust_button).click()
        print("<li>" + "Click on Member List Link" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Edit_Element.member_list_navigation_link).click()
        # Wait till page load
        wait_page_load = EC.presence_of_element_located((By.XPATH, Member_Element.filter_add_icon))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Member List", "Page breaks after clicking Member List Navigation Link.")
        print("Expected Results: Page does not break after clicking Member List Navigation Link." + "<br>")

    def test_TC_Member_Edit_21_Navigate_Back_from_Adjust_Turn_Over_Amount_Page(self):
        Member_Edit_Actions.Navigate_Member_Edit_Setting(self)
        print("<li>" + "Click on 'Adjust Turn Over Amount' button'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Edit_Element.adjust_turn_over_amount_button).click()
        print("<li>" + "Click on Member List Link" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Edit_Element.member_list_navigation_link).click()
        # Wait till page load
        wait_page_load = EC.presence_of_element_located((By.XPATH, Member_Element.filter_add_icon))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Member List", "Page breaks after clicking Member List Navigation Link.")
        print("Expected Results: Page does not break after clicking Member List Navigation Link." + "<br>")

    def test_TC_Member_Edit_22_Navigate_Back_from_Change_Member_Password_Page(self):
        Member_Edit_Actions.Navigate_Member_Edit_Setting(self)
        print("<li>" + "Click on 'Change Member Password' button'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Edit_Element.reset_password_button).click()
        print("<li>" + "Click on Member List Link" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Edit_Element.member_list_navigation_link).click()
        # Wait till page load
        wait_page_load = EC.presence_of_element_located((By.XPATH, Member_Element.filter_add_icon))
        WebDriverWait(self.driver, 10).until(wait_page_load)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Member List", "Page breaks after clicking Member List Navigation Link.")
        print("Expected Results: Page does not break after clicking Member List Navigation Link." + "<br>")


if __name__ == '__main__':
    unittest.main()
