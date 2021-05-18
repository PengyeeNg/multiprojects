import SetUp.Base_SetUp
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Actions.login_page import Login_Actions
from Elements.bank_page import Bank_Account_Element
from Elements.bank_page import Bank_Element

class Bank_Account_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Bank_Account(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Bank' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Bank_Element.bank).click()
        bank_account = EC.presence_of_element_located((By.XPATH, Bank_Account_Element.bank_account))
        WebDriverWait(self.driver, 10).until(bank_account)
        print("<li>" + "Select 'Bank Account'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Bank_Account_Element.bank_account).click()
        bank_account_page = self.driver.title
        self.assertEqual(bank_account_page, "Receiving Account Management", "User is not able to navigate to Bank Account Page.")
