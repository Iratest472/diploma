import pytest
import allure
from selenium import webdriver
from pages.main_page import MainPage
from config import main_url, cookies


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    driver.get(main_url)

    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.get(main_url)
    return MainPage(driver, main_url)


@allure.feature("Smoke")
@allure.story("UI")
@allure.title("Проверка заголовка главной страницы")
@pytest.mark.smoke
def test_check_main_page_title(main_page):
    with allure.step("Заголовок главной страницы"):
        assert main_page.check_page_title(
            "Кинопоиск. Онлайн кинотеатр. Фильмы сериалы мультфильмы и энциклопедия")


@allure.feature("Поиск")
@allure.story("UI")
@allure.title("Поиск фильмов по названию")
@pytest.mark.parametrize("film_title",
                         ["Аватар", "Такси 4"])
def test_search_book_by_title(main_page, film_title):
    with allure.step(f"Поиск фильмов по названию"
                     f" {film_title}"):
        main_page.search_items_by_phrase(film_title)
    with allure.step("Количество результатов больше 0"):
        assert main_page.get_search_results_count() > 0
    with allure.step(f"Название фильма содержится в результатах"):
        assert film_title in main_page.find_book_titles()


@allure.feature("Поиск")
@allure.story("UI")
@allure.title("Поиск персонажей по имени")
@pytest.mark.parametrize("person_name",
                         ["Леонардо Ди Каприо", "Квентин Тарантино"])
def test_search_person_by_name(main_page, person_name):
    """ Тестируем возможность поиска актеров, режиссеров и др. персонажи по имени. """
    with allure.step(f"Ищем персонаж по имени {person_name}"):
        main_page.search_items_by_phrase(person_name)

    with allure.step("Убедимся, что количество результатов поиска больше нуля"):
        assert main_page.get_search_results_count() > 0, \
               f"Ничего не найдено по запросу '{person_name}'. Ожидаем минимум один результат."

    with allure.step(f"Убеждаемся, что имя {person_name} встречается в списке результатов"):
        results_list = main_page.find_person_names()
        assert any(name.lower() == person_name.lower() for name in results_list), \
               f"Имя '{person_name}' не обнаружено в результатах поиска."


@allure.feature("Поиск")
@allure.story("UI")
@allure.title("Поиск фильмов по названию только дефисы")
@pytest.mark.parametrize("film_title",
                         ["-----", "-----"])
def test_search_book_by_title_negative(main_page, film_title):
    with allure.step(f"Поиск фильмов по названию"
                     f" {film_title}"):
        main_page.search_items_by_phrase(film_title)
    with allure.step("Количество результатов больше 0"):
        assert main_page.get_search_results_count() > 0
    with allure.step(f"Название фильма содержится в результатах"):
        assert film_title in main_page.find_book_titles()


@allure.feature("Поиск")
@allure.story("UI")
@allure.title("Поиск персонажей по имени только пробелами")
@pytest.mark.parametrize("person_name",
                         ["       ", "       "])
def test_search_person_by_name_negative(main_page, person_name):
    """ Тестируем возможность поиска актеров, режиссеров и др. персонажи по имени. """
    with allure.step(f"Ищем персонаж по имени {person_name}"):
        main_page.search_items_by_phrase(person_name)

    with allure.step("Убедимся, что количество результатов поиска больше нуля"):
        assert main_page.get_search_results_count() > 0, \
               f"Ничего не найдено по запросу '{person_name}'. Ожидаем минимум один результат."

    with allure.step(f"Убеждаемся, что имя {person_name} встречается в списке результатов"):
        results_list = main_page.find_person_names()
        assert any(name.lower() == person_name.lower() for name in results_list), \
               f"Имя '{person_name}' не обнаружено в результатах поиска."
