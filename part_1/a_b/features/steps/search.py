from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.HomePage import HomePage
from pages.AbstractaHomePage import AbstractaHomePage

from utilities import ConfigReader

import time
TIME_TO_WAIT = int(ConfigReader.read_configuration("Time","wait"))

KEY_WORD = ConfigReader.read_configuration("Search","key_word")

@given(u'I’m on the homepage')
def step_impl(context):
    assert context.driver.title == "Google"


@when(u'I type “test automation” into the search field')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.type_test_automation()
    


@when(u'I click the Google Search button')
def step_impl(context):
    context.home_page.click_search_button()


@then(u'I go to the search results page, and the first 3 results contain the word “automation”')
def step_impl(context):

    #Scroll down slowly through the page
    context.home_page.scroll_down(3)
    
    #Get the web site names
    web_site_names = context.home_page.get_web_site_names()

    #Check if the first 3 results contain the word “automation”
    names = 0
    for web_site_name in web_site_names:
        if len(web_site_name.text) > 0 and names < 3:
            print(web_site_name.text)
            assert "automation" in web_site_name.text.lower()
            names += 1
        elif names == 3:
            break
    

# Second scenario

@given(u'I search by keyword')
def step_impl(context):

    context.home_page = HomePage(context.driver)
    context.home_page.type_test_automation()
    context.home_page.click_search_button()

@when(u'I click on the first result link')
def step_impl(context):
    context.home_page.click_first_result()

@then(u'I go to the page, and the page title contains the word "automation”')
def step_impl(context):
    context.abstracta_home_page = AbstractaHomePage(context.driver)
    assert "automation" in context.abstracta_home_page.get_tittle_page().lower()