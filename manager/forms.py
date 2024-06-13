from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, SelectField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo

# форма авторизации
class Login(FlaskForm):
    login = StringField("Login: ")
    password = PasswordField("Password: ", validators=[DataRequired(), Length(min=4, max=100, message="Неверный пароль")])
    submit = SubmitField("Войти")

# форма регистрации
class RegisterForm(FlaskForm):
    login = StringField("Login: ")
    password = PasswordField("Password: ", validators=[DataRequired(), Length(min=4, max=100, message="Неверный формат")])
    password_repeat = PasswordField("Password: ", validators=[DataRequired(), EqualTo("password", message="Пароли не совпадают")])
    submit = SubmitField("Войти")

# опции
options = [
    ('Хакерство'),
    ('Безопасность'),
    ('Вещества'),
]

# форма поста
class PostForm(FlaskForm):
    title = StringField("Заголовок", validators=[DataRequired()])
    text = TextAreaField("Текст", validators=[DataRequired()])
    select_option = SelectField('Тема', choices=options, validators=[DataRequired()]) # Добавляем валидатор DataRequired()
    submit = SubmitField("Опубликовать")

# Шифрование
class EncryptForm(FlaskForm):
    message = TextAreaField('Сообщение для шифрования', validators=[DataRequired(), Length(min=5, max=1000)])
    key = StringField('Ключ', validators=[DataRequired(), Length(min=4, max=32)])
    submit = SubmitField('Зашифровать')

# дешифрование
class DecryptForm(FlaskForm):
    message = TextAreaField('Сообщение для дешифрования', validators=[DataRequired(), Length(min=5, max=1000)])
    key = StringField('Ключ', validators=[DataRequired(), Length(min=4, max=32)])
    submit = SubmitField('Расшифровать')