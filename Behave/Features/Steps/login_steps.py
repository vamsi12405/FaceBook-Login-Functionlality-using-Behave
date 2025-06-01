import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Helper.SeleniumHelper import SeleniumHelper as SH
from Logs.log_file import AllureLoggingHandler as AL
from behave import *

login_url="https://www.facebook.com/login/"

@when("we input '{login_id}' and '{password}'")
def cred_are_given(context,login_id,password):
    SH(context.driver).page_url(login_url)
    AL().log("info","Page Opened")
    SH(context.driver).input_val("//input[@name='email']","{}".format(login_id))
    SH(context.driver).input_val("//input[@type='password']","{}".format(password))
    AL().log(logging.info,"Password Entered")
    SH(context.driver).input_click("//button[@name='login']")
    AL().log("info","Page Closed")

@then("Program tries to run")
def step_impl(context):
    flag=False
    try:
        element = SH(context.driver).wait("//a[@href='https://facebook.com/login/identify/']")
        print("test pass")
        flag=True

    except Exception as e:
        logging.error("Element not found after waiting for seconds")
        AL().log("error","Page Closed")
    return flag



