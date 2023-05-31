from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

class RegistrationForm(FlaskForm):
    name = StringField('Имя: ', validators=[DataRequired()])
    surname = StringField('Фамилия: ', validators=[DataRequired()])
    email = StringField('Почта: ', validators=[DataRequired()])
    password = PasswordField('Пароль: ', validators=[DataRequired()])
    confirm_password = PasswordField('Подтвердите пароль: ', validators=[DataRequired()])
    submit = submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    email = StringField('Почта: ', validators=[DataRequired()])
    password = PasswordField('Пароль: ', validators=[DataRequired()])

class UploadMusic(FlaskForm):
    pass

class SetNewPasswd(FlaskForm):
    pass
