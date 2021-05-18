import SetUp.Base_SetUp
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Actions.login_page import Login_Actions
from Elements.system_setting_page import QR_Code_Element
from Elements.system_setting_page import Parameter_Settings_Element
from Elements.system_setting_page import Task_Management_Element
from Elements.system_setting_page import Homepage_Carousel_Element
from Elements.system_setting_page import Third_Party_Settings_Element
from Elements.system_setting_page import File_Management_Element
from Elements.system_setting_page import CMS_Element
from Elements.system_setting_page import Frontend_registration_Settings_Element
from Elements.system_setting_page import Game_Maintenance_Element
from Elements.system_setting_page import Bet_Limit_Setting_Element
from Elements.system_setting_page import System_Setting_Element


class Qr_Code_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Qr_Code(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'System Setting' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(System_Setting_Element.system_setting).click()
        qr_code = EC.presence_of_element_located((By.XPATH, QR_Code_Element.qr_code))
        WebDriverWait(self.driver, 10).until(qr_code)
        print("<li>" + "Select 'QR Code'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(QR_Code_Element.qr_code).click()
        qr_code_page = self.driver.title
        self.assertEqual(qr_code_page, "Share Promotion Qr Code List", "User is not able to navigate to QR Code Page.")

class Parameter_Settings_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Parameter_Settings(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'System Setting' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(System_Setting_Element.system_setting).click()
        parameter_settings = EC.presence_of_element_located((By.XPATH, Parameter_Settings_Element.parameter_settings))
        WebDriverWait(self.driver, 10).until(parameter_settings)
        print("<li>" + "Select 'Parameter Settings'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Parameter_Settings_Element.parameter_settings).click()
        parameter_settings_page = self.driver.title
        self.assertEqual(parameter_settings_page, "Parameter Settings", "User is not able to navigate to Parameter Settings Page.")

class Task_Management_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Task_Management(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'System Setting' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(System_Setting_Element.system_setting).click()
        task_management = EC.presence_of_element_located((By.XPATH, Task_Management_Element.task_management))
        WebDriverWait(self.driver, 10).until(task_management)
        print("<li>" + "Select 'Task Management'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Task_Management_Element.task_management).click()
        task_management_page = self.driver.title
        self.assertEqual(task_management_page, "Task Management", "User is not able to navigate to Task Management Page.")

class Homepage_Carousel_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Homepage_Carousel(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'System Setting' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(System_Setting_Element.system_setting).click()
        homepage_carousel = EC.presence_of_element_located((By.XPATH, Homepage_Carousel_Element.homepage_carousel))
        WebDriverWait(self.driver, 10).until(homepage_carousel)
        print("<li>" + "Select 'Homepage Carousel'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Homepage_Carousel_Element.homepage_carousel).click()
        homepage_carousel_page = self.driver.title
        self.assertEqual(homepage_carousel_page, "Homepage Carousel", "User is not able to navigate to Homepage Carousel Page.")

class Third_Party_Settings_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Third_Party_Settings(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'System Setting' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(System_Setting_Element.system_setting).click()
        third_party_settings = EC.presence_of_element_located((By.XPATH, Third_Party_Settings_Element.third_party_settings))
        WebDriverWait(self.driver, 10).until(third_party_settings)
        print("<li>" + "Select 'Third Party Settings'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Third_Party_Settings_Element.third_party_settings).click()
        third_party_settings_page = self.driver.title
        self.assertEqual(third_party_settings_page, "Third-Party Payment Settings", "User is not able to navigate to Third Party Settings.")

class File_Management_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_File_Management(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'System Setting' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(System_Setting_Element.system_setting).click()
        file_management = EC.presence_of_element_located((By.XPATH, File_Management_Element.file_management))
        WebDriverWait(self.driver, 10).until(file_management)
        print("<li>" + "Select 'File Management'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(File_Management_Element.file_management).click()
        file_management_page = self.driver.title
        self.assertEqual(file_management_page, "File", "User is not able to navigate to File Management Page.")

class CMS_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_CMS(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'System Setting' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(System_Setting_Element.system_setting).click()
        cms = EC.presence_of_element_located((By.XPATH, CMS_Element.cms))
        WebDriverWait(self.driver, 10).until(cms)
        print("<li>" + "Select 'CMS'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(CMS_Element.cms).click()
        cms_page = self.driver.title
        self.assertEqual(cms_page, "List Page", "User is not able to navigate to CMS Page.")

class Fronted_Registration_Settings_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Frontend_Registration_Settings(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'System Setting' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(System_Setting_Element.system_setting).click()
        frontend_registration_settings = EC.presence_of_element_located((By.XPATH, Frontend_registration_Settings_Element.fronted_registration_settings))
        WebDriverWait(self.driver, 10).until(frontend_registration_settings)
        print("<li>" + "Select 'Frontend Registration Settings'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Frontend_registration_Settings_Element.fronted_registration_settings).click()
        frontend_registration_settings_page = self.driver.title
        self.assertEqual(frontend_registration_settings_page, "Frontend Registration Settings", "User is not able to navigate to Frontend Registration Settings.")

class Game_Maintenance_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Game_Maintenance(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'System Setting' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(System_Setting_Element.system_setting).click()
        game_maintenance = EC.presence_of_element_located((By.XPATH, Game_Maintenance_Element.game_maintenence))
        WebDriverWait(self.driver, 10).until(game_maintenance)
        print("<li>" + "Select 'Game Maintenance'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Game_Maintenance_Element.game_maintenence).click()
        game_maintenance_page = self.driver.title
        self.assertEqual(game_maintenance_page, "Game Maintenance", "User is not able to navigate to Game Maintenance Page.")

class Bet_Limit_Setting_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Bet_Limit_Setting(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'System Setting' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(System_Setting_Element.system_setting).click()
        bet_limit_setting = EC.presence_of_element_located((By.XPATH, Bet_Limit_Setting_Element.bet_limit_setting))
        WebDriverWait(self.driver, 10).until(bet_limit_setting)
        print("<li>" + "Select 'Bet Limit Setting'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Bet_Limit_Setting_Element.bet_limit_setting).click()
        bet_limit_setting_page = self.driver.title
        self.assertEqual(bet_limit_setting_page, "Bet Limit Setting", "User is not able to navigate to Bet Limit Setting Page.")