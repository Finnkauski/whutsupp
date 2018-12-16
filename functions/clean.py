# -- imports
# base
import re
import functools

# third party
import toml 

# project
from functions.compose import compose

# -- config
config   = toml.load('config.ini')

# -- definitions
letters = lambda s: re.sub('[^A-z ]', '', s)


# -- create pipe
pipe    = compose(str.lower, letters)
def clean_(d):
    d['clean'] = pipe(d['msg'])
    return d
clean   = functools.partial(map, clean_)
