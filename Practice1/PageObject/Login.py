from selenium import webdriver
class Login:
    #locators
    Textbox_Username_Id = "Email"
    Textbox_Password_ID = "Password"
    Button_Login_Class = "button-1 login-button"

    def __init__(self,driver):
        self.driver = driver

    def Enter_Username(self,username):
        self.driver.find_element_by_id(self.Textbox_Username_Id).send_keys(username)

    def Enter_Password(self,password):
        self.driver.find_element_by_id(self.Textbox_Password_ID).send_keys(password)

    def Click_Login(self):
        self.driver.find_element_by_class(self.Button_Login_Class).click()
