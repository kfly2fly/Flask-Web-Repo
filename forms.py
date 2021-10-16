from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

# Will write python classes that will be representative of forms which will then be converted to HTML

# Want to create a registration form, so we will write a registration form class, which will be inherited from FlaskForm
# Need to do more research on classes


class RegistrationForm(FlaskForm):
    # DataRequired means that the field cannot be blank, use wtforms.validators
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    # need usernames to be between 2 and 20 characters long, so use validators
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
