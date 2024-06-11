from flask import redirect, request, render_template, abort
from app.app import app, db
from manager.models import Post, Category
from manager.forms import PostForm
from flask_login import login_required

@app.route("/forum/post/<int:post_id>")
@login_required
def post(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if not post:
        abort(404)
    return render_template("user/main/post.html", post=post)


@app.route("/category", methods=["GET", "POST"])
@login_required
def category():
    topics = Category.query.all()
    return render_template("user/main/forum.html", topics=topics)


@app.route("/forum/<int:forum_id>")
@login_required
def forum(forum_id):
    category = Category.query.get(forum_id)
    posts = Post.query.filter_by(category_id=forum_id).all()
    return render_template('user/main/all_post.html', category=category, posts=posts)