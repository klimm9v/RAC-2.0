from flask import redirect, request, render_template, abort, Response
from app.app import app, db
from manager.models import Post, Category
from manager.forms import PostForm
from flask_login import login_required
from sqlalchemy import desc



@app.route("/forum/post/<int:post_id>")
@login_required
def post(post_id: int) -> Response:
    post = Post.query.filter_by(id=post_id).first()
    if not post:
        abort(404)
    user = post.author
    return render_template("user/main/post.html", user=user, post=post)



@app.route("/category", methods=["GET", "POST"])
@login_required
def category() -> Response: 
    topics = Category.query.all()
    return render_template("user/main/forum.html", topics=topics)



@app.route("/forum/<int:forum_id>", methods=["GET", "POST"])
@login_required
def forum(forum_id: int) -> Response:
    category = Category.query.get(forum_id)
    posts = Post.query.filter_by(category_id=forum_id).order_by(desc(Post.id)).all()
    return render_template('user/main/all_post.html', category=category, posts=posts)