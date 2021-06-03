from flask import Blueprint, render_template

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/about')
def about():
    return '<h1>Starter code for the assessment<h1>'

@bp.route('/contact')
def contact():
    return '<h1>Starter code for the assessment<h1>'
