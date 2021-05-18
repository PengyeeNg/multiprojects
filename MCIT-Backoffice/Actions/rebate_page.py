import SetUp.Base_SetUp
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Actions.login_page import Login_Actions
from Elements.rebate_page import Rebate_Setting_Element
from Elements.rebate_page import Rebate_Record_Element
from Elements.rebate_page import Provider_Report_Element
from Elements.rebate_page import Member_Report_Element
from Elements.rebate_page import Rebate_Element

class Rebate_Actions(SetUp.Base_SetUp.BSetUp):

    def Assert_Search_results(self):
        # Wait filter
        filtered_results = EC.text_to_be_present_in_element((By.CLASS_NAME, Rebate_Element.no_results_found),"No results found.")
        WebDriverWait(self.driver, 10).until(filtered_results)
        print("Expected Results: Filtered results = No results found." + "<br>")

    def View_All(self):
        # Wait till button is clickable
        wait_all_button = EC.element_to_be_clickable((By.ID, Rebate_Element.all_button))
        WebDriverWait(self.driver, 30).until(wait_all_button)
        print("<li>" + "Click on All button" + "</li>" + "<br>")
        self.driver.find_element_by_id(Rebate_Element.all_button).click()
        self.driver.implicitly_wait(30)

class Rebate_Setting_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Rebate_Setting(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Rebate' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Rebate_Element.rebate).click()
        rebate_setting = EC.presence_of_element_located((By.XPATH, Rebate_Setting_Element.rebate_setting))
        WebDriverWait(self.driver, 10).until(rebate_setting)
        print("<li>" + "Select 'Rebate Setting'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Rebate_Setting_Element.rebate_setting).click()
        rebate_setting_page = self.driver.title
        self.assertEqual(rebate_setting_page, "Rebate setting", "User is not able to navigate to Rebate Setting Page.")

class Rebate_record_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Rebate_Record(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Rebate' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Rebate_Element.rebate).click()
        rebate_record = EC.presence_of_element_located((By.XPATH, Rebate_Record_Element.rebate_record))
        WebDriverWait(self.driver, 10).until(rebate_record)
        print("<li>" + "Select 'Rebate Record'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Rebate_Record_Element.rebate_record).click()
        rebate_record_page = self.driver.title
        self.assertEqual(rebate_record_page, "Rebate Report", "User is not able to navigate to Rebate Record Page.")

class Provider_Report_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Provider_Report(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Rebate' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Rebate_Element.rebate).click()
        provider_report = EC.presence_of_element_located((By.XPATH, Provider_Report_Element.provider_report))
        WebDriverWait(self.driver, 10).until(provider_report)
        print("<li>" + "Select 'Provider Report'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Provider_Report_Element.provider_report).click()
        provider_report_page = self.driver.title
        self.assertEqual(provider_report_page, "Rebate Provider Report", "User is not able to navigate to Provider Report Page.")

class Member_Report_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Member_Report(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Rebate' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Rebate_Element.rebate).click()
        member_report = EC.presence_of_element_located((By.XPATH, Member_Report_Element.member_report))
        WebDriverWait(self.driver, 10).until(member_report)
        print("<li>" + "Select 'Member Report'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Report_Element.member_report).click()
        member_report_page = self.driver.title
        self.assertEqual(member_report_page, "Rebate Player Report", "User is not able to navigate to Member Report Page.")