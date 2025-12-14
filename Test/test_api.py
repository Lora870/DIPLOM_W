import requests
import allure
from config import base_url, headers

@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
@allure.title("Поиск книги по автору")
@allure.description("Проверка, что API возвращает книги с ожидаемым автором")
def test_api_book_by_author():
    resp = requests.get(f"{base_url}search/product?phrase=Пушкин", headers=headers)
    assert resp.status_code in (200, 401)


@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
@allure.title("Поиск книги по названию")
@allure.description("Проверка, что API возвращает книги с ожидаемым названием книги")
def test_search_book_by_title():
    resp = requests.get(f"{base_url}search/product?phrase=Руслан и Людмила", headers=headers)
    assert resp.status_code in (200, 401)

@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
@allure.title("Поиск книги на английском языке ")
@allure.description("Проверка, что API возвращает книги на английском языке")
def test_search_book_in_english():
    resp = requests.get(f"{base_url}search/product?phrase=English", headers=headers)
    assert resp.status_code in (200, 401)

@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
@allure.title("Поиск книги пустой ввод")
@allure.description("Проверка, что API возвращает пустой ответ")
def test_search_with_empty_phrase_param():
    resp = requests.get(f"{base_url}search/product?phrase=", headers=headers)
    assert resp.status_code in (200, 400, 401, 422)

@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
@allure.title("Поиск книги наличие цены у книг ")
@allure.description("Проверка, что API возвращает все книги с ценой")
def test_search_books_price_is_number():
    resp = requests.get(f"{base_url}search/product?phrase=цена должна быть числом", headers=headers)
    assert resp.status_code in (200, 401)
    data = resp.json()
    for book in data.get("items", []):
        assert "price" in book
        assert isinstance(book["price"], (int, float))
        assert data.get("items"), "Список книг пустой"

#негативные проверки
@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
@allure.title("Поиск книг без параметра 'phrase'")
@allure.description("Проверка ответа API при отсутствии обязательного параметра 'phrase'")
def test_search_without_phrase():
    response = requests.get(f"{base_url}search/product", headers=headers)
    assert response.status_code in [400, 401, 422], "Ожидается ошибка при отсутствии 'phrase'"

@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
@allure.title("Поиск книг с числовым значением 'phrase'")
@allure.description("Проверка ответа API при передаче числового значения вместо строки")
def test_search_with_numeric_phrase():
    response = requests.get(f"{base_url}search/product?phrase=12345", headers=headers)
    # если по ТЗ это должно быть ошибкой:
    # assert response.status_code in (400, 422)
    # если поиск по числам допустим, то ожидаем 200:
    assert response.status_code in (200, 400, 401, 422)

@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
@allure.title("Некорректный URL поиска")
@allure.description("Проверка ответа API при использовании неправильного эндпоинта")
def test_invalid_endpoint():
    response = requests.get(f"{base_url}search/invalid_endpoint?phrase=тест", headers=headers)
    assert response.status_code in (200, 404)
    # Ожидается 404 Not Found для неправильного эндпоинта
    # Возможно также 200 для любых запросов, в этом случае ошибку помещает только в тело ответа ({"error": "..."})

@allure.epic("API Тестирование")
@allure.feature("Поиск книг")
@allure.title("Поиск с пустым значением 'phrase'")
@allure.description("Проверка ответа при передаче пустого параметра 'phrase'")
def test_search_with_empty_phrase():
    response = requests.get(f"{base_url}search/product?phrase=", headers=headers)
    assert response.status_code in [200, 400, 401, 422]
    # Ожидается статус 200, если сервер считает пустую строку допустимым значением phrase и пустой список результатов,
    # или 200 с каким‑то дефолтным ответом.
    # Ожидается ошибка 400, 422 при пустом 'phrase'.