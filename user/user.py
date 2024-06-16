from app.app import app, db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask import request, redirect, url_for, render_template, flash, make_response, abort
from manager.forms import Login, RegisterForm, PostForm, CreateLetter
from manager.models import User, Category, Post
from flask_login import login_user, logout_user, login_required, current_user
import datetime, os
from datetime import datetime

@app.route("/main")
@login_required
def main():
    return render_template("user/main/main.html")
  
  
@app.route("/yashik", methods=["GET", "POST"])
@login_required
def yashik():
  form = CreateLetter()
  return render_template("user/main/yashik.html", form=form)
  
  
# отображение аккаунта сессии
@app.route("/account")
@login_required
def account():
    return render_template("user/main/me_account.html", user=current_user)



# отображение аккаунта пользователя
@app.route("/account/<string:username>", methods=["GET", "POST"])
@login_required
def get_account(username):
    user = User.query.filter_by(login=username).first()
    if not user:
        abort(404)
    if user.id == current_user.id:
       return render_template("user/main/me_account.html", user=user)
    return render_template("user/main/account.html", user=user)



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
            category_id = form.select_option.data
            category = Category.query.filter_by(name=category_id).first()
            new_post = Post(title=title, text=text, user_id=current_user.id, date_post=date_post, category_id=category.id)
            db.session.add(new_post)
            db.session.commit()
            db.session.close()
            return redirect(url_for("create"))
    return render_template("user/main/create.html", form=form)


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
    return render_template("user/main/account.html", user=current_user)


@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))


@app.route("/logout")
def logout():
  user_id = current_user.id
  user = User.query.get(user_id)
  user.last_online = datetime.now()
  db.session.commit()
  logout_user()
  return redirect(url_for("login"))


from user.routes import index


# Авторизация
@app.route("/login", methods=["GET", "POST"])
def login():
  form = Login()
  if request.method == "POST":
    if form.validate_on_submit(): 
      q = User.query.filter_by(login=form.login.data).first()
      if q and check_password_hash(q.password, form.password.data):
          login_user(q)
          return redirect(url_for("main"))
      else:
        flash("ошибка пароля или такого пользователя не существует.",)
    else:
      flash("Ошибка.")
  return render_template("user/auth/login.html", form=form)


from manager.utils import generate_random


# Регистрация
@app.route("/register", methods=["GET", "POST"])
def register():
  form = RegisterForm()
  if request.method == "POST":
    if form.validate_on_submit():
      login = form.login.data.lower()
      password = form.password.data
      q = User.query.filter_by(login=login).first()
      if q:
        flash("Такой login существует")
        return redirect(url_for("register"))
      password_hash = generate_password_hash(password)
      new_user = User(login=login, password=password_hash)
      db.session.add(new_user)
      db.session.commit()
      code = str(new_user.id) + new_user.login[:3] + str(generate_random())
      new_user.code = code
      db.session.commit()
      login_user(new_user)
      return redirect(url_for("main"))
  return render_template("user/auth/register.html", form=form)