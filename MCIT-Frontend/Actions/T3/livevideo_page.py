from Setup.T3 import Base_Setup
from Elements.T3.livevideo_page import LiveVideoElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class LiveVideopageActions(Base_Setup.BSetup):

    def Access_to_LiveVideo_Page(self):
        print("<li>" + "Click on Live Video tab" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(LiveVideoElement.live_video_tab).click()



