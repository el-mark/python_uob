from flask import render_template, redirect, url_for, flash
from app import app, db
from datetime import datetime
from app.forms import LoginForm, RegistrationForm, AddStudentForm, BorrowForm
from app.models import Student, Loan
from app.variable_a import VariableA, variable_b
from app.calculator import addition, subtraction
from app.calculator.multiplication import mul
# import app.variable_a


@app.route('/')
@app.route('/index')
def index():
    variable_number = addition.add(1,1) + subtraction.sub(3,6)
    multiplication_1 = mul(3,4)
    valure_variable_b = variable_b()
    return render_template('index.html', variable_a=VariableA.value, variable_number=variable_number, multiplication_1=multiplication_1)

@app.route('/datetime')
def date_time():
    now = datetime.now()
    return render_template('datetime.html', title='Date & Time', now=now)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login for {form.username.data}', 'success')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Registration for {form.username.data} received', 'success')
        return redirect(url_for('index'))
    return render_template('registration.html', title='Register', form=form)


@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    form = AddStudentForm()
    if form.validate_on_submit():
        new_student = Student(
            username=form.username.data, firstname=form.firstname.data,                  
            lastname=form.lastname.data, email=form.email.data, age=form.age.data
        )
        db.session.add(new_student)
        try:
            db.session.commit()
            flash(f'New Student added: {form.username.data} received', 'success')
            return redirect(url_for('index'))
        except:
            db.session.rollback()
            if Student.query.filter_by(username=form.username.data).first():
                form.username.errors.append('This username is already taken. Please choose another')
            if Student.query.filter_by(email=form.email.data).first():
                form.email.errors.append('This email address is already registered. Please choose another')
    return render_template('add_student.html', title='Add Student', form=form)


@app.route('/borrow', methods=['GET', 'POST'])
def borrow():
    form = BorrowForm()
    if form.validate_on_submit():
        new_loan = Loan(device_id=form.device_id.data,
                        student_id=form.student_id.data,
                        borrowdatetime=datetime.now())

        db.session.add(new_loan)
        try:
            db.session.commit()
            flash(f'New Loan added', 'success')
            return redirect(url_for('index'))
        except:
            db.session.rollback()
    return render_template('borrow.html', title='Borrow', form=form)


