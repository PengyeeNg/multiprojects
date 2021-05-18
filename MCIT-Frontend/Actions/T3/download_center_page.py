from Setup.T3 import Base_Setup
from Elements.T3.download_center_page import DownloadCenterElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class DownloadCenterpageActions(Base_Setup.BSetup):

    def Access_to_Download_Center(self):
        def Access_to_Promotions(self):
            print("<li>" + "Click on Download Center tab" + "</li>" + "<br>")
            self.driver.find_element_by_xpath(DownloadCenterElement.download_center_tab).click()
            # Wait modal dialog load
            # wait_page_load = EC.element_to_be_clickable((By.XPATH, ))
            # WebDriverWait(self.driver, 20).until(wait_page_load)
