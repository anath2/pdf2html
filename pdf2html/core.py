'''
Core module
'''

import random


def generate_random_url(base_url, strlen=12):

    '''
    ARGS:
        base_url: url to be extended
        length: length of the random string
    Generates a url with random letters
    '''
    alphanum = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    random_str = ''.join(alparange[random.randrange(len(alphanum))] for l in range(strlen)])
    return base_url + '/' + random_str
