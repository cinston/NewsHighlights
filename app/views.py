from flask import render_template
from app import app

@app.route('/')
def index():
    """
    view root page function that returns the index p0age and its data
    """
    return render_template('index.html')