from behave import *
from selenium import webdriver
import time

def before_scenario(context, scenario):
    print("Starting new scenario...")
    context.driver = webdriver.Chrome()
    time.sleep(5)
    
    
def after_scenario(context, scenario):
    print("Finishing scenario...")
    context.driver.quit()