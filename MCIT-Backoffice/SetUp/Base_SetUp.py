import base64
import unittest
import os
from datetime import datetime
from selenium.webdriver.common.by import By
from Input_Data.Browser import Browser_Data
from selenium import webdriver
from Elements.login_page import Login_Element
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BSetUp(unittest.TestCase):
    # Define folder's name format
    folder_date = datetime.now().strftime('%Y%m%d')
    # Define path to save test evidence
    screenshot_path = r"C:\Users\Lenovo\PycharmProjects\MCIT-Backoffice\Screenshot\Test_Evidence-%s" % folder_date
    if not os.path.exists(screenshot_path):
        os.mkdir(screenshot_path)

    def setUp(self):
        # create a new Chrome session
        self.driver = webdriver.Chrome(Browser_Data.chrome_path)
        # Maximize the window
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        print("<li>" + "Access to Backoffice Webpage" + "</li>" + "<br>")
        self.driver.get(Browser_Data.test_url)
        try:
            logo_available = EC.presence_of_element_located((By.XPATH, Login_Element.page_logo))
            WebDriverWait(self.driver, 10).until(logo_available)
        except:
            print("Unable to Access to URL")
            self.driver.close()

    def tearDown(self):
        # Define image's name format
        test_name = self.id()
        image_date_time = datetime.now().strftime('_%H%M%S')
        # Capture test evidence with test name and timestamp
        file_name = "%s" % test_name
        evidence_id = file_name + "%s.png" % image_date_time
        name = os.path.join(BSetUp.screenshot_path, evidence_id)
        self.driver.get_screenshot_as_file(name)

        # Convert test evidence into base64 format
        data_uri = base64.b64encode(open(name, 'rb').read()).decode('utf-8')
        img_tag = '<img src="data:image/png;base64,{0}" width="929" height="420">'.format(data_uri)
        # Include test evidence name and images in test report
        print("Actual Results:" + "<br>")
        print(img_tag)
        # print(" Test Evidence ID: " + evidence_id)
        # Close the Chrome driver
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
