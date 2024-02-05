from app import app
from flask import render_template

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
