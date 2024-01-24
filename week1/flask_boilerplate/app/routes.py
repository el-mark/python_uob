from app import app
from flask import render_template

@app.route('/')
def home():
    return 'hello world'

@app.route('/template_a')
def template_a():
    variable_a = 'Variable A'
    return render_template('template_a.html', variable_a=variable_a)
