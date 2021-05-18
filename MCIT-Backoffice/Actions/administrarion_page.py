import SetUp.Base_SetUp
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Actions.login_page import Login_Actions
from Elements.administration_page import Administration_Log_Element
from Elements.administration_page import Administration_List_Element
from Elements.administration_page import Administration_Element


class Admin_Log_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Admin_Log(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Administration' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Administration_Element.administration).click()
        admin_log = EC.presence_of_element_located((By.XPATH, Administration_Log_Element.administration_log))
        WebDriverWait(self.driver, 10).until(admin_log)
        print("<li>" + "Select 'Admin Log'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Administration_Log_Element.administration_log).click()
        admin_log_page = self.driver.title
        self.assertEqual(admin_log_page, "Administratir Operation Log", "User is not able to navigate to Admin Log Page.")

class Admin_List_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Admin_List(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Administration' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Administration_Element.administration).click()
        admin_list = EC.presence_of_element_located((By.XPATH, Administration_List_Element.administration_list))
        WebDriverWait(self.driver, 10).until(admin_list)
        print("<li>" + "Select 'Admin List'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Administration_List_Element.administration_list).click()
        admin_list_page = self.driver.title
        self.assertEqual(admin_list_page, "Admin Management", "User is not able to navigate to Admin List Page.")
