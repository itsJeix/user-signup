from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, InputRequired, EqualTo, Email, Regexp, Length

class LoginForm(Form):
    username = StringField('username', validators=[DataRequired(), Regexp('^\w+$', message="Invalid Characters")])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=5, message="Password is too short"), EqualTo('confirm', message='Passwords need to match')])
    confirm = PasswordField('Repeat Password')
    email = StringField('email', validators=[DataRequired(), Email(message='Use a valid email')])
