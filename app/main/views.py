from flask import render_template
from . import main
from ..request import get_sources, get_articles

#Index route and view function
@main.route('/')
def index():
    """
    View root page function that returns the index page and it's content
    """
    title  = "News Centre. "
    heading = "Welcome our Trusted news sources you can select one in your category to read through what they have for you"

    #Getting the sources
    general = get_sources('general')
    sports = get_sources('sports')
    business = get_sources('business')
    entertainment = get_sources('entertainment')
    science = get_sources('science')

    return render_template('index.html', title=title, heading=heading, general = general, sports = sports, business = business, entertainment = entertainment, science = science)
