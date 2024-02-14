from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import SearchEventFrom

app.globals_events = [
    {
        'title': 'Concert of Cold Play',
        'date': '23/03/2024',
        'venue': 'Arena 1'
    },
    {
        'title': 'Concert of Green Day',
        'date': '09/04/2024',
        'venue': 'Arena 1'
    },
    {
        'title': 'Exposition of Modern Art',
        'date': '01/03/2024-20/03/2024',
        'venue': 'MAC Museum'
    }
]


@app.route('/', methods=['GET', 'POST'])
def home():
    form = SearchEventFrom()
    events = None
    print(form.title_of_event.data)
    if form.validate_on_submit():
        events = []
        for event in app.globals_events:
            if event['title'].lower().find(form.title_of_event.data) >= 0:
                events.append(event)
                

    return render_template('home.html', title='Events', form=form, events=events)
