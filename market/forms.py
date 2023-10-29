from flask_wtf import FlaskForm
from wtforms import StringField,EmailField, PasswordField, SubmitField


class RegisterForm(FlaskForm):
    username = StringField(label='username')
    email = EmailField(label="email")
    password1 = PasswordField(label='password')
    password2 = PasswordField(label='confirm password')
    submit = SubmitField(label='submit')
