from Setup.T3 import Base_Setup
from Elements.T3.login_page import LogInElement
from Actions.T3.login_page import LoginpageActions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Elements.T3.user_page import UserElement


class UserpageActions(Base_Setup.BSetup):

    def Access_to_Quota_Conversion(self):
        LoginpageActions.Login_to_Mainpage(self)
        print("<li>" + "Click on Announcement" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(LogInElement.notification_link).click()
        print("<li>" + "Click on Quota Conversion" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserElement.quota_conversion_link).click()
        # Wait page load
        wait_page_load = EC.presence_of_element_located((By.XPATH, UserElement.quota_conversion_element))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        page_loaded = self.driver.find_element_by_xpath(UserElement.quota_conversion_element).is_displayed()
        self.assertTrue(page_loaded, "User is not able to access to Quota Conversion.")

    def Access_to_Deposit_Area(self):
        LoginpageActions.Login_to_Mainpage(self)
        print("<li>" + "Click on Announcement" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(LogInElement.notification_link).click()
        print("<li>" + "Click on Deposit Area" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserElement.deposit_area_link).click()
        # Wait page load
        wait_page_load = EC.presence_of_element_located((By.XPATH, UserElement.deposit_area_element))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        page_loaded = self.driver.find_element_by_xpath(UserElement.deposit_area_element).is_displayed()
        self.assertTrue(page_loaded, "User is not able to access to Deposit Area.")

    def Access_to_Withdrawal_Area(self):
        LoginpageActions.Login_to_Mainpage(self)
        print("<li>" + "Click on Announcement" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(LogInElement.notification_link).click()
        print("<li>" + "Click on Withdrawal Area" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserElement.withdrawal_area_link).click()
        # Wait page load
        wait_page_load = EC.presence_of_element_located((By.XPATH, UserElement.withdrawal_area_element))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        page_loaded = self.driver.find_element_by_xpath(UserElement.withdrawal_area_element).is_displayed()
        self.assertTrue(page_loaded, "User is not able to access to Withdrawal Area.")

    def Access_to_Funding_Records(self):
        LoginpageActions.Login_to_Mainpage(self)
        print("<li>" + "Click on Announcement" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(LogInElement.notification_link).click()
        print("<li>" + "Click on Funding Records" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserElement.funding_records_link).click()
        # Wait page load
        wait_page_load = EC.presence_of_element_located((By.XPATH, UserElement.funding_records_element))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        page_loaded = self.driver.find_element_by_xpath(UserElement.funding_records_element).is_displayed()
        self.assertTrue(page_loaded, "User is not able to access to Funding Records.")

    def Access_to_Betting_Record(self):
        LoginpageActions.Login_to_Mainpage(self)
        print("<li>" + "Click on Announcement" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(LogInElement.notification_link).click()
        print("<li>" + "Click on Betting Record" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserElement.betting_record_links).click()
        # Wait page load
        wait_page_load = EC.presence_of_element_located((By.XPATH, UserElement.betting_record_element))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        page_loaded = self.driver.find_element_by_xpath(UserElement.betting_record_element).is_displayed()
        self.assertTrue(page_loaded, "User is not able to access to Betting Record.")

    def Access_to_Member_Agent(self):
        LoginpageActions.Login_to_Mainpage(self)
        print("<li>" + "Click on Announcement" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(LogInElement.notification_link).click()
        print("<li>" + "Click on Member Agent" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserElement.member_agent_links).click()
        # Wait page load
        wait_page_load = EC.presence_of_element_located((By.XPATH, UserElement.member_agent_element))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        page_loaded = self.driver.find_element_by_xpath(UserElement.member_agent_element).is_displayed()
        self.assertTrue(page_loaded, "User is not able to access to Member Agent.")

    def Access_to_Announcement(self):
        LoginpageActions.Login_to_Mainpage(self)
        print("<li>" + "Click on Announcement" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(LogInElement.notification_link).click()
        print("<li>" + "Click on Announcement" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserElement.announcement_link).click()
        # Wait page load
        wait_page_load = EC.presence_of_element_located((By.XPATH, UserElement.announcement_element))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        page_loaded = self.driver.find_element_by_xpath(UserElement.announcement_element).is_displayed()
        self.assertTrue(page_loaded, "User is not able to access to Announcement.")

    def Access_to_Personal_Information(self):
        LoginpageActions.Login_to_Mainpage(self)
        print("<li>" + "Click on Announcement" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(LogInElement.notification_link).click()
        print("<li>" + "Click on Personal Information" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserElement.personal_information_link).click()
        # Wait page load
        wait_page_load = EC.presence_of_element_located((By.XPATH, UserElement.personal_information_element))
        WebDriverWait(self.driver, 20).until(wait_page_load)
        page_loaded = self.driver.find_element_by_xpath(UserElement.personal_information_element).is_displayed()
        self.assertTrue(page_loaded, "User is not able to access to personal information.")