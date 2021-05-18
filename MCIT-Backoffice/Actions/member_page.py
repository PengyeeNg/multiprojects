import SetUp.Base_SetUp
from Actions.login_page import Login_Actions
from Elements.member_page import Member_Element
from Elements.member_page import Member_Edit_Element
from Elements.member_page import Member_Levels_Element
from Elements.member_page import Member_Log_Element
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Input_Data.member_page import Member_Data

class Member_Actions(SetUp.Base_SetUp.BSetUp):
    def Filter_by_Name(self):
        print("<li>" + "Click on add icon at the end of Filter column" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Element.filter_add_icon).click()
        member_name_field = EC.presence_of_element_located((By.ID, Member_Element.member_name_field))
        WebDriverWait(self.driver, 10).until(member_name_field)
        print("<li>" + "Insert name into member name field" + "</li>" + "<br>")
        self.driver.find_element_by_id(Member_Element.member_name_field).send_keys(Member_Data.filter_name)
        print("<li>" + "Click on Inquire icon" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Element.filter_search_button).click()
        # Verify filter results
        filtered_results = EC.text_to_be_present_in_element((By.CSS_SELECTOR, Member_Element.filtered_results), "No results found.")
        WebDriverWait(self.driver, 10).until(filtered_results)
        print("Expected Results: Filtered results = No results found." + "<br>")


class Member_Edit_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Member_Edit(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Member' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Element.member).click()
        member_edit = EC.presence_of_element_located((By.XPATH, Member_Edit_Element.member_edit))
        WebDriverWait(self.driver, 10).until(member_edit)
        print("<li>" + "Select 'Member Edit'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Edit_Element.member_edit).click()
        member_edit_page = self.driver.title
        self.assertEqual(member_edit_page, "Member List", "User is not able to navigate to Member Edit Page.")

    def Navigate_Member_Edit_Setting(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Member' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Element.member).click()
        member_edit = EC.presence_of_element_located((By.XPATH, Member_Edit_Element.member_edit))
        WebDriverWait(self.driver, 10).until(member_edit)
        print("<li>" + "Select 'Member Edit'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Edit_Element.member_edit).click()
        member_edit_page = self.driver.title
        self.assertEqual(member_edit_page, "Member List", "User is not able to navigate to Member Edit Page.")
        print("<li>" + "Click on 'Setting' button'" + "</li>" + "<br>")
        # Wait till menu is displayed
        self.driver.find_element_by_xpath(Member_Edit_Element.setting_button).click()
        setting_menu = EC.presence_of_element_located((By.XPATH, Member_Edit_Element.setting_menu))
        WebDriverWait(self.driver, 10).until(setting_menu)

    def Assert_Tab_Element(self):
        inquire_button = EC.presence_of_element_located((By.ID, Member_Edit_Element.member_finance_inquire_button))
        WebDriverWait(self.driver, 10).until(inquire_button)
        # Assert element is displayed
        inquire_button_display = self.driver.find_element_by_id(Member_Edit_Element.member_finance_inquire_button).is_displayed()
        self.assertTrue(inquire_button_display,"User is not able to access to Member Finance Tab")



class Member_Levels_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Member_Levels(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Member' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Element.member).click()
        member_edit = EC.presence_of_element_located((By.XPATH, Member_Edit_Element.member_edit))
        WebDriverWait(self.driver, 10).until(member_edit)
        print("<li>" + "Select 'Member Levels'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Levels_Element.member_levels).click()
        member_levels_page = self.driver.title
        self.assertEqual(member_levels_page, "Member Levels", "User is not able to navigate to Member Levels Page")


class Member_Log_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Member_Log(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Member' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Element.member).click()
        member_edit = EC.presence_of_element_located((By.XPATH, Member_Edit_Element.member_edit))
        WebDriverWait(self.driver, 10).until(member_edit)
        print("<li>" + "Select 'Member Log'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Log_Element.member_log).click()
        member_log_page = self.driver.title
        self.assertEqual(member_log_page, "Member Login Log", "User is not able to navigate to Member Log Page")
