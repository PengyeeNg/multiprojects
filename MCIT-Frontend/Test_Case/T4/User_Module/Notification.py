import unittest
from Setup.T4 import Base_Setup
from Elements.T4.user_page import UserpageElement
from Actions.T4.login_page import LoginpageActions
from Actions.T4.user_page import UserActions
import time


class UserNotificationModule(Base_Setup.BSetup):

    def test_TC_Notification_01_View_Notification(self):
        print("<b> Expected Results: Able to view notification details. </b>" + "<br>")
        LoginpageActions.Login_to_Mainpage(self)
        UserActions.Access_to_Notification(self)
        print("<li>" + "Click on a Notification" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserpageElement.notification_notification).click()
        time.sleep(1)
        notification_details = self.driver.find_element_by_class_name(UserpageElement.notification_details).is_displayed()
        # Assert
        self.assertTrue(notification_details,"Unable to view the notification details.")



if __name__ == '__main__':
    unittest.main()
