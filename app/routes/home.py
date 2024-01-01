from flask import Blueprint, render_template

Home = Blueprint('home', __name__)


@Home.route('/')
def index():
    """
    principal page app
    """
    data = {
        'title': "Bio D"
    }
    return render_template('index.html', data=data)
