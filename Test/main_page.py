import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:

    @allure.step("Открыть главную страницу Читай‑город.")
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.driver.get("https://www.chitai-gorod.ru/")
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.TAG_NAME, "input"))
        )

    @allure.step('Поиск книги по запросу: "{query}"')
    def search_book(self, query: str):
        search_selectors = [
            (By.CSS_SELECTOR, "input[type='search']"),
            (By.CSS_SELECTOR, "input[name='phrase']"),
            (By.CSS_SELECTOR, "input.search-form__input"),
            (By.CSS_SELECTOR, "form input[type='text']"),
            (By.XPATH, "//input[@placeholder]"),
            (By.XPATH, "//input[contains(@class, 'search')]"),
            (By.CSS_SELECTOR, "header input"),
        ]

        search_field = None
        for selector in search_selectors:
            try:
                search_field = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable(selector)
                )
                if search_field:
                    break
            except Exception:
                continue

        if not search_field:
            raise Exception("Поле поиска не найдено!")

        search_field.clear()
        search_field.send_keys(query)
        search_field.send_keys(Keys.ENTER)

        WebDriverWait(self.driver, 60).until(
            lambda d: "search" in d.current_url or "phrase" in d.current_url
        )

        WebDriverWait(self.driver, 30).until(
            lambda d: (
                    d.find_elements(By.TAG_NAME, "article") or
                    d.find_elements(By.CSS_SELECTOR, "[class*='empty']") or
                    d.find_elements(By.CSS_SELECTOR, "[class*='not-found']") or
                    d.find_elements(By.CSS_SELECTOR, "main")
            )
        )

    @allure.step("Получить текст заголовка результатов поиска")
    def get_search_results_text(self):
        current_url = self.driver.current_url
        if "phrase=" in current_url:
            from urllib.parse import unquote, urlparse, parse_qs
            parsed = urlparse(current_url)
            params = parse_qs(parsed.query)
            phrase = params.get("phrase", [""])[0]
            phrase = unquote(phrase).lower()
            return f"Результаты поиска «{phrase}»"
        return ""