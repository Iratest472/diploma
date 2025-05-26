from config import api_url, my_headers
from pages.api_page import KinoApi
import pytest
import allure

kino_api = KinoApi(api_url, my_headers)


@allure.feature("Поиск")
@allure.story("API")
@allure.title("Поиск фильмов по названию")
@pytest.mark.parametrize("film_title",
                         ["Девчата", "Мамы"])
def test_search_for_movie_by_name(film_title):
    resp = kino_api.search_for_movie_name(film_title)
    with allure.step(f"Поиск фильмов по названию {film_title}"):
        data = resp.json()
    with allure.step("Убедимся, что количество результатов поиска больше нуля"):
        assert "docs" in data and len(data["docs"]) > 0
        assert data["docs"][0]["name"] == film_title
    with allure.step("Проверка статуса ответа"):
        assert resp.status_code == 200


@allure.feature("Поиск")
@allure.story("API")
@allure.title("Поиск фильмов по id")
@pytest.mark.parametrize("film_id",
                         ["555554", "254887"])
def test_search_for_movie_by_id(film_id):
    resp = kino_api.search_for_movie_id(film_id)
    with allure.step(f"Поиск фильмов по id {film_id}"):
        assert resp.json()["id"] == int(film_id)
    with allure.step("Проверка статуса ответа"):
        assert resp.status_code == 200


@allure.feature("Поиск")
@allure.story("API")
@allure.title("Поиск актеров по имени")
@pytest.mark.parametrize("name_actors",
                         ["Ирина", "Денис"])
def test_search_for_actors_by_name(name_actors):
    resp = kino_api.search_for_actors_name(name_actors)
    with allure.step(f"Поиск фильмов по id {name_actors}"):
        assert resp.json()["docs"][0]["name"] == name_actors
    with allure.step("Проверка статуса ответа"):
        assert resp.status_code == 200


@allure.feature("Поиск")
@allure.story("API")
@allure.title("Поиск актеров по имени только цифрами")
@pytest.mark.parametrize("film_title", ["11111111", "1111111111"])
def test_search_for_movie_by_name_negative(film_title):
    resp = kino_api.search_for_movie_name(film_title)
    with allure.step("Проверка статуса ответа"):
        assert resp.status_code == 200


@allure.feature("Поиск")
@allure.story("API")
@allure.title("Поиск актеров по имени только дефисами")
@pytest.mark.parametrize("name_actors",
                         ["--------", "-------"])
def test_search_for_actors_by_name_negative(name_actors):
    resp = kino_api.search_for_actors_name(name_actors)
    with allure.step("Проверка статуса ответа"):
        assert resp.status_code == 200
