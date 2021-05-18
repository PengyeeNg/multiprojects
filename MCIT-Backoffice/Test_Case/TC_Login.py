import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import SetUp.Base_SetUp
from Actions.login_page import Login_Actions
from Actions.main_page import MainPage_Actions
from Elements.login_page import Login_Element
from Elements.main_page import MainPage_Element
from selenium.webdriver.support import expected_conditions as EC
import SetUp.Base_SetUp
from Input_Data.Browser import Browser_Data
import pickle


class Login(SetUp.Base_SetUp.BSetUp):

    def test_TC_Login_01_Valid_Login(self):

        Login_Actions.valid_login_flow(self)
        print("Expected Results: User is able to access to Backoffice Main Page." + "<br>")

    def test_TC_Login_02_Invalid_Login_Password(self):
        print("<li>" + "Insert valid username" + "</li>" + "<br>")
        Login_Actions.insert_username(self)
        self.driver.implicitly_wait(10)
        print("<li>" + "Insert invalid password" + "</li>" + "<br>")
        Login_Actions.insert_invalid_password(self)
        self.driver.implicitly_wait(10)
        print("<li>" + "Click on login button" + "</li>" + "<br>")
        Login_Actions.click_log_in_button(self)
        prompt = EC.presence_of_element_located((By.CSS_SELECTOR, Login_Element.incorrect_password_prompt))
        WebDriverWait(self.driver, 10).until(prompt)
        self.driver.implicitly_wait(10)
        prompt_message = self.driver.find_element_by_css_selector(Login_Element.incorrect_password_prompt).text
        self.assertEqual(prompt_message, 'Incorrect Username Or Password', "Error Prompt is not displayed.")
        print("Expected Results: Alert prompted without navigating to Backoffice Main Page." + "<br>")

    def test_TC_Login_03_Invalid_Login_Username(self):
        print("<li>" + "Insert invalid username" + "</li>" + "<br>")
        Login_Actions.insert_invalid_username(self)
        self.driver.implicitly_wait(10)
        print("<li>" + "Insert valid password" + "</li>" + "<br>")
        Login_Actions.insert_password(self)
        self.driver.implicitly_wait(10)
        print("<li>" + "Click on login button" + "</li>" + "<br>")
        Login_Actions.click_log_in_button(self)
        prompt = EC.presence_of_element_located((By.CSS_SELECTOR, Login_Element.incorrect_password_prompt))
        WebDriverWait(self.driver, 10).until(prompt)
        self.driver.implicitly_wait(10)
        prompt_message = self.driver.find_element_by_css_selector(Login_Element.incorrect_password_prompt).text
        self.assertEqual(prompt_message, 'Incorrect Username Or Password', "Error Prompt is not displayed.")
        print("Expected Results: Alert prompted without navigating to Backoffice Main Page." + "<br>")

    def test_TC_Login_04_Login_with_Empty_Value_Password(self):
        print("<li>" + "Insert valid username" + "</li>" + "<br>")
        Login_Actions.insert_username(self)
        self.driver.implicitly_wait(10)
        print("<li>" + "Click on login button" + "</li>" + "<br>")
        Login_Actions.click_log_in_button(self)
        prompt = EC.presence_of_element_located((By.CSS_SELECTOR, Login_Element.blank_password_prompt))
        WebDriverWait(self.driver, 10).until(prompt)
        prompt_message = self.driver.find_element_by_css_selector(Login_Element.blank_password_prompt).text
        self.assertEqual(prompt_message, "Password cannot be blank.", "Error Prompt is not displayed/ incorrect.")
        print("Expected Results: Alert prompted without navigating to Backoffice Main Page." + "<br>")

    def test_TC_Login_05_Login_with_Empty_Value_Username(self):
        print("<li>" + "Insert valid password" + "</li>" + "<br>")
        Login_Actions.insert_password(self)
        self.driver.implicitly_wait(10)
        print("<li>" + "Click on login button" + "</li>" + "<br>")
        Login_Actions.click_log_in_button(self)
        prompt = EC.presence_of_element_located((By.CSS_SELECTOR, Login_Element.blank_username_prompt))
        WebDriverWait(self.driver, 10).until(prompt)
        prompt_message = self.driver.find_element_by_css_selector(Login_Element.blank_username_prompt).text
        self.assertEqual(prompt_message, "Username cannot be blank.", "Error Prompt is not displayed/ incorrect.")
        print("Expected Results: Alert prompted without navigating to Backoffice Main Page." + "<br>")

    def test_TC_Login_06_Remember_Me_Checked(self):
        print("<li>" + "Insert valid username" + "</li>" + "<br>")
        Login_Actions.insert_username(self)
        self.driver.implicitly_wait(10)
        print("<li>" + "Insert valid password" + "</li>" + "<br>")
        Login_Actions.insert_password(self)
        self.driver.implicitly_wait(10)
        print("<li>" + "Check 'Remember Me' checkbox" + "</li>" + "<br>")
        remember_me = self.driver.find_element_by_id(Login_Element.remember_me_checkbox)
        if remember_me.is_selected():
            print("<li>" + "Click on login button" + "</li>" + "<br>")
            Login_Actions.click_log_in_button(self)
        else:
            self.driver.find_element_by_id(Login_Element.remember_me_checkbox).is_selected()
            self.driver.implicitly_wait(10)
            print("<li>" + "Click on login button" + "</li>" + "<br>")
            Login_Actions.click_log_in_button(self)
        logo_available = EC.presence_of_element_located((By.XPATH, MainPage_Element.main_page_title))
        WebDriverWait(self.driver, 10).until(logo_available)
        main_page = self.driver.find_element_by_xpath(MainPage_Element.main_page_title).is_displayed()
        self.assertTrue(main_page, "User is not able to access to Backoffice Main Page.")
        # Add cookies
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        print("<li>" + "Re-access to Backoffice Webpage" + "</li>" + "<br>")
        self.driver.get(Browser_Data.test_url)
        logo_available = EC.presence_of_element_located((By.XPATH, MainPage_Element.main_page_title))
        WebDriverWait(self.driver, 10).until(logo_available)
        main_page = self.driver.find_element_by_xpath(MainPage_Element.main_page_title).is_displayed()
        self.assertTrue(main_page, "User is not able to re-access to Backoffice Main Page.")
        print("Expected Results: Navigated to Backoffice Main Page without the needs of re-sign in." + "<br>")

    def test_TC_Login_07_Remember_Me_Unchecked(self):
        print("<li>" + "Insert valid username" + "</li>" + "<br>")
        Login_Actions.insert_username(self)
        self.driver.implicitly_wait(10)
        print("<li>" + "Insert valid password" + "</li>" + "<br>")
        Login_Actions.insert_password(self)
        self.driver.implicitly_wait(10)
        print("<li>" + "Uncheck 'Remember Me' checkbox" + "</li>" + "<br>")
        remember_me = self.driver.find_element_by_id(Login_Element.remember_me_checkbox)
        if remember_me.is_selected():
            self.driver.find_element_by_id(Login_Element.remember_me_checkbox).click()
            print("<li>" + "Click on login button" + "</li>" + "<br>")
            Login_Actions.click_log_in_button(self)
        else:
            print("<li>" + "Click on login button" + "</li>" + "<br>")
            Login_Actions.click_log_in_button(self)
        logo_available = EC.presence_of_element_located((By.XPATH, MainPage_Element.main_page_title))
        WebDriverWait(self.driver, 10).until(logo_available)
        main_page = self.driver.find_element_by_xpath(MainPage_Element.main_page_title).is_displayed()
        self.assertTrue(main_page, "User is not able to access to Backoffice Main Page.")
        # Add cookies
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        print("<li>" + "Re-access to Backoffice Webpage" + "</li>" + "<br>")
        self.driver.get(Browser_Data.test_url)
        sign_in_page = self.driver.title
        self.assertEqual(sign_in_page, "Sign In", "User is not able to navigate to Sign In Page.")
        print("Expected Results: Navigated to Backoffice Sign In Page." + "<br>")

    def test_TC_Login_08_Log_Out(self):

        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on the username dropdown" + "</li>" + "<br>")
        MainPage_Actions.click_username_dropdown(self)
        username_dropdown_menu = EC.presence_of_element_located((By.XPATH, MainPage_Element.username_dropdown_menu))
        WebDriverWait(self.driver, 10).until(username_dropdown_menu)
        print("<li>" + "Click on sign out button" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainPage_Element.log_out_button).click()
        sign_in_page = self.driver.title
        self.assertEqual(sign_in_page, "Sign In", "User is not able to log out and navigated to Sign In Page.")
        print("Expected Results: Account logged out and navigated to Sign In Page." + "<br>")


if __name__ == '__main__':
    unittest.main()
