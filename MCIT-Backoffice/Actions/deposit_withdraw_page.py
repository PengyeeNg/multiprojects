import SetUp.Base_SetUp
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Actions.login_page import Login_Actions
from Elements.deposit_withdraw_page import Deposit_History_Element
from Elements.deposit_withdraw_page import Deposit_Element
from Elements.deposit_withdraw_page import Withdrawal_Element
from Elements.deposit_withdraw_page import Withdraw_History_Element
from Elements.deposit_withdraw_page import Adjust_Balance_Element
from Elements.deposit_withdraw_page import Account_Transaction_Record_Element
from Elements.deposit_withdraw_page import Bonus_Element
from Elements.deposit_withdraw_page import Commission_Record_Element
from Elements.deposit_withdraw_page import Adjustment_Record_Element
from Elements.deposit_withdraw_page import Turn_Over_Amount_Record_Element
from Elements.deposit_withdraw_page import Wallet_Transfer_Element
from Elements.deposit_withdraw_page import Deposit_Withdraw_Element
from Input_Data.deposit_withdraw_page import Deposit_Withdraw_Data

class Deposit_Withdraw_Actions(SetUp.Base_SetUp.BSetUp):
    def Filter_Deposit_Withdraw(self):
        print("<li>" + "Click on add icon at the end of filter column" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Deposit_Withdraw_Element.filter_add_button).click()
        wait_filter_column_expand = EC.presence_of_element_located((By.CLASS_NAME, Deposit_Withdraw_Element.filter_search_button))
        WebDriverWait(self.driver, 10).until(wait_filter_column_expand)
        print("<li>" + "Insert Username" + "</li>" + "<br>")
        self.driver.find_element_by_id(Deposit_Withdraw_Element.username_filter_field).send_keys(Deposit_Withdraw_Data.username_filter)
        print("<li>" + "Click on Search button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Deposit_Withdraw_Element.filter_search_button).click()

    def Assert_Search_results(self):
        # Verify filter results
        filtered_results = EC.text_to_be_present_in_element((By.CLASS_NAME, Deposit_Withdraw_Element.no_results_found),"No results found.")
        WebDriverWait(self.driver, 10).until(filtered_results)
        print("Expected Results: Filtered results = No results found." + "<br>")

    def View_All(self):
        # Wait till button is clickable
        wait_all_button = EC.element_to_be_clickable((By.CLASS_NAME, Deposit_Withdraw_Element.all_button))
        WebDriverWait(self.driver, 30).until(wait_all_button)
        print("<li>" + "Click on All button" + "</li>" + "<br>")
        self.driver.find_element_by_class_name(Deposit_Withdraw_Element.all_button).click()


class Deposit_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Deposit(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Deposit/Withdraw' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Deposit_Withdraw_Element.deposit_withdraw).click()
        new_deposit = EC.presence_of_element_located((By.XPATH, Deposit_Element.deposit))
        WebDriverWait(self.driver, 10).until(new_deposit)
        print("<li>" + "Select 'Deposit'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Deposit_Element.deposit).click()
        new_deposit_page = self.driver.title
        self.assertEqual(new_deposit_page, "Deposit Management", "User is not able to navigate to New Deposit Page.")

class Deposit_History_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Deposit_History(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Deposit/Withdraw' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Deposit_Withdraw_Element.deposit_withdraw).click()
        deposit = EC.presence_of_element_located((By.XPATH, Deposit_History_Element.deposit_history))
        WebDriverWait(self.driver, 10).until(deposit)
        print("<li>" + "Select 'Deposit History'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Deposit_History_Element.deposit_history).click()
        deposit_page = self.driver.title
        self.assertEqual(deposit_page, "Deposit Management", "User is not able to navigate to Deposit Page.")

class Withdrawal_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Withdrawal(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Deposit/Withdraw' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Deposit_Withdraw_Element.deposit_withdraw).click()
        new_withdrawal = EC.presence_of_element_located((By.XPATH, Withdrawal_Element.withdrawal))
        WebDriverWait(self.driver, 10).until(new_withdrawal)
        print("<li>" + "Select 'Withdrawal'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Withdrawal_Element.withdrawal).click()
        new_withdrawal_page = self.driver.title
        self.assertEqual(new_withdrawal_page, "Withdrawal Management", "User is not able to navigate to New Withdrawal Page.")

class Withdraw_History_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Withdraw_History(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Deposit/Withdraw' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Deposit_Withdraw_Element.deposit_withdraw).click()
        withdraw = EC.presence_of_element_located((By.XPATH, Withdraw_History_Element.withdraw_history))
        WebDriverWait(self.driver, 10).until(withdraw)
        print("<li>" + "Select 'Withdraw History'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Withdraw_History_Element.withdraw_history).click()
        withdraw_page = self.driver.title
        self.assertEqual(withdraw_page, "Withdrawal Management", "User is not able to navigate to Withdraw Page.")

class Adjust_Balance_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Adjust_Balance(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Deposit/Withdraw' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Deposit_Withdraw_Element.deposit_withdraw).click()
        adjust_balance = EC.presence_of_element_located((By.XPATH, Adjust_Balance_Element.adjust_balance))
        WebDriverWait(self.driver, 10).until(adjust_balance)
        print("<li>" + "Select 'Adjust Balance'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Adjust_Balance_Element.adjust_balance).click()
        adjust_balance_page = self.driver.title
        self.assertEqual(adjust_balance_page, "Adjust Balance (Batch)", "User is not able to navigate to Adjust Balance Page.")

class Account_Transaction_Record_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Account_Transaction_Record(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Deposit/Withdraw' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Deposit_Withdraw_Element.deposit_withdraw).click()
        account_transaction_record = EC.presence_of_element_located((By.XPATH, Account_Transaction_Record_Element.account_transaction))
        WebDriverWait(self.driver, 10).until(account_transaction_record)
        print("<li>" + "Select 'Account Transaction Record'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Account_Transaction_Record_Element.account_transaction).click()
        account_transaction_record_page = self.driver.title
        self.assertEqual(account_transaction_record_page, "Account Turnover", "User is not able to navigate to Account Transaction Page.")

class Bonus_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Bonus(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Deposit/Withdraw' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Deposit_Withdraw_Element.deposit_withdraw).click()
        bonus = EC.presence_of_element_located((By.XPATH, Bonus_Element.bonus))
        WebDriverWait(self.driver, 10).until(bonus)
        print("<li>" + "Select 'Bonus'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Bonus_Element.bonus).click()
        bonus_page = self.driver.title
        self.assertEqual(bonus_page, "Bonus Management", "User is not able to navigate to Bonus Page.")

class Commission_Record_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Commision_Record(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Deposit/Withdraw' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Deposit_Withdraw_Element.deposit_withdraw).click()
        commission_record = EC.presence_of_element_located((By.XPATH, Commission_Record_Element.commission_record))
        WebDriverWait(self.driver, 10).until(commission_record)
        print("<li>" + "Select 'Commission Record'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Commission_Record_Element.commission_record).click()
        commission_record_page = self.driver.title
        self.assertEqual(commission_record_page, "Member Commission Details", "User is not able to navigate to Commission Record Page.")

class Adjustment_Record_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Adjustment_Record(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Deposit/Withdraw' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Deposit_Withdraw_Element.deposit_withdraw).click()
        adjustment_record = EC.presence_of_element_located((By.XPATH, Adjustment_Record_Element.adjustment_record))
        WebDriverWait(self.driver, 10).until(adjustment_record)
        print("<li>" + "Select 'Adjustment Record'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Adjustment_Record_Element.adjustment_record).click()
        adjustment_record_page = self.driver.title
        self.assertEqual(adjustment_record_page, "Adjustment Record", "User is not able to navigate to")

class Turn_Over_Amount_Record_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Turn_Over_Amount_Record(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Deposit/Withdraw' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Deposit_Withdraw_Element.deposit_withdraw).click()
        turn_over_amount_record = EC.presence_of_element_located((By.XPATH, Turn_Over_Amount_Record_Element.turn_over_amount))
        WebDriverWait(self.driver, 10).until(turn_over_amount_record)
        print("<li>" + "Select 'Turn Over Amount Record'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Turn_Over_Amount_Record_Element.turn_over_amount).click()
        turn_over_amount_record_page = self.driver.title
        self.assertEqual(turn_over_amount_record_page, "Turn Over Amount Record", "User is not able to navigate to Turn Over Amount Record Page.")

class Wallet_Transfer_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Wallet_Transfer(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Deposit/Withdraw' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Deposit_Withdraw_Element.deposit_withdraw).click()
        wallet_transfer = EC.presence_of_element_located((By.XPATH, Wallet_Transfer_Element.wallet_transfer))
        WebDriverWait(self.driver, 10).until(wallet_transfer)
        print("<li>" + "Select 'Wallet Transfer'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Wallet_Transfer_Element.wallet_transfer).click()
        wallet_transfer_page = self.driver.title
        self.assertEqual(wallet_transfer_page, "Wallet Transfer", "User is not able to navigate to Wallet Transfer Page.")