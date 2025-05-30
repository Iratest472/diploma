## Оглавление
- [Описание](#описание)
- [Структура](#структура)
- [Инструкция по работе с тестами](#инструкция)
- [Стек технологий](#стек-технологий)
- [Установка библиотек](#установка-библиотек)
- [Полезные ссылки](#полезные-ссылки)
- [Библиотеки](#библиотеки)

## Описание
Финальная работа по ручному тестированию: <ссылка>

**Сайт: [www.kinopoisk.ru](https://www.kinopoisk.ru/)**

**Продукт:** Кинопоиск

**Описание продукта:** Кинопоиск - это русскоязычный интернет-сервис и интернет-издание о кинематографе. С 2018 года — онлайн-кинотеатр. С 2020 года совместно с «Плюс Студией», продюсерским центром «Яндекса», производит и распространяет оригинальные фильмы и сериалы. 
«Кинопоиск» предоставляет информацию о кинофильмах, телесериалах, в том числе кадры, трейлеры, постеры, обои, а также данные о персонах, связанных с кино- и телепроизводством: актёрах, режиссёрах, продюсерах, сценаристах, операторах, композиторах, художниках и монтажёрах. Посетители могут ставить оценки фильмам и сериалам, добавлять их в ожидаемые, писать рецензии, покупать билеты в кинотеатры на сайте с компьютера или мобильных устройств. Имеется онлайн-кинотеатр с фильмами и сериалами по подписке «Яндекс. Плюс» или за отдельную плату. Приложение «Кинопоиск» можно устанавливать на Android и iOS, Apple TV, Smart TV (LG, Samsung и телевизоры на базе Android TV), игровые консоли PlayStation 4 и PlayStation 5.  

## Структура

pages - классы
* `api_page.py`
* `main_page.py` 

tests - тесты
* `tests/test_api.py` 
* `test_ui.py` 
  
`pytest.ini` - маркеры для запуска pytest

`README.md` - отчет-инструкция к работе

`config.py` - конфигурации

`requirements.txt` - зависимости

## Инструкция по работе с тестами
**Подготовка:**
1. Запускаем `VS Code`
2. Нажимаем `Ctrl+Shift+P` (или `Cmd+Shift+P` на macOS), чтобы открыть командную панель
3. Клонируем репозиторий `git clone` <ссылка на проект>
4. Создаем и активируем виртуальное окружение 
    `python -m venv venv`
    `venv\Scripts\activate`
5. Устанавливаем зависимости из файла `requirements.txt`. Команда `pip install -r requirements.txt`

*Перед запуском тестов в файл `config.py` необходимо добавить куки и ключ для доступа к API.* 

**Запуск API тестов:**

1. Команда `pytest tests/test_api.py --alluredir=./allure_result_api`
2. После завершения тестирования вводим команду `allure serve allure_result_api` для просмотра отчета о тестировании

**Запуск UI тестов:**

1. Команда `pytest tests/test_ui.py --alluredir=./allure_result_ui`
2. После завершения тестирования вводим команду `allure serve allure_result_ui` для просмотра отчета о тестировании

**Запуск всех тестов:**

1. Команду `pytest --alluredir=./allure_result_all`
2. После завершения тестирования вводим команду `allure serve allure_result_all` для просмотра отчета о тестировании

## Стек технологий
- **pytest** - основная библиотека для написания и выполнения тестов.
- **selenium** - библиотека для автоматизации UI тестирования.
- **requests** - библиотека для работы с HTTP-клиентом, используемая для API тестирования.
- **allure** - библиотека для генерации отчетов о выполнении тестов.

### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файла .gitignore]( https://www.toptal.com/developers/gitignore/)

### Библиотеки

- pip3 install pytest
- pip install selenium
- pip install webdriver-manager
- pip3 install requests
- pip install allure-pytest