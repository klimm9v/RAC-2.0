from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo

# форма авторизации
class Login(FlaskForm):
    login = StringField("Login: ")
    password = PasswordField("Password: ", validators=[DataRequired(), Length(min=4, max=100, message="Неверный пароль")])
    recaptcha = RecaptchaField()
    submit = SubmitField("Войти")

# форма регистрации
class RegisterForm(FlaskForm):
    login = StringField("Login: ")
    password = PasswordField("Password: ", validators=[DataRequired(), Length(min=4, max=100, message="Неверный формат")])
    password_repeat = PasswordField("Password: ", validators=[DataRequired(), EqualTo("password", message="Пароли не совпадают")])
    recaptcha = RecaptchaField()
    submit = SubmitField("Войти")

# форма поста
class PostForm(FlaskForm):
    title = StringField("Заголовок", validators=[DataRequired()])
    text = TextAreaField("Текст", validators=[DataRequired()])
    submit = SubmitField("Отправить")
