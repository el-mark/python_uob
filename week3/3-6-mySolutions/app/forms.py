from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SearchEventFrom(FlaskForm):
    title_of_event = StringField(
        'Title of event:', validators=[DataRequired(message='Please enter an Event Title')]
    )
    submit = SubmitField('Save', validators=[DataRequired()])
