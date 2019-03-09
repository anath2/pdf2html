'''
Application entry point
'''

def create_app(test_config=None):
    '''
    Application factory
    '''
    app = Flask(__name__, instance_relative_config=True)
