from selenium import webdriver
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
#
# @pytest.fixture(params=["chrome", "firefox"])
# def driver(request):
#     if request.param == "chrome":
#         driver_instance = webdriver.Chrome()
#     else:
#         driver_instance = webdriver.Firefox()
#
#     yield driver_instance
#     driver_instance.quit()