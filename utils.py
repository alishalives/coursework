import json


class Data:
    def __init__(self, posts_path, comments_path):
        # if type(posts_path) or type(comments_path) != json:
        #     raise TypeError("Файлы должны быть json-формата!")
        self.posts_path = posts_path
        self.comments_path = comments_path

    # Функция загрузки постов
    def get_posts_all(self):
        with open(self.posts_path, 'r', encoding="utf-8") as file:
            posts = json.load(file)
            return posts

    # Функция загрузки комментариев
    def get_comments_all(self):
        with open(self.comments_path, 'r', encoding="utf-8") as file:
            comments = json.load(file)
            return comments

    # Функция возвращает посты определенного пользователя
    def get_posts_by_user(self, user_name):
        posts = self.get_posts_all()
        user_post = [post for post in posts if user_name.lower() == post["poster_name"].lower()]

        comments = self.get_comments_all()
        user_comment = [comment for comment in comments if user_name.lower() == comment["commenter_name"]]

        """Если введенного пользователя нет среди пользователей, публикующих
        посты, и среди комментирующих, функция вызывает ошибку ValueError.
        Если же он зафиксирован только среди комментаторов, то выводится []"""
        if len(user_post) == len(user_comment) == 0:
            raise ValueError("Такого пользователя нет")
        elif len(user_post) == 0:
            return user_post
        return user_post

    # Функция возвращает комментарии определенного поста
    def get_comments_by_post_id(self, post_id):
        comments = self.get_comments_all()
        post_comments = [comment for comment in comments if comment["post_id"] == int(post_id)]

        """Если поста с указанным post_id нет, то есть
        введенное число не лежит в диапазоне, указанном
        ниже, то функция вызывает ошибку ValueError.
        Если же у данного поста отсутствуют комментарии,
        функция выводит пустой список"""
        if int(post_id) not in range(1, len(self.get_posts_all()) + 1):
            raise ValueError("Посты по введенному id не найдены")
        elif len(post_comments) == 0:
            return post_comments
        return post_comments

    # Функция возвращает список постов по ключевому слову
    def search_for_posts(self, query):
        if str(query).isdigit():
            return "Ошибка"

        posts = self.get_posts_all()
        query_posts = [post for post in posts if query.lower() in post["content"].lower()]
        return query_posts

    # Функция возвращает пост по его идентификатору
    def get_post_by_pk(self, pk):
        if str(pk).isalpha():
            return "Ошибка"

        posts = self.get_posts_all()
        pk_post = [post for post in posts if post["pk"] == int(pk)]
        return pk_post


a = Data("./data/posts.json", "./data/comments.json")
# print(len(a.get_posts_all()))
# print(a.get_comments_by_post_id('5'))
# print(a.get_posts_by_user("leo"))
# print(a.search_for_posts("утром"))
# print(a.get_post_by_pk(2))
