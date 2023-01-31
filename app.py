import logging
import utils
from flask import Flask, render_template, request, jsonify

POSTS_PATH = "./data/posts.json"
COMMENTS_PATH = "./data/comments.json"
# Создание экземпляра Flask с указанием папки, из которой будем брать шаблоны
app = Flask(__name__, template_folder="templates")
app.config['JSON_AS_ASCII'] = False


# Создание представления основной страницы со всеми постами
@app.route("/")
def main_page():
    posts = utils.get_posts_all(POSTS_PATH)
    return render_template("index.html", posts=posts)


# Создание представления поста с указанным id
@app.route("/posts/<int:postid>")
def post_page(postid):
    id_post = utils.get_post_by_pk(postid, POSTS_PATH)
    comments = utils.get_comments_by_post_id(postid, POSTS_PATH, COMMENTS_PATH)
    len_comments = len(comments)
    return render_template("post.html", id_post=id_post, comments=comments, len_comments=len_comments)


# Создание представления страницы со всеми постами определенного пользователя
@app.route("/users/<username>")
def user_posts(username):
    posts = utils.get_posts_by_user(username, POSTS_PATH, COMMENTS_PATH)
    return render_template("user-feed.html", posts=posts, username=username)


# Создание представления страницы с постами, содержащими ввод пользователя в поисковой строке
@app.route("/search")
def search_page():
    user_input = str(request.args.get('s'))
    posts = utils.search_for_posts(user_input, POSTS_PATH)
    posts_count = len(posts)
    return render_template("search.html", posts=posts, posts_count=posts_count)


@app.route("/api/posts")
def get_join_posts():
    logging.basicConfig(filename="./log/api.log", level=logging.INFO, filemode="w", datefmt="%d-%b-%y %H:%M:%S",
                        encoding="utf", format="[%(asctime)s] [%(levelname)s]Запрос %(message)s")
    logging.info("Запущена страница со всеми постами в формате JSON")
    posts = utils.get_posts_all(POSTS_PATH)
    return jsonify(posts)


@app.route("/api/posts/<int:post_id>")
def get_join_post(post_id):
    logging.basicConfig(filename="./log/api.log", level=logging.INFO, filemode="w", datefmt="%d-%b-%y %H:%M:%S",
                        encoding="utf", format="[%(asctime)s] [%(levelname)s]Запрос %(message)s")
    logging.info(f"Запущена страница постa c номером {post_id} в формате JSON")
    post = utils.get_post_by_pk(post_id, POSTS_PATH)
    return jsonify(post)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1>"


@app.errorhandler(500)
def page_server_error(e):
    return "<h1>500</h1>"


if __name__ == "__main__":
    app.run()
