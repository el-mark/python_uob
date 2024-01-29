from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class SearchForm(FlaskForm):
    search = StringField('Text to search:')
    submit = SubmitField('Search')
