from flask import Flask, request
import datetime
import random


from math import isqrt
def is_prime(n):
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = isqrt(n)
    for i in range(5, limit+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

def prime_divisors(number):
    divisors = []
    for i in range(2, number):
        if number % i == 0 and is_prime(i):
            divisors.append(i)
    return divisors


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

@app.route('/prime/<number>')
def prime(number):
    divisors = prime_divisors(int(number))
    return str(divisors)
