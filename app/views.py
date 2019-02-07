from flask import render_template
from app import app
from .request import get_news

@app.route('/')
def index():
    """
    view root page function that returns the index page and its data
    """
    popular_news = get_news('popular')
    print(popular_news)
    
    title = 'Home - This is a news website that lists and previews news articles from various sources.'    
    return render_template('index.html', title = title)

@app.route('/news/<int:news_id>')    
def news(news_id):    
    """
    view news function that returns the movie details page and its data
    """
    return render_template('news.html',id = news_id)
