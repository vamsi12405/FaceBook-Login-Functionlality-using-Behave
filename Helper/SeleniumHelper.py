from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumHelper:
    def __init__(self, driver):
        self.driver = driver

    def page_url(self, url):
        self.driver.get(url)

    def input_val(self, xpath, value):
        self.driver.find_element(By.XPATH, xpath).send_keys(value)

    def input_click(self, xpath):
        self.driver.find_element(By.XPATH, xpath).click()

    def wait(self, xpath, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )