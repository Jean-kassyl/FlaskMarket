from flask_wtf import FlaskForm
from wtforms import StringField,EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email, Length, ValidationError
from market.models import Users


class RegisterForm(FlaskForm):
    def validate_username(self, field):
        user = Users.query.filter_by(username=field.data).first()

        if user:
            raise ValidationError('the username is already taken, please choose a different username')



    username = StringField(label='Username', validators=[DataRequired(), Length(min=3, max=12)])
    email = EmailField(label="Email", validators=[DataRequired(), Email()])
    password1 = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    password2 = PasswordField(label='Confirm password',validators=[DataRequired(), EqualTo('password1')])
    submit = SubmitField(label='Create account') 
