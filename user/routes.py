from app.app import app
from flask_login import current_user
from flask import redirect, url_for

@app.route('/')
def index():
  if not current_user.is_authenticated:
    return redirect(url_for("login"))
  else:
    return redirect(url_for("main"))