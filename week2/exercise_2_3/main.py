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

@app.route('/search/<search_text>')
def search(search_text):
    abbreviations = app.globals_abbreviations
    filtered_abbreviations = []
    for abbreviation in abbreviations:
        if len(filtered_abbreviations) > 10:
            break
        if abbreviation[0].startswith(search_text):
            filtered_abbreviations.append(abbreviation)

    return render_template('search.html', abbreviations = filtered_abbreviations)
