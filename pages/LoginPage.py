from pages.WebGeneric import WebGeneric
class Login(WebGeneric):
    def __init__(self, driver):
        WebGeneric.__init__(self,driver)
        self.driver = driver
        self.signin_nav="//a[text()='Sign In']"
        self.un_id="email"
        self.pwd_id="password"
        self.Sign_in="btnSignin"

    def zoomin_login(self, un, pwd):
        wg = WebGeneric(self.driver)
        wg.signin(self.signin_nav)
        wg.enter(self.un_id, un)
        wg.enter(self.pwd_id, pwd)
        wg.submit(self.Sign_in)

        # Login to the application
        # self.driver.find_element_by_xpath("//a[text()='Sign In']").click()
        # self.driver.find_element_by_xpath("//input[@placeholder='Email or Username']").send_keys(un)
        # self.driver.find_element_by_id("password").send_keys(pwd)
        # self.driver.find_element_by_id("btnSignin").click()
