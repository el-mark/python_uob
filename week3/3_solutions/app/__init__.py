from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY']= b'rty%#$ui56789'

from app import views
