import SetUp.Base_SetUp
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Actions.login_page import Login_Actions
from Elements.promotion_page import List_Promotion_Element
from Elements.promotion_page import Promotion_Banner_Element
from Elements.promotion_page import Promotion_Statistic_Element
from Elements.promotion_page import Promotion_Mission_Element
from Elements.promotion_page import Promotion_Element

class List_Promotion_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_List_Promotion(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Promotion' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Promotion_Element.promotion).click()
        list_promotion = EC.presence_of_element_located((By.XPATH, List_Promotion_Element.list_promotion))
        WebDriverWait(self.driver, 10).until(list_promotion)
        print("<li>" + "Select 'List Promotion'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(List_Promotion_Element.list_promotion).click()
        list_promotion_page = self.driver.title
        self.assertEqual(list_promotion_page, "Deposit Bonus Strategy", "User is not able to navigate to List Promotion Page.")

class Promotion_Banner_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Promotion_Banner(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Promotion' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Promotion_Element.promotion).click()
        promotion_banner = EC.presence_of_element_located((By.XPATH, Promotion_Banner_Element.promotion_banner))
        WebDriverWait(self.driver, 10).until(promotion_banner)
        print("<li>" + "Select 'Promotion Banner'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Promotion_Banner_Element.promotion_banner).click()
        promotion_banner_page = self.driver.title
        self.assertEqual(promotion_banner_page, "Activity Announcement List", "User is not able to navigate to Promotion Banner Page.")

class Promotion_Statistic_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Promotion_Statistic(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Promotion' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Promotion_Element.promotion).click()
        promotion_statistic = EC.presence_of_element_located((By.XPATH, Promotion_Statistic_Element.promotion_statistic))
        WebDriverWait(self.driver, 10).until(promotion_statistic)
        print("<li>" + "Select 'Promotion Statistic'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Promotion_Statistic_Element.promotion_statistic).click()
        promotion_statistic_page = self.driver.title
        self.assertEqual(promotion_statistic_page, "Deposit Bonus Strategy", "User is not able to navigate to Promotion Statistic Page.")

class Promotion_Mission_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Promotion_Mission(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Promotion' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Promotion_Element.promotion).click()
        promotion_mission = EC.presence_of_element_located((By.XPATH, Promotion_Mission_Element.promotion_mission))
        WebDriverWait(self.driver, 10).until(promotion_mission)
        print("<li>" + "Select 'Promotion Mission'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Promotion_Mission_Element.promotion_mission).click()
        promotion_mission_page = self.driver.title
        self.assertEqual(promotion_mission_page, "Member Promotion", "User is not able to navigate to Promotion Mission Page.")