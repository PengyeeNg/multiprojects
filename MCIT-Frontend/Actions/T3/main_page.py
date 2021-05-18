from selenium.webdriver import ActionChains
from Setup.T3 import Base_Setup
from Input_Data.T3.Browser import BrowserData
from Elements.T3.main_page import MainpageElement
from Elements.T3.signup_page import SignUppageElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class MainpageActions(Base_Setup.BSetup):

    def Access_to_Mainpage(self):
        print("<li>" + "Access to Frontend T3 Webpage: " + BrowserData.webpage_t3 + "</li>" + "<br>")
        self.driver.get(BrowserData.webpage_t3)
        # Wait the page loads
        wait_main_page = EC.element_to_be_clickable((By.CLASS_NAME, MainpageElement.announcement_modal_dialog_close_button))
        WebDriverWait(self.driver, 20).until(wait_main_page)
        # Close Announcement dialog box
        print("<li>" + "Close the Announcement modal dialog" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(MainpageElement.announcement_modal_dialog_close_button).click()
        self.driver.implicitly_wait(10)
        # Assert
        main_page = self.driver.title
        self.assertEqual(main_page, "Platform","User is not able to access to main page.")

    def Scroll_to_Main_Page_Bottom(self):
        print("<li>" + "Scroll to the bottom of the main page" + "</li>" + "<br>")
        scroll_to_bottom = self.driver.find_element_by_class_name(MainpageElement.main_bottom_page)
        actions = ActionChains(self.driver)
        actions.move_to_element(scroll_to_bottom).perform()
        self.driver.implicitly_wait(10)

    def Access_to_SignUp_Page(self):
        print("<li>" + "Access to Frontend T3 Webpage: " + BrowserData.webpage_t3 + "</li>" + "<br>")
        self.driver.get(BrowserData.webpage_t3)
        # Wait the page loads
        wait_main_page = EC.element_to_be_clickable((By.CLASS_NAME, MainpageElement.announcement_modal_dialog_close_button))
        WebDriverWait(self.driver, 20).until(wait_main_page)
        # Close Announcement dialog box
        print("<li>" + "Close the Announcement modal dialog" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(MainpageElement.announcement_modal_dialog_close_button).click()
        self.driver.implicitly_wait(10)
        # Assert
        main_page = self.driver.title
        self.assertEqual(main_page, "Platform", "User is not able to access to main page.")
        print("<li>" + "Click on sign up button" + "</li>" + "<br>")
        self.driver.find_element_by_css_selector(SignUppageElement.sign_up).click()
        self.driver.refresh()
        # Wait the page loads
        wait_main_page = EC.element_to_be_clickable((By.CLASS_NAME, MainpageElement.announcement_modal_dialog_close_button))
        WebDriverWait(self.driver, 20).until(wait_main_page)
        # Close Announcement dialog box
        print("<li>" + "Close the Announcement modal dialog" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(MainpageElement.announcement_modal_dialog_close_button).click()
        self.driver.implicitly_wait(10)
        # Assert
        main_page = self.driver.title
        self.assertEqual(main_page, "Platform", "User is not able to access to main page.")
        print("<li>" + "Click on sign up button" + "</li>" + "<br>")
        self.driver.find_element_by_css_selector(SignUppageElement.sign_up).click()
        #  Wait page loads
        # wait_sign_up = EC.visibility_of_element_located((By.ID, SignUppageElement.username_field))
        # WebDriverWait(self.driver, 10).until(wait_sign_up)
        # Assert
        # sign_up_button = self.driver.find_element_by_id(SignUppageElement.username_field).is_displayed()
        # self.assertTrue(sign_up_button, "User is not able to access to Sign Up Modal Dialog.")


