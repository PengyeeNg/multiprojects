import unittest
import SetUp.Base_SetUp
from Actions.announcement_page import Member_Message_Actions
from Actions.announcement_page import Announcement_Actions
from Elements.announcement_page import Member_Message_Element
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class Member_Mesage(SetUp.Base_SetUp.BSetUp):

    def test_TC_Member_Message_01_Batch_Deletion(self):
        Member_Message_Actions.Navigate_Member_Message(self)
        self.driver.find_element_by_xpath(Member_Message_Element.announcement_checkbox).click()
        self.driver.find_element_by_class_name(Member_Message_Element.batch_deletion_button).click()
        # Wait till dialog box displayed
        wait_batch_delete_confirmation = EC.presence_of_element_located((By.CLASS_NAME, Member_Message_Element.batch_delete_confirmation_ok_button))
        WebDriverWait(self.driver, 20).until(wait_batch_delete_confirmation)
        # Assert
        batch_delete_confirmation_dialog_box = self.driver.find_element_by_class_name(Member_Message_Element.batch_delete_confirmation_ok_button).is_displayed()
        self.assertTrue(batch_delete_confirmation_dialog_box, "User is not able to batch delete member message.")
        print("Expected Results: Delete Confirmation dialog box pooped out." + "<br>")

    def test_TC_Member_Message_02_Send_Notification(self):
        Member_Message_Actions.Navigate_Member_Message(self)
        self.driver.find_element_by_class_name(Member_Message_Element.site_notification_button).click()
        # Wait till dialog box displayed
        wait_send_notification_dialog_box = EC.presence_of_element_located((By.ID, Member_Message_Element.send_site_notification_save_button))
        WebDriverWait(self.driver, 20).until(wait_send_notification_dialog_box)
        # Assert
        send_notification_dialog_box = self.driver.find_element_by_id(Member_Message_Element.send_site_notification_save_button).is_displayed()
        self.assertTrue(send_notification_dialog_box, "User is not able to send notification")
        print("Expected Results: New Message dialog box pooped out." + "<br>")

    def test_TC_Member_Message_03_Delete_Notification(self):
        Member_Message_Actions.Navigate_Member_Message(self)
        self.driver.find_element_by_class_name(Member_Message_Element.delete_button).click()
        # Wait till dialog box displayed
        wait_delete_confirmation = EC.presence_of_element_located((By.CLASS_NAME, Member_Message_Element.delete_confirmation_ok_button))
        WebDriverWait(self.driver, 20).until(wait_delete_confirmation)
        # Assert
        delete_confirmation_dialog_box = self.driver.find_element_by_class_name(Member_Message_Element.delete_confirmation_ok_button).is_displayed()
        self.assertTrue(delete_confirmation_dialog_box, "User is not able to delete member message.")
        print("Expected Results: Delete Confirmation dialog box pooped out." + "<br>")

    def test_TC_Member_Message_04_View_All_Notification(self):
        Member_Message_Actions.Navigate_Member_Message(self)
        Announcement_Actions.View_All(self)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Member Message", "Page breaks after clicking All button.")
        print("Expected Results: Page does not break after clicking All button." + "<br>")

    def test_TC_Member_Message_05_Edit_Notification(self):
        Member_Message_Actions.Navigate_Member_Message(self)
        self.driver.find_element_by_class_name(Member_Message_Element.edit_button).click()
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Member Message", "Page breaks after clicking Edit button.")
        print("Expected Results: Page does not break after clicking Edit button." + "<br>")

    def test_TC_Member_Message_06_Table_Sorting_Member_Message(self):
        Member_Message_Actions.Navigate_Member_Message(self)
        print("<li>" + "Click on Recipient header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Message_Element.recipient_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Title header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Message_Element.title_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Time header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Message_Element.time_header_sorting).click()
        self.driver.implicitly_wait(30)
        print("<li>" + "Click on Status header" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Member_Message_Element.status_header_sorting).click()
        self.driver.implicitly_wait(30)
        # Assert
        no_break_page = self.driver.title
        self.assertEqual(no_break_page, "Member Message", "Page breaks after clicking table sorting.")
        print("Expected Results: Page does not break after clicking table sorting." + "<br>")


if __name__ == '__main__':
    unittest.main()
