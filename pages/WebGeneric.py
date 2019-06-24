class WebGeneric:
    def __init__(self, driver):
        self.driver = driver

    def signin(self, locator):
        self.driver.find_element_by_xpath(locator).click()

    def enter(self, locator, input_val):
        self.driver.find_element_by_id(locator).send_keys(input_val)

    def submit(self, locator):
        self.driver.find_element_by_id(locator).click()