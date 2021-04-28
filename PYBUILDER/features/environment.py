from behave import *
from selenium import webdriver

def before_scenario(context, scenario):
    print("Starting new scenario...")  
    context.driver = webdriver.Chrome()    
    entorno = str(context.config.userdata.get("entorno"))
    print("LA URL!!",entorno)

def after_scenario(context, scenario):    
    print("Ending current scenario...")  
    context.driver.quit()