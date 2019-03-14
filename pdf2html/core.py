'''
Core module
'''

import random
import time


def get_random_url(base_url):
    '''
    ARGS:
        base_url: The base url to be extended by the random string

    Returns a randomly unique string url
    '''
    random_str_len = 12

    while True:
        random_str = get_random_str(random_str_len)
        random_url = base_url + '/' + random_str
        if random_str in not in db:
            return random_url
        time.sleep(1)


def get_random_str(strlen):

    '''
    ARGS:
        strlen: length of the random string

    Generates a url with random letters
    '''
    random_str = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(strlen))
    return random_str
