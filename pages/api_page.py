import requests
import allure
from selenium.webdriver.common.by import By


class KinoApi:
    def __init__(self, api_url: str, my_headers) -> None:
        self.api_url = api_url
        self.my_headers = my_headers

    @allure.step("Получаем названия фильмов")
    def search_for_movie_name(self, movie_name: str):
        my_params = {
            'page': 1,
            'limit': 1,
            'query': movie_name}
        resp = requests.get(self.api_url + 'v1.4/movie/search', params=my_params, headers=self.my_headers)
        return resp

    def search_for_movie_id(self, movie_id: str):
        my_params = {
        }
        resp = requests.get(self.api_url + f'v1.4/movie/{movie_id}', params=my_params, headers=self.my_headers)
        return resp

    def search_for_actors_name(self, actors_name: str):
        my_params = {
            'page': 1,
            'limit': 1,
            'query': actors_name}
        resp = requests.get(self.api_url + 'v1.4/person/search', params=my_params, headers=self.my_headers)
        return resp

    @allure.step("Поиск контента по фразе: {phrase}")
    def search_items_by_phrase(self, phrase):
        self._wait_for_elements(By.CSS_SELECTOR, "input[name=kp_query]").send_keys(phrase)
        self.driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
