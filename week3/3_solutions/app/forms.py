from datetime import date, timedelta
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DateField, EmailField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, NumberRange, ValidationError

class QualifyFrom(FlaskForm):
    subjects = [
        ('1', 'Math'),
        ('2', 'Biology'),
        ('3', 'History')
    ]
    first_subject = SelectField('First Subject', choices=subjects)
    second_subject = SelectField('Second Subject', choices=subjects)
    third_subject = SelectField('Third Subject', choices=subjects)

    grades = [
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C')
    ]
    first_grade = SelectField('Third Grade', choices=grades)
    second_grade = SelectField('Second Grade', choices=grades)
    third_grade = SelectField('Third Grade', choices=grades)

    submit = SubmitField('Check', validators=[DataRequired()])

class SignUpForm(FlaskForm):
    def check_date_of_birth(form, field):
        print(field.data)
        today_date = date.today()
        print(today_date)
        date_100_years_ago = today_date - timedelta(days=365 * 100)
        if field.data > today_date:
            raise ValidationError('The Date of birth must be a past date')
        
        if field.data < date_100_years_ago:
            raise ValidationError('The Date of birth must be less than 100 years ago')

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
        'date_of_birth:', validators=[DataRequired(message='Please enter your Date of birth'), check_date_of_birth]
    )
    telephone = StringField(
        'Telephone:', validators=[DataRequired(message='Please enter your Telephone')]
    )
    address = StringField(
        'Address:', validators=[DataRequired(message='Please enter your Address')]
    )
    height = IntegerField(
        'Height (cm):', validators=[DataRequired(message='Please enter your height'), NumberRange(min=90, max=300, message='Height must be between %(min)d and %(max)d centimeters')]
    )
    width = IntegerField(
        'Width (cm):', validators=[DataRequired(message='Please enter your Width')]
    )

    submit = SubmitField('Save', validators=[DataRequired()])
