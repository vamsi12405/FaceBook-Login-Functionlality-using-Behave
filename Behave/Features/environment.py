from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def before_scenario(context,scenario):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

def after_scenario(context,scenario):
    print("chrom driver closed")
    context.driver.close()


