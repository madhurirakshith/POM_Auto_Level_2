import pytest

@pytest.fixture(scope='class')
def test_setup(request):
    from selenium import webdriver
    driver = webdriver.Chrome(
        executable_path="C:/Users/Rakshith Yenadka/PycharmProjects/POM_Auto_Level_2/drivers/chromedriver.exe")
    driver.get("http://www.zoomin.com/in")
    driver.implicitly_wait(30)
    request.cls.driver = driver