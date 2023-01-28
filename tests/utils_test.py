import pytest
from utils import Data


data = Data("../data/posts.json", "../data/comments.json")


class TestData:
    def test_init_type_error(self):
        with pytest.raises(TypeError):
            data_new = Data("filename.png", "./data/posts.json")

    def test_get_posts_all(self):
        assert data.get_posts_all() != [], "JSON-файл с постами не содержит постов!"

    def test_get_comments_all(self):
        assert data.get_comments_all() != [], "JSON-файл с комментариями не содержит комментариев!"

    def test_get_posts_by_user_value_error(self):
        with pytest.raises(ValueError):
            data.get_posts_by_user("Alina")

    def test_get_posts_by_user(self):
        assert data.get_posts_by_user("ralf") == [], "Ошибка в получении поста"

    def test_get_comments_by_post_id_value_error(self):
        with pytest.raises(ValueError):
            data.get_comments_by_post_id("Привет")

    def test_get_comments_by_post_id(self):
        assert data.get_comments_by_post_id(8) == [], "Ошибка в получении комментария поста"

    def test_search_for_posts_value_error(self):
        with pytest.raises(TypeError):
            data.search_for_posts(5)

    def test_search_for_posts(self):
        assert data.search_for_posts("Еда") != [], "Постов с данным включением нет!"

    def test_get_post_by_pk(self):
        with pytest.raises(TypeError):
            data.get_post_by_pk("Еда")
