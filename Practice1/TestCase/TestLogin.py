from selenium import webdriver
import pytest
from PageObject.Login import Login

class Test_Login():

    url = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"

    def testlogin(self):
        driver = webdriver.Chrome(executable_path="C:\\Program Files (x86)\\Python 3.9\\Drivers\\chromedriver.exe")
        login = Login(driver)
        login.Enter_Username(self.username)
        login.Enter_Password(self.password)
        login.Click_Login()

