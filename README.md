# Диплом

## Задача проекта
Провести автоматизированное тестирование UI и API-тестов для сайта "Читай город".

## Шаблон для автоматизации тестирования на python

### Шаги
1. Склонировать проект 'git clone'
2. Установить зависимости
3. Запустить тесты 'pytest'

### Стек
- pytest
- selenium
- request
- allure

### Запуск тестов:
-   pytest          # все тесты
-   pytest -m ui    # только UI-тесты
    pytest -m api   # только API-тесты

### Структура
- test_api - тесты АПИ
- test_ui - тесты UI
  
### Библиотеки
- pip install pytest
- pip install selenium
- pip install webdriver-manager
- pip install allure