import SetUp.Base_SetUp
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from Actions.login_page import Login_Actions
from Elements.department_page import Permission_Element
from Elements.department_page import Permission_List_Element
from Elements.department_page import Role_List_Element
from Elements.department_page import Route_List_Element
from Elements.department_page import Department_Element

class Permission_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Permission(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Department' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Department_Element.department).click()
        permission = EC.presence_of_element_located((By.XPATH, Permission_Element.permission))
        WebDriverWait(self.driver, 10).until(permission)
        print("<li>" + "Select 'Permission'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Permission_Element.permission).click()
        permission_page = self.driver.title
        self.assertEqual(permission_page, "Assignments", "User is not able to navigate to Permission Page.")

class Permission_List_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Permission_List(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Department' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Department_Element.department).click()
        permission_list = EC.presence_of_element_located((By.XPATH, Permission_List_Element.permission_list))
        WebDriverWait(self.driver, 10).until(permission_list)
        print("<li>" + "Select 'Permission List'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Permission_List_Element.permission_list).click()
        permission_list_page = self.driver.title
        self.assertEqual(permission_list_page, "Permissions", "User is not able to navigate to Permission List Page.")

class Role_List_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Role_List(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Department' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Department_Element.department).click()
        role_list = EC.presence_of_element_located((By.XPATH, Role_List_Element.role_list))
        WebDriverWait(self.driver, 10).until(role_list)
        print("<li>" + "Select 'Role List'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Role_List_Element.role_list).click()
        role_list_page = self.driver.title
        self.assertEqual(role_list_page, "Roles", "User is not able to navigate to Role List Page.")

class Route_List_Actions(SetUp.Base_SetUp.BSetUp):
    def Navigate_Route_List(self):
        Login_Actions.valid_login_flow(self)
        print("<li>" + "Click on 'Department' dropdown" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Department_Element.department).click()
        route_list = EC.presence_of_element_located((By.XPATH, Route_List_Element.route_list))
        WebDriverWait(self.driver, 10).until(route_list)
        print("<li>" + "Select 'Route List'" + "</li>" + "<br>")
        self.driver.find_element_by_xpath(Route_List_Element.route_list).click()
        route_list_page = self.driver.title
        self.assertEqual(route_list_page, "Routes", "User is not able to navigate to Routes Page.")
