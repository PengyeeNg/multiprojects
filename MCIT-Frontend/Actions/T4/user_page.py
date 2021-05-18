from Setup.T4 import Base_Setup
from Elements.T4.user_page import UserpageElement

class UserActions(Base_Setup.BSetup):

    def Access_to_Account(self):
        print("<li>" + "Click on Account" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserpageElement.account_tab).click()

    def Access_to_Profile(self):
        print("<li>" + "Click on Profile" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserpageElement.profile_tab).click()

    def Access_to_Referrer(self):
        print("<li>" + "Click on Referrer" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserpageElement.referrer_tab).click()

    def Access_to_Notification(self):
        print("<li>" + "Click on Notification" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(UserpageElement.notification_tab).click()




