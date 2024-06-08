from app.app import app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os

# конфиг
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admin.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
app.secret_key = '12345'
login_manager.init_app(app)
UPLOAD_FOLDER = os.path.join('app', 'static', 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', "webp",}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CSRF_ENABLED = True
app.config['RECAPTCHA_PUBLIC_KEY'] = '6Le1iOMpAAAAAEgs1Qq6VvkuGsUim5NMhJzT5mkS'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6Le1iOMpAAAAAEHs_tumXMC9uIHAuDOYHpgot_4V'