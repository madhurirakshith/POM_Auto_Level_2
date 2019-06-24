class Logout():
    def __init__(self, driver):
        self.driver = driver

    def zoominlogout(self):
            #Logout from the application
            self.driver.find_element_by_xpath("//span[text()='Madhuri']").click()
            self.driver.find_element_by_xpath("//a[text()='Log Out']").click()