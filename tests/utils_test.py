import pytest
import utils


def test_get_posts_all():
    assert utils.get_posts_all("./data/posts.json") != [], "JSON-файл с постами не содержит постов!"


def test_get_comments_all():
    assert utils.get_comments_all("./data/comments.json") != [], "JSON-файл с комментариями не содержит комментариев!"


def test_get_posts_by_user_value_error():
    with pytest.raises(ValueError):
        utils.get_posts_by_user("Alina", "./data/posts.json", "./data/comments.json")


def test_get_posts_by_user():
    assert utils.get_posts_by_user("ralf", "./data/posts.json", "./data/comments.json") == [], \
        "Ошибка в получении поста"


def test_get_comments_by_post_id_value_error():
    with pytest.raises(ValueError):
        utils.get_comments_by_post_id("Привет", "./data/posts.json", "./data/comments.json")


def test_get_comments_by_post_id():
    assert utils.get_comments_by_post_id(8, "./data/posts.json", "./data/comments.json") == [], \
        "Ошибка в получении комментария поста"


def test_search_for_posts_value_error():
    with pytest.raises(TypeError):
        utils.search_for_posts(5, "./data/posts.json")


def test_search_for_posts():
    assert utils.search_for_posts("Еда", "./data/posts.json") != [], "Постов с данным включением нет!"


def test_get_post_by_pk():
    with pytest.raises(TypeError):
        utils.get_post_by_pk("Еда", "./data/posts.json")
