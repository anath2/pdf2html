'''
Entrypoint view
'''

from flask import render_template, Blueprint, request, redirect

from . import core

bp = Blueprint('pdf2html', __name__)


@bp.route('/', methods=('GET', 'POST'))
def index():
    # Algorithm
    if request.method == 'POST':
        path = request.form['file']

        # Generate expireable random string url
        file_url = 'SOMETHING'
        redirect(file_url)

    return render_template('index.html')


@bp.route('/about', methods=('GET',))
def about():
    # Render about page
    pass
