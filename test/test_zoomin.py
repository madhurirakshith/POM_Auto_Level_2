from pages.LoginPage import Login
from pages.HomePage import Logout
from data.testdata import *
import pytest

@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_ZoominLogin(self):
        driver = self.driver
        lp = Login(driver)
        lp.zoomin_login(USERNAME, PASSWORD)

    def test_ZoominLogout(self):
        driver = self.driver
        hp = Logout(driver)
        hp.zoominlogout()