import pytest
from pytest_bdd import scenario, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='session', autouse=False)
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()


@scenario("url.feature", 'Basic AnimeGO Site')
def test_publish():
    pass


@given('the AnimeGO home page is displayed')
def ddg_home(driver):
    driver.get('https://animego.org/')


@when(parsers.parse('the user press the button anime'))
def search_phrase(driver):
    element = driver.find_element(By.XPATH, "//*[@class='nav-link']")
    element.click()


@then(parsers.parse('results equal url anime page'))
def search_results(driver):
    assert driver.current_url == 'https://animego.org/anime'
