import json


# Функция загрузки постов
def get_posts_all(posts_path):
    with open(posts_path, 'r', encoding="utf-8") as file:
        posts = json.load(file)
        return posts


def get_comments_all(comments_path):
    with open(comments_path, 'r', encoding="utf-8") as file:
        comments = json.load(file)
        return comments


def get_posts_by_user(user_name, posts_path, comments_path):
    posts = get_posts_all(posts_path)
    user_post = [post for post in posts if user_name.lower() == post["poster_name"].lower()]

    comments = get_comments_all(comments_path)
    user_comment = [comment for comment in comments if user_name.lower() == comment["commenter_name"]]

    """Если введенного пользователя нет среди пользователей, публикующих
    посты, и среди комментирующих, функция вызывает ошибку ValueError.
    Если же он зафиксирован только среди комментаторов, то выводится []"""
    if len(user_post) == len(user_comment) == 0:
        raise ValueError("Такого пользователя нет")
    elif len(user_post) == 0:
        return user_post
    return user_post


def get_comments_by_post_id(post_id, post_path, comments_path):
    comments = get_comments_all(comments_path)
    post_comments = [comment for comment in comments if comment["post_id"] == int(post_id)]

    """Если поста с указанным post_id нет, то есть
    введенное число не лежит в диапазоне, указанном
    ниже, то функция вызывает ошибку ValueError.
    Если же у данного поста отсутствуют комментарии,
    функция выводит пустой список"""
    if int(post_id) not in range(1, len(get_posts_all(post_path)) + 1):
        raise ValueError("Посты по введенному id не найдены")
    elif len(post_comments) == 0:
        return post_comments
    return post_comments


def search_for_posts(query, posts_path):
    if type(query) != str:
        raise TypeError("Введите корректное значение для поиска постов, содержащих введенную фразу")
    posts = get_posts_all(posts_path)
    query_posts = [post for post in posts if query.lower() in post["content"].lower()]
    return query_posts


def get_post_by_pk(pk, posts_path):
    if type(pk) != int:
        raise TypeError("Введите корректное значения для поиска поста по номеру")
    posts = get_posts_all(posts_path)
    pk_post = [post for post in posts if post["pk"] == int(pk)]
    return pk_post

# a = Data("./data/posts.json", "./data/comments.json")
# print(len(a.get_posts_all()))
# print(a.get_comments_by_post_id('5'))
# print(a.get_posts_by_user("leo"))
# print(a.search_for_posts("утром"))
# print(a.get_post_by_pk(2))
