from flask import Flask, render_template

app = Flask(__name__)

with app.open_resource('data/en-abbreviations.txt') as file:
    abbreviations = []
    for line in file:
        line_string = line.decode("utf-8")
        if not line_string.startswith("#"):
            abbreviations.append(line_string.split("\t"))

    app.globals_abbreviations = abbreviations


@app.route('/')
def home():
    return 'home'

@app.route('/header')
def header():
    return render_template('header.html', abbreviations=app.globals_abbreviations[0:10])
