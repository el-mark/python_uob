from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
# To enable email validation,
# 1. install the email-validation package in your py312 environment,
# 2. Comment out the following import line and uncomment the next one
# 3. follow the instructions below for the email field in the RegistrationForm Class
from wtforms.validators import DataRequired, EqualTo
# from wtforms.validators import DataRequired, EqualTo, Email

class RegistrationForm(FlaskForm):
    # username = StringField('Username', validators=[DataRequired()])
    firstname = StringField('First Name')
    lastname = StringField('Last Name', validators=[DataRequired()])
    # To enable email validation, comment out the following line and uncomment the next one:
    email = StringField('Email', validators=[DataRequired()])
    
    # password = PasswordField('Password', validators=[DataRequired()])
    # confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class BorrowForm(FlaskForm):
    student_id = StringField('Student Id', validators=[DataRequired()])
    device_id = StringField('Device Id', validators=[DataRequired()])

    submit = SubmitField('Register Borrow')

class ReturnDeviceForm(FlaskForm):
    device_id = StringField('Device Id', validators=[DataRequired()])

    submit = SubmitField('Register Borrow')

class DeleteStudentForm(FlaskForm):
    student_id = StringField('Student Id', validators=[DataRequired()])

    submit = SubmitField('Delete')

class GetReportForm(FlaskForm):
    object_id = StringField('Id for search', validators=[DataRequired()])
    object_classes = [
        ('student', 'Student'),
        ('device', 'Device')
    ]
    object_class = SelectField('Choose one', choices=object_classes)

    submit = SubmitField('Search')
