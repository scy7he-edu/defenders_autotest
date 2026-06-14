# Defenders Autotest 🛡️

[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-enabled-green.svg)](https://playwright.dev/python/)
[![Allure](https://img.shields.io/badge/Allure-Report-yellow.svg)](https://docs.qameta.io/allure/)

Проект для автоматизированного E2E тестирования веб-приложения на базе **Python**, **Pytest** и **Playwright**. Отчеты о прохождении тестов генерируются с помощью **Allure**, включая автоматическое прикрепление скриншотов при падении тестов.

## 🛠 Технологический стек
* **Язык**: Python
* **Тестовый фреймворк**: Pytest
* **Автоматизация браузера**: Playwright
* **Отчетность**: Allure Reports
* **Конфигурация**: python-dotenv

## 🚀 Установка и настройка

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/scy7he-edu/defenders_autotest
   cd defenders_autotest
   ```

2. **Создайте и активируйте виртуальное окружение:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Linux/macOS
   # или
   venv\Scripts\activate  # Для Windows
   ```

3. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Установите браузеры Playwright:**
   ```bash
   playwright install chromium
   ```
   *(Вы можете установить все браузеры, написав просто `playwright install`)*

5. **Настройте переменные окружения:**
   Создайте файл `.env` в корневой директории проекта и добавьте тестовые учетные данные, указанные в `.env.example`:
   ```env
   EMAIL = 'your e-mail'
   PASSWORD = 'your password'
   ```

## 🏃‍♂️ Запуск тестов

Для запуска всех тестов с генерацией сырых данных Allure создайте папку `allure-results` в корневом каталоге и выполните:
```bash
pytest --alluredir=allure-results
```

Для запуска тестов с графическим интерфейсом браузера (Headed mode):
```bash
pytest --headed --alluredir=allure-results
```

## 📊 Просмотр отчетов Allure

После выполнения тестов сгенерируйте и откройте HTML-отчет Allure:
```bash
allure serve allure-results
```