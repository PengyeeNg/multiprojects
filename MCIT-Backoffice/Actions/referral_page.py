import SetUp.Base_SetUp
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Actions.login_page import Login_Actions
from Elements.referral_page import Member_Map_Element
from Elements.referral_page import Referral_Element

class Member_Map_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_New_Member_Map(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Referral' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Referral_Element.referral).click()
        member_map = EC.presence_of_element_located((By.XPATH, Member_Map_Element.member_map))
        WebDriverWait(self.driver, 10).until(member_map)
        print("<li>" + "Select 'Member Map'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Map_Element.member_map).click()
        member_map_page = self.driver.title
        self.assertEqual(member_map_page, "Relationship Member Map", "User is not able to navigate to Member Map Page.")