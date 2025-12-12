import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:

    @allure.step("Открыть главную страницу Читай‑город")
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.driver.get("https://www.chitai-gorod.ru")

    @allure.step('Поиск книги по запросу: "{query}"')
    def search_book(self, query: str):
        search_field = self.driver.find_element(By.NAME, "search")
        search_field.clear()
        search_field.send_keys(query)
        self.driver.find_element(
            By.CLASS_NAME,
            "search-form__icon-search"
        ).click()
        WebDriverWait(self.driver, 40).until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "search-title__head"),
                query
            )
        )

    @allure.step("Получить текст заголовка результатов поиска")
    def get_search_results_text(self):
        return self.driver.find_element(
            By.CLASS_NAME,
            "search-title__head"
        ).text