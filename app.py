from flask import Flask, render_template, request
from utils import Data


# Создание экземпляра Flask с указанием папки, из которой будем брать шаблоны
app = Flask(__name__, template_folder="templates")
# Создание экземпляра класса с функциями
data = Data("./data/posts.json", "./data/comments.json")


# Создание представления основной страницы со всеми постами
@app.route("/")
def main_page():
    posts = data.get_posts_all()
    return render_template("index.html", posts=posts)


# Создание представления поста с указанным id
@app.route("/posts/<postid>")
def post_page(postid):
    id_post = data.get_post_by_pk(postid)
    comments = data.get_comments_by_post_id(postid)
    len_comments = len(comments)
    return render_template("post.html", id_post=id_post, comments=comments, len_comments=len_comments)


# Создание представления страницы со всеми постами определенного пользователя
@app.route("/users/<username>")
def user_posts(username):
    posts = data.get_posts_by_user(username)
    return render_template("user-feed.html", posts=posts, username=username)


# Создание представления страницы с постами, содержащими ввод пользователя в поисковой строке
@app.route("/search")
def search_page():
    user_input = str(request.args.get('s'))
    posts = data.search_for_posts(user_input)
    posts_count = len(posts)
    return render_template("search.html", posts=posts, posts_count=posts_count)


app.run()
