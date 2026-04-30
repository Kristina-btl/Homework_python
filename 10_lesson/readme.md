# Проект автотестов с Page Object и Allure

## Установка и запуск

```bash
# Установка зависимостей
pip install selenium pytest allure-pytest

# Запуск всех тестов
pytest --alluredir=allure-results

# Запуск тестов калькулятора
pytest test_01_calc.py --alluredir=allure-results

# Запуск тестов магазина
pytest test_02_shop.py --alluredir=allure-results

# Просмотр отчета в браузере
allure serve allure-results

# Или генерация статического отчета
allure generate allure-results -o allure-report --clean

# Затем открыть allure-report/index.html
```

## Структура проекта

```
lesson_10/
├── CalculatorPage.py            # Page Object для калькулятора
├── FormPage.py                  # Page Object для формы
├── ShopPage.py                  # Page Object для магазина
├── test_01_calc.py              # Тесты калькулятора с задержками
├── test_02_shop.py              # Тесты интернет-магазина
├── requirements.txt             # Файл зависимостей
├── README.md                    # Этот файл
└── .gitignore                   # Файл для игнорирования (рекомендуется добавить)
```

## Описание тестов


### 1. Тест калькулятора (test_01_calc.py)
- **Цель:** Проверить математические операции
- **Операции:** Сложение, вычитание, умножение, деление
- **Особенность:** Учет задержки вычислений (5-20 секунд)

### 2. Тест магазина (test_02_shop.py)
- **Цель:** Проверить оформление заказа
- **Процесс:** Авторизация → Добавление товаров → Оформление
- **Ожидание:** Итоговая сумма = $58.29