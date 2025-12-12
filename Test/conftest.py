import pytest
from selenium import webdriver

# Фикстура для инициализации и закрытия драйвера.
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(50)
    yield driver
    driver.quit()