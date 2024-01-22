from flask import Flask, request
import datetime
import random

def get_quotes_array():
    quotes_file = open('quotes.txt', 'r')
    quotes = []
    for line in quotes_file:
        quotes.append(line)
    return quotes

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/now')
def date_time():
    date_and_time = datetime.datetime.now()

    return date_and_time.strftime("%c")

@app.route('/random_quote')
def random_quote():
    quotes = get_quotes_array()
    return quotes[random.randrange(1, len(quotes))]

@app.route('/quote/<number>')
def quote(number):
    quotes = get_quotes_array()
    return quotes[int(number)]
