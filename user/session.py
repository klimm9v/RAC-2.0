from flask_login import login_user, login_manager, logout_user, current_user, login_required
from manager.models import User
from app.app import app, db, ALLOWED_EXTENSIONS
from flask import redirect, url_for, request, flash, session
from manager.forms import Login
from manager.models import User
from app.app import login_manager
import os
from datetime import datetime

# Работа с сессией

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



@app.errorhandler(404)
def error404(e):
    return "Error 404"

@app.errorhandler(401)
def error401(e):
    return 'Error 401'

@app.errorhandler(403)
def error404(e):
    return 'Error 403'