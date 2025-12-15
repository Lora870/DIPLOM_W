import allure
from main_page import MainPage
from ui_test_data import (
    SEARCH_TITLE_CHERRY,
    SEARCH_AUTHOR_TEXT,
    SEARCH_ENGLISH_TEXT,
    SEARCH_SYMBOLS,
    SEARCH_THAI_TEXT,
    EXPECTED_TITLE_CHERRY,
    EXPECTED_AUTHOR_TEXT,
    EXPECTED_ENGLISH_TEXT,
    EXPECTED_SYMBOLS,
    EXPECTED_THAI_TEXT
)


@allure.epic("UI Тестирование")
@allure.feature("Поиск книжной информации")
class TestBookSearch:
    @allure.title("Поиск книги по заголовку")
    @allure.description("Тест проверяет возможность поиска книги по заголовку")
    def test_by_name(self, driver):
        main_page = MainPage(driver)

        main_page.search_book(SEARCH_TITLE_CHERRY)
        assert EXPECTED_TITLE_CHERRY in main_page.get_search_results_text()

    @allure.title("Поиск автора")
    @allure.description("Тест проверяет возможность поиска автора")
    def test_by_name_author(self, driver):
        main_page = MainPage(driver)

        main_page.search_book(SEARCH_AUTHOR_TEXT)
        assert EXPECTED_AUTHOR_TEXT in main_page.get_search_results_text()

    @allure.title("Поиск книги на английском")
    @allure.description("Тест проверяет поиск книги с использованием английского названия")
    def test_by_name_english(self, driver: object) -> None:
        main_page = MainPage(driver)

        main_page.search_book(SEARCH_ENGLISH_TEXT)
        assert EXPECTED_ENGLISH_TEXT in main_page.get_search_results_text()

    @allure.title("Поиск книги с символами вместо названия")
    @allure.description("Тест проверяет поиск книги с использование символов вместо названия")
    def test_negative_by_symbols(self, driver: object) -> None:
        main_page = MainPage(driver)

        main_page.search_book(SEARCH_SYMBOLS)
        assert EXPECTED_SYMBOLS in main_page.get_search_results_text()

    @allure.title("Поиск книги на тайском языке")
    @allure.description("Тест проверяет поиск книги с использование тайских символов в названии")
    def test_negative_by_thai(self, driver):
        main_page = MainPage(driver)

        main_page.search_book(SEARCH_THAI_TEXT)
        assert EXPECTED_THAI_TEXT in main_page.get_search_results_text()