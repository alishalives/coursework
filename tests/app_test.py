import pytest

from app import app


def test_app_posts_type():
    response = app.test_client().get('/api/posts')
    assert type(response.json) == list, "Возвращается не список"


# def test_app_post():
#     response = app.test_client().get('/api/posts/<int:id_post>')
#     assert type(response.json) == list
