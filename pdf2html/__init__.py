'''
Application entry point
'''

import os
from flask import Flask

from . import index


def create_app(test_config=None):
    '''
    Application factory
    '''
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(index.bp)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'pdf2html.sqlite')
    )

    if test_config is not None:
        app.config.from_mapping(test_config)
    else:
        app.config.from_pyfile('config.py', silent=True)

    os.makedirs(app.instance_path, exist_ok=True)

    return app
