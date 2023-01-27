import pytest
from utils import Data

# data = Data("../data/posts.json", "../data/comments.json")


class TestData:
    def test_init_type_error(self):
        with pytest.raises(TypeError):
            data = Data("pfpfpf")


# # Юнит-тесты к функции get_posts_all()
# assert data.get_posts_all() != [], "JSON-файл с постами не содержит постов!"
# assert len(data.get_posts_all()) != 0, "JSON-файл с постами не содержит постов!"
# # Юнит-тесты к функции get_comments_all()
# assert data.get_comments_all() != [], "JSON-файл с комментариями не содержит комментариев!"
# assert len(data.get_comments_all()) != 0, "JSON-файл с комментариями не содержит комментариев!"
# # Юнит-тест к функции get_posts_by_user(x)
# assert data.get_posts_by_user("leo") != [], "У пользователя отсутствуют посты!"
# # Юнит-тест к функции get_comments_by_post_id(x)
# assert data.get_comments_by_post_id(4) != [], "У поста отсутствуют комментарии!"
# # Юнит-тесты к функции search_for_posts(x)
# assert data.search_for_posts("Еда") != [], "Постов с данным включением нет!"
# assert data.search_for_posts("еда") != "Ошибка", "Вы ввели цифру!"
# # Юнит-тесты к функции get_post_by_pk(x)
# assert data.get_post_by_pk(3) != "Ошибка", "Вы ввели не число"
