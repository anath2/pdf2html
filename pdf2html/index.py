'''
Application entry point
'''

import functools
from flask import render_template, Blueprint


bp = Blueprint('pdf2html', __name__)


@bp.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')
