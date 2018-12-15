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
letters  = lambda s: re.sub('[^A-z ]', '', s)

clean_   = compose(str.lower, letters)
clean    = lambda iterable: map(lambda row: list(row) + [clean_(row[3])], iterable)

