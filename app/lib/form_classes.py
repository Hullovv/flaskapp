from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, FileField
from wtforms.validators import DataRequired, Email, EqualTo

class RegistrationForm(FlaskForm):
    name = StringField('Имя: ', validators=[DataRequired()])
    surname = StringField('Фамилия: ', validators=[DataRequired()])
    email = StringField('Почта: ', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль: ', validators=[DataRequired()])
    confirm_password = PasswordField('Подтвердите пароль: ', validators=[DataRequired(), EqualTo('password')])
    reg_submit = SubmitField('Заругестрироваться')

class LoginForm(FlaskForm):
    email = StringField('Почта: ', validators=[DataRequired()])
    password = PasswordField('Пароль: ', validators=[DataRequired()])
    log_submit = SubmitField('Войти')

class UploadMusic(FlaskForm):
    music_field = FileField('Выбрать файл')
    mus_submit = SubmitField('Загрузить')

class SetNewPasswd(FlaskForm):
    pass
