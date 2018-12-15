# -- imports
# base
import re
import functools

# third party
import toml 

# project
from functions.compose import compose

# config 
config        = toml.load('config.ini')
match_pattern = config['format']['regex']

# -- definitions 
# -- do a check for which entries comform to a pattern 
match = functools.partial(re.match, match_pattern)
check = functools.partial(filter, match)

# -- search for groups that we parse out
search_  = lambda s: re.search(pattern=config['parse']['regex'], string=s).groups()
search   = functools.partial(map, search_)

parse = compose(search, check)
