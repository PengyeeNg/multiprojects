from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import SetUp.Base_SetUp
from Elements.login_page import Login_Element
from Input_Data.login_page import Login_Data
from selenium.webdriver.common.by import By
from Elements.main_page import MainPage_Element

class Login_Actions(SetUp.Base_SetUp.BSetUp):

    def insert_username(self):
        self.driver.find_element_by_id(Login_Element.username).send_keys(Login_Data.username)

    def insert_password(self):
        self.driver.find_element_by_id(Login_Element.password).send_keys(Login_Data.password)

    def insert_invalid_password(self):
        self.driver.find_element_by_id(Login_Element.password).send_keys(Login_Data.invalid_password)

    def insert_invalid_username(self):
        self.driver.find_element_by_id(Login_Element.username).send_keys(Login_Data.invalid_username)

    def click_log_in_button(self):
        self.driver.find_element_by_name(Login_Element.log_in_button).click()

    def find_incorrect_value_prompt(self):
        self.driver.find_element_by_name(Login_Element.incorrect_password_prompt)

    def find_rememberme_checkbox(self):
        self.driver.find_element_by_id(Login_Element.remember_me_checkbox)

    def valid_login_flow(self):
        print("<li>" + "Insert valid username" + "</li>" + "<br>")
        Login_Actions.insert_username(self)
        self.driver.implicitly_wait(10)
        print("<li>" + "Insert valid password" + "</li>" + "<br>")
        Login_Actions.insert_password(self)
        self.driver.implicitly_wait(10)
        print("<li>" + "Click on login button" + "</li>" + "<br>")
        Login_Actions.click_log_in_button(self)
        logo_available = EC.presence_of_element_located((By.XPATH, MainPage_Element.main_page_title))
        WebDriverWait(self.driver, 10).until(logo_available)
        main_page = self.driver.find_element_by_xpath(MainPage_Element.main_page_title).is_displayed()
        self.assertTrue(main_page, "User is not able to access to Backoffice Main Page.")