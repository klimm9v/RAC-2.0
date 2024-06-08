from app.app import app, db
from flask import request, abort
from flask_login import current_user, login_required
from flask import request, redirect, url_for, render_template, flash
from manager.models import Post, User
from manager.forms import PostForm
from datetime import datetime
import os



# Отображение главной страницы
@app.route("/main")
@login_required
def main():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template("user/main/etc/main.html", posts=posts)



# Отображение определенного поста
@app.route("/post/<int:post_id>")
@login_required
def post(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if not post:
        abort(404)
    return render_template("user/main/etc/post.html", post=post)


# отображение аккаунта сессии
@app.route("/account")
@login_required
def account():
    return render_template("user/main/user/me_account.html", user=current_user)


# отображение аккаунта пользователя
@app.route("/account/<string:username>", methods=["GET", "POST"])
@login_required
def get_account(username):
    user = User.query.filter_by(login=username).first()
    if not user:
        abort(404)
    if user.id == current_user.id:
       return render_template("user/main/user/me_account.html", user=user)
    return render_template("user/main/user/account.html", user=user)



# Создания поста
@app.route("/create", methods=["GET", "POST"])
@login_required
def create():
    form = PostForm()
    if request.method == "POST":
        if form.validate_on_submit():
            title = form.title.data
            text = form.text.data.replace("\n", "<br>")
            text = text.replace("<script>", "< script >")
            date_post = datetime.now()
            new_post = Post(title=title, text=text, user_id=current_user.id, date_post=date_post)
            db.session.add(new_post)
            db.session.commit()
            db.session.close()
            return redirect(url_for("create"))
    return render_template("user/main/etc/create.html", form=form)



from manager.utils import allowed_file
from werkzeug.utils import secure_filename



# обновление аватарки
@app.route('/upload_avatar', methods=['GET', 'POST'])
@login_required
def upload_avatar():
    if request.method == 'POST':
        # Проверяем, есть ли файл в запросе
        if 'avatar' not in request.files:
            flash('Нет файла')
            return redirect(url_for("account"))
        file = request.files['avatar']
        # Проверяем, выбран ли файл
        if file.filename == '':
            return redirect(url_for("account"))
        # Проверяем, разрешен ли тип файла и сохраняем его
        if file and allowed_file(file.filename):
            id = current_user.id
            filename = secure_filename(file.filename) + str(id)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            # Обновляем путь к аватару в базе данных
            current_user.avatar = filename  # Сохраняем только имя файла
            db.session.commit()  # Фиксируем изменения в базе данных
            
            return redirect(url_for('account'))
        else:
            flash('Недопустимый формат файла')
            return redirect(request.url)
    # Если GET запрос, просто отображаем форму
    return render_template("user/main/user/account.html", user=current_user)