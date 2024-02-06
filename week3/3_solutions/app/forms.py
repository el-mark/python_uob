from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DateField, EmailField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo

class SignUpForm(FlaskForm):
    user_name = StringField(
        'User Name:', validators=[DataRequired(message='Please enter your Name')]
    )
    email = EmailField(
        'Email Address:', validators=[DataRequired(message='Please enter an email'), Email("Enter a valid address")]
    )
    password = PasswordField(
        'Password:', validators=[DataRequired(message='Please enter a password')]
    )
    confirm_password = PasswordField(
        'Confirm Password:', validators=[DataRequired(message='Please confirm your password'), EqualTo('password', message='Passwords must match')]
    )

    date_of_birth = DateField(
        'date_of_birth:', validators=[DataRequired(message='Please enter your Date of birth')]
    )
    telephone = StringField(
        'Telephone:', validators=[DataRequired(message='Please enter your Telephone')]
    )
    address = StringField(
        'Address:', validators=[DataRequired(message='Please enter your Address')]
    )
    height = IntegerField(
        'height:', validators=[DataRequired(message='Please enter your height')]
    )
    width = IntegerField(
        'Width:', validators=[DataRequired(message='Please enter your Width')]
    )

    submit = SubmitField('Save', validators=[DataRequired()])
