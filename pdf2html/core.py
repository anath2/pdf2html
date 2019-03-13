'''
Core module
'''

import random


def generate_random_url(base_url, len=12):

    '''
    ARGS:
        base_url: url to be extended
        length: length of the random string
    Generates a url with random letters
    '''
    start = 65  # ASCII 'A'
    end = 127  # Last letter

    random_str = ''.join([chr(random.randrange(start, end)) for l in range(len)])
    return base_url + '/' + random_str
