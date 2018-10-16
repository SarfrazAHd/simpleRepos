class HomePage():
    def __int__(self,driver):
        self.driver=driver
        self.welcome_link_id="welcome"
        self.logout_link_txt= "logout"



    def click_Welcome(self, welcome):
        self.welcome=welcome
        self.driver.find_element_by_id(self.welcome_link_id).click()

    def click_Lgout(self, logout):
        self.logout=logout

        self.driver.find_element_link_text(self.logout_link_txt).click()