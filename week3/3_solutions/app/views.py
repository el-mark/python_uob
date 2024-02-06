from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import SignUpForm

with app.open_resource('data/quotes.txt') as file:
    quotes = []
    for line in file:
        quotes.append(line.decode("utf-8"))
    app.globals_quotes = quotes


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/cs_qualify/<grades_raw>')
def cs_qualify(grades_raw):
    qualification = 'Approved'

    grades =  grades_raw.split(',')
    counter = 0
    for grade in grades:
        if grade == 'a':
            counter += 1
    
    if counter == 3:
        qualification = 'Approved'
    else:
        qualification = 'Not Approved'

    return render_template('cs_qualify.html', title='Qualification', qualification=qualification, grades=grades)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = SignUpForm()
    if form.validate_on_submit():
        flash(f'{form.user_name.data} your registration was successful!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)
