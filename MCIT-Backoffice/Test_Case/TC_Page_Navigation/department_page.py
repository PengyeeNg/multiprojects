import unittest
import SetUp.Base_SetUp
from Actions.department_page import Permission_Actions
from Actions.department_page import Permission_List_Actions
from Actions.department_page import Role_List_Actions
from Actions.department_page import Route_List_Actions


class Navigate_Department_Modules(SetUp.Base_SetUp.BSetUp):

    def test_TC_Department_01_Navigate_Permission_Page(self):
        Permission_Actions.Navigate_Permission(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Department_02_Navigate_Permission_List_Page(self):
        Permission_List_Actions.Navigate_Permission_List(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Department_03_Navigate_Role_List_Page(self):
        Role_List_Actions.Navigate_Role_List(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

    def test_TC_Department_04_Navigate_Route_List_Page(self):
        Route_List_Actions.Navigate_Route_List(self)
        print("Expected Results: Able to access to the page without breaking." + "<br>")

if __name__ == '__main__':
    unittest.main()
