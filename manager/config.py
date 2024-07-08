from app.app import app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_session import Session
import os
from datetime import timedelta



# конфиг
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
app.permanent_session_lifetime = timedelta(days=1)
app.config['SECRET_KEY'] = '12345'  # Замените на уникальную строку
UPLOAD_FOLDER = os.path.join('app', 'static', 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', "webp",}
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=10)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CSRF_ENABLED = True
app.config['RECAPTCHA_PUBLIC_KEY'] = '6Le1iOMpAAAAAEgs1Qq6VvkuGsUim5NMhJzT5mkS'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6Le1iOMpAAAAAEHs_tumXMC9uIHAuDOYHpgot_4V'