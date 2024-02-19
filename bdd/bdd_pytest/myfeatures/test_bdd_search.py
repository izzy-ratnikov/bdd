import pytest
from pytest_bdd import scenario, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver import Keys
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


@scenario("search.feature", 'Basic AnimeGO Search')
def test_publish():
    pass


@given('the AnimeGO home page is displayed')
def ddg_home(driver):
    driver.get('https://animego.org/')


@when(parsers.parse('the user searches for "{phrase}"'))
def search_phrase(driver):
    element = driver.find_element(By.XPATH, "//*[@id='navbar-search']")
    element.click()
    element = driver.find_element(By.XPATH, "//div[2]//ul[2]/li[3]//input")
    element.send_keys("naruto")
    element = driver.find_element(By.XPATH, "//div[2]//ul[2]/li[3]//input")
    element.send_keys(Keys.RETURN)


@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(driver):
    assert driver.current_url == "https://animego.org/search/all?q=naruto"
