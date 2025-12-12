import requests
import allure
from config import base_url, headers

@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
@allure.title("Поиск книги по автору")
@allure.description("Проверка, что API возвращает книги с ожидаемым автором.")
def test_api_book_by_author():
    resp = requests.get(f"{base_url}search/product?phrase=Пушкин", headers=headers)
    assert resp.status_code == 200


@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
@allure.title("Поиск книги по названию")
@allure.description("Проверка, что API возвращает книги с ожидаемым названием книги.")
def test_api_book_by_author():
    resp = requests.get(f"{base_url}search/product?phrase=Руслан и Людмила", headers=headers)
    assert resp.status_code == 200

@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
@allure.title("Поиск книги на английском языке ")
@allure.description("Проверка, что API возвращает книги на английском языке.")
def test_api_book_by_author():
    resp = requests.get(f"{base_url}search/product?phrase=English", headers=headers)
    assert resp.status_code == 200

@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
@allure.title("Поиск книги пустой ввод ")
@allure.description("Проверка, что API возвращает пустой ответ.")
def test_api_book_by_author():
    resp = requests.get(f"{base_url}search/product?phrase=пустой ответ", headers=headers)
    assert resp.status_code == 200

@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
@allure.title("Поиск книги наличие цены у книг ")
@allure.description("Проверка, что API возвращает все книги с ценой ")
def test_api_book_by_author():
    resp = requests.get(f"{base_url}search/product?phrase=цена должна быть числом", headers=headers)
    assert resp.status_code == 200

#негативные проверки
@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
@allure.title("Поиск книг без параметра 'phrase'")
@allure.description("Проверка ответа API при отсутствии обязательного параметра 'phrase'")
def test_search_without_phrase():
    response = requests.get(f"{base_url}search/product", headers=headers)
    assert response.status_code == 400 or response.status_code == 422, "Ожидается ошибка при отсутствии 'phrase'"

@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
@allure.title("Поиск книг с некорректным типом 'phrase'")
@allure.description("Проверка ответа API при передаче числового значения вместо строки")
def test_search_with_numeric_phrase():
    response = requests.get(f"{base_url}search/product?phrase=12345", headers=headers)
    assert response.status_code == 400 or response.status_code == 422, "Ожидается ошибка при некорректном типе 'phrase'"

@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
@allure.title("Некорректный URL поиска")
@allure.description("Проверка ответа API при использовании неправильного эндпоинта")
def test_invalid_endpoint():
    response = requests.get(f"{base_url}search/invalid_endpoint?phrase=тест", headers=headers)
    assert response.status_code == 404, "Ожидается 404 Not Found для неправильного эндпоинта"

@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
@allure.title("Поиск с пустым значением 'phrase'")
@allure.description("Проверка ответа API при передаче пустого параметра 'phrase'")
def test_search_with_empty_phrase():
    response = requests.get(f"{base_url}search/product?phrase=", headers=headers)
    assert response.status_code == 400 or response.status_code == 422, "Ожидается ошибка при пустом 'phrase'"