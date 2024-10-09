import pytest
from selenium import webdriver
from locators.account_page_locators import *
from locators.main_page_locators import *
from helpers.constants import URL
from helpers.generator import *
from page_object.main_page import MainPage


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get(URL.BASE)
    yield driver
    driver.quit()

@pytest.fixture
def create_user():
    login_pass, token = create_new_user()
    yield login_pass, token
    requests.delete('https://stellarburgers.nomoreparties.site/api/auth/user', headers={'Authorization': f'{token}'})


@pytest.fixture
def signin(driver, create_user):
    page = MainPage(driver)
    page.go_to_site(URL.BASE)
    page.click_element(MainPageLocators.ENTER_BUTTON)
    page.send_keys(ResetPassPageLocators.INPUT_EMAIL, create_user[0][0])
    page.send_keys(ResetPassPageLocators.INPUT_PASSWORD, create_user[0][1])
    page.click_element(ResetPassPageLocators.ENTER_BUTTON)
    page.wait_until_element_visibility(10, MainPageLocators.CONSTRUCTOR_TITLE)