class LoginPage():


    def __init__(self,driver):
        self.driver=driver
        self.txt_userName_id= "txtUsername"
        self.txt_passWord_id = "Password"
        self.login_id= "btnLogin"


    def enter_username(self,userName):
        self.useraName=userName
        self.driver.find_element_by_id(self.driver.find_element_by_id()).clear()
        self.driver.find_element_by_id(self.driver.find_element_by_id()).send_keys(userName)

    def enter_passWord(self, password):
        self.password = password
        self.driver.find_element_by_id(self.driver.find_element_by_id()).clear()
        self.driver.find_element_by_id(self.txt_passWord_id).send_keys(password)


    def click_login(self):
        self.driver.find_element_by_id(self.login_id).click()