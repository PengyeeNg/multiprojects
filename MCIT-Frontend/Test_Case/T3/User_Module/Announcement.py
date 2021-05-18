import unittest
from Actions.T3.user_page import UserpageActions
from Elements.T3.user_page import UserElement
from Input_Data.T3.user_page import UserData
from Setup.T3 import Base_Setup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

class AnnouncementModule(Base_Setup.BSetup):

    def test_TC_Announcement_01_Navigate_to_AnnouncementPage(self):
        print("<b> Expected Results: Able to view announcement page. </b>" + "<br>")
        UserpageActions.Access_to_Announcement(self)
        time.sleep(3)
        # Assert
        announcement_detail = self.driver.find_element_by_xpath(UserElement.announcement_details).text
        self.assertNotEqual(announcement_detail, "", "Announcement is not available.")


if __name__ == '__main__':
    unittest.main()
