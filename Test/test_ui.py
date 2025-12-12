import allure
from main_page import MainPage


@allure.epic("UI Тестирование")
@allure.feature("Поиск книжной информации")
class TestBookSearch:
    @allure.title("Поиск книги по заголовку")
    @allure.description("Тест проверяет возможность поиска книги по заголовку 'капитанская'.")
    def test_by_name(self, driver):
        main_page = MainPage(driver)

        main_page.search_book("капитанская")
        assert "капитанская" in main_page.get_search_results_text()

    @allure.title("Поиск автора")
    @allure.description("Тест проверяет возможность поиска автора 'пушкин'.")
    def test_by_name_author(self, driver):
        main_page = MainPage(driver)

        main_page.search_book("пушкин")
        assert "Показываем результаты по запросу «пушкин», найдено:" in main_page.get_search_results_text()

    @allure.title("Поиск книги на английском")
    @allure.description("Тест проверяет поиск книги с использование английского названия")
    def test_by_name_language_english(self, driver):
        main_page = MainPage(driver)

        main_page.search_book("house")
        assert "«house»" in main_page.get_search_results_text()

    @allure.title("Поиск книги с символами вместо названия")
    @allure.description("Тест проверяет поиск книги с использование символов вместо названия")
    def test_negative_by_symbols(self, driver):
        main_page = MainPage(driver)

        main_page.search_book("#$%")
        assert "«#$%»" in main_page.get_search_results_text()

    @allure.title("Поиск книги на тайском языке")
    @allure.description("Тест проверяет поиск книги с использование тайских символов в названии")
    def test_negative_by_language_thai(self, driver):
        main_page = MainPage(driver)

        main_page.search_book("เกาะมหาสมบัต")
        assert 'Результаты поиска «เกาะมหาสมบัต»' in main_page.get_search_results_text()