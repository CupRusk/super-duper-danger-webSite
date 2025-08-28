# Super Duper Danger Website

## Описание

Веб-проект, состоящий из фронтенда и бэкенда. Реализует регистрацию пользователей и работу с IP-адресами.

### Структура проекта

- **front-end/** — клиентская часть (HTML, CSS, JS)
  - `html/` — страницы сайта (`index.html`, `register.html`)
  - `css/` — стили сайта (`block.css`, `style.css`)
  - `js/` — скрипты для взаимодействия с сервером (`index.js`, `login.js`)
- **back-end/** — серверная часть (Python)
  - `main.py` — основной файл запуска сервера
  - `logic/db/` — работа с базой данных (`database.py`, `models.py`)
  - `logic/router/` — обработка маршрутов API
    - `ip/find_ip.py` — работа с IP
    - `register/enter.py`, `register/register.py` — регистрация и вход
  - `IP.db` — база данных SQLite

## Запуск проекта

### 1. Установка зависимостей
Убедитесь, что установлен Python 3.13 и необходимые библиотеки (например, FastAPI, sqlite3).

### 2. Запуск бэкенда
```powershell
python back-end/main.py
```

### 3. Запуск фронтенда
Откройте файл `front-end/html/index.html` в браузере.

## API
- `POST /api/register` — регистрация пользователя
- Другие маршруты реализованы в папке `back-end/logic/router/`

## Авторы
- CupRusk(Денис), Solevoy(Даня)

## Лицензия
MIT
