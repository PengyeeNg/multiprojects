from selenium.webdriver import ActionChains
from Setup.T4 import Base_Setup
from Input_Data.T4.Browser import BrowserData
from Elements.T4.main_page import MainpageElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
from Elements.T4.register_page import RegisterpageElement

class MainpageActions(Base_Setup.BSetup):

    def Access_to_Mainpage(self):
        print("<li>" + "Access to Frontend T4 Webpage: " + BrowserData.webpage_t4 + "</li>" + "<br>")
        self.driver.get(BrowserData.webpage_t4)
        time.sleep(3)
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

    def Access_to_Casino(self):
        print("<li>" + "Click on Casino Tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.casino_tab).click()
        # Wait the page loads
        time.sleep(3)
        # Assert
        page_title = self.driver.find_element_by_class_name(MainpageElement.page_title).text
        self.assertEqual(page_title, "THE MOST TRUSTED LIVE CASINO PROVIDER IN MALAYSIA", "Unable to access to casino page.")

    def Access_to_Slot(self):
        print("<li>" + "Click on Slot Tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.slot_tab).click()
        # Wait the page loads
        time.sleep(3)
        # Assert
        page_title = self.driver.find_element_by_class_name(MainpageElement.page_title).text
        self.assertEqual(page_title, "THE MOST TRUSTED SLOT PROVIDER IN MALAYSIA", "Unable to access to slot page.")

    def Access_to_Sport(self):
        print("<li>" + "Click on Sport Tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.sport_tab).click()
        # Wait the page loads
        time.sleep(3)
        # Assert
        page_title = self.driver.find_element_by_class_name(MainpageElement.page_title).text
        self.assertEqual(page_title, "THE MOST TRUSTED SPORTSBOOK PROVIDER IN MALAYSIA", "Unable to access to sport page.")

    def Access_to_Promo(self):
        print("<li>" + "Click on Promo Tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.promo_tab).click()
        # Wait the page loads
        time.sleep(3)
        # Assert
        promotions = self.driver.find_element_by_class_name(MainpageElement.promotion).is_displayed()
        self.assertTrue(promotions, "Unable to access to Promo page.")

    def Navigate_to_Live_Casino(self):
        print("<li>" + "Scroll down main page, and click on Live Casino" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.entitled_live_casino).click()
        # Wait the page loads
        time.sleep(3)
        # Assert
        page_title = self.driver.find_element_by_class_name(MainpageElement.page_title).text
        self.assertEqual(page_title, "THE MOST TRUSTED LIVE CASINO PROVIDER IN MALAYSIA", "Unable to access to casino page.")

    def Navigate_to_Slot_Games(self):
        print("<li>" + "Scroll down main page, and click on Slot Games" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.entitled_slot_games).click()
        # Wait the page loads
        time.sleep(3)
        # Assert
        page_title = self.driver.find_element_by_class_name(MainpageElement.page_title).text
        self.assertEqual(page_title, "THE MOST TRUSTED SLOT PROVIDER IN MALAYSIA", "Unable to access to slot games page.")

    def Navigate_to_Sports(self):
        print("<li>" + "Scroll down main page, and click on Sports" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(MainpageElement.entitled_sports).click()
        # Wait the page loads
        time.sleep(3)
        # Assert
        page_title = self.driver.find_element_by_class_name(MainpageElement.page_title).text
        self.assertEqual(page_title, "THE MOST TRUSTED SPORTSBOOK PROVIDER IN MALAYSIA", "Unable to access to sports page.")

    def Access_to_Register_Page(self):
        MainpageActions.Access_to_Mainpage(self)
        print("<li>" + "Click on Register button" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(RegisterpageElement.sign_up_button).click()
        # Wait the page loads
        time.sleep(2)









