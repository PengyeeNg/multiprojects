import SetUp.Base_SetUp
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Actions.login_page import Login_Actions
from Elements.announcement_page import Member_Message_Element
from Elements.announcement_page import Announcement_Element

class Announcement_Actions(SetUp.Base_SetUp.BSetUp):
    def View_All(self):
        # Wait till button is clickable
        wait_all_button = EC.element_to_be_clickable((By.ID, Announcement_Element.all_button))
        WebDriverWait(self.driver, 30).until(wait_all_button)
        print("<li>" + "Click on All button" + "</li>" + "<br>")
        self.driver.find_element_by_id(Announcement_Element.all_button).click()
        self.driver.implicitly_wait(30)

class Member_Message_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Member_Message(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Announcement' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Announcement_Element.announcement).click()
        member_message = EC.presence_of_element_located((By.XPATH, Member_Message_Element.member_message))
        WebDriverWait(self.driver, 10).until(member_message)
        print("<li>" + "Select 'Member Message'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Message_Element.member_message).click()
        member_message_page = self.driver.title
        self.assertEqual(member_message_page, "Member Message", "User is not able to navigate to Member Message.")
