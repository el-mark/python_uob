from app import app, db
from flask import render_template, redirect, url_for, flash
from app.forms import RegistrationForm, BorrowForm, ReturnDeviceForm
from app.models import Student, Loan
from datetime import datetime

with app.open_resource('data/quotes.txt') as file:
    quotes = []
    for line in file:
        quotes.append(line.decode("utf-8"))
    app.globals_quotes = quotes

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/template_a')
def template_a():
    variable_a = 'Variable A'
    return render_template('template_a.html', title='Template A', variable_a=variable_a, quotes=app.globals_quotes)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():

        new_student = Student(
            firstname=form.firstname.data, lastname=form.lastname.data,
            email=form.email.data
        )

        # if Student.query.filter_by(username=form.username.data).first():
        #     form.username.errors.append('This username is already taken. Please choose another')
        if Student.query.filter_by(email=form.email.data).first():
            form.email.errors.append('This email address is already registered. Please choose another')

        if not form.email.errors:
            db.session.add(new_student)
            db.session.commit()
            flash(f'New Student added: {form.email.data} received', 'success')
            return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)

@app.route('/borrow', methods=['GET', 'POST'])
def borrow():
    form = BorrowForm()
    if form.validate_on_submit():

        new_loan = Loan(
            student_id=form.student_id.data, device_id=form.device_id.data,
            borrow_datetime=datetime.now()
        )

        if not Student.query.filter_by(student_id=form.student_id.data).first():
            form.student_id.errors.append('This student is not registered')

        if Loan.query.filter(Loan.student_id == form.student_id.data, Loan.return_datetime == None).first():
            form.student_id.errors.append('This student has a borrowed item already')

        if Loan.query.filter(Loan.device_id == form.device_id.data, Loan.return_datetime == None).first():
            form.device_id.errors.append('This device has not been returned yet')

        if not form.student_id.errors and not form.device_id.errors:
            db.session.add(new_loan)
            db.session.commit()
            flash(f'New Loan added for student with id: {form.student_id.data}', 'success')
            return redirect(url_for('home'))

    return render_template('borrow.html', title='Borrow', form=form)

@app.route('/return_device', methods=['GET', 'POST'])
def return_device():
    form = ReturnDeviceForm()
    if form.validate_on_submit():

        loan = Loan.query.filter(
            Loan.device_id == form.device_id.data, Loan.return_datetime == None
        ).first()

        if not Loan.query.filter_by(device_id=form.device_id.data).first():
            form.device_id.errors.append('The device does not exist')
        elif not loan:
            form.device_id.errors.append('The device is already returned')

        if not form.device_id.errors:
            loan.return_datetime = datetime.now()
            db.session.commit()
            flash(f'The device with id: {form.device_id.data} was returned successfully', 'success')
            return redirect(url_for('home'))

    return render_template('return_device.html', title='Return', form=form)
