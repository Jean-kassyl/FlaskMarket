from flask_wtf import FlaskForm
from wtforms import StringField,EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email, Length


class RegisterForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired(), Length(min=3, max=12)])
    email = EmailField(label="Email", validators=[DataRequired(), Email()])
    password1 = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    password2 = PasswordField(label='Confirm password',validators=[DataRequired(), EqualTo('password1')])
    submit = SubmitField(label='Create account') 
