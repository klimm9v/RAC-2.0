from app.app import app, db
from werkzeug.security import generate_password_hash, check_password_hash
from flask import request, redirect, url_for, render_template, flash, session
from manager.forms import Login, RegisterForm
from user.session import login_user
from manager.models import User
from datetime import timedelta

from user.user import main



# Авторизация
@app.route("/login", methods=["GET", "POST"])
def login():
  form = Login()
  if request.method == "POST":
    if form.validate_on_submit(): 
      q = User.query.filter_by(login=form.login.data).first()
      if q:
        if check_password_hash(q.password, form.password.data):
          login_user(q)
          return redirect(url_for("main"))
        else:
          flash("Неверный password",)
      else:
        flash("Неверный login",)
    else:
      flash("Ошибка")
  return render_template("user/auth/login.html", form=form)



# Регистрация
@app.route("/", methods=["GET", "POST"])
@app.route("/register", methods=["GET", "POST"])
def register():
  form = RegisterForm()
  if request.method == "POST":
    if form.validate_on_submit():
      login = form.login.data
      password = form.password.data
      q = User.query.filter_by(login=login).first()
      if q:
        flash("Такой login существует")
        return redirect(url_for("register"))
      password_hash = generate_password_hash(password)
      new_user = User(login=login, password=password_hash)
      db.session.add(new_user)
      db.session.commit()
      login_user(new_user)
      session.permanent = True
      return redirect(url_for("main"))
  return render_template("user/auth/register.html", form=form)