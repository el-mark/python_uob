from app import app, db
from flask import render_template, redirect, url_for, flash
from app.forms import RegistrationForm
from app.models import Student

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

        db.session.rollback()
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

