from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo

class SignUpForm(FlaskForm):
    user_name = StringField(
        'User Name:', validators=[DataRequired(message='Please enter your Name')]
    )
    email = StringField('Email Address:', validators=[DataRequired(message='Please enter an email'), Email("Enter a valid address")])
    password = PasswordField('Password:', validators=[DataRequired(message='Please enter a password')])
    confirm_password = PasswordField('Confirm Password:', validators=[DataRequired(message='Please confirm your password'), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Save', validators=[DataRequired()])
