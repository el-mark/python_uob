from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import RegistrationForm

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
        flash(f'Registration for {form.username.data} successful', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)
