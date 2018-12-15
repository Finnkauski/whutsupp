# -- imports
# base
import re
import functools

# third party
import toml 

# project
from functions.compose import compose

# -- config 
config         = toml.load('config.ini')
match_pattern  = config['format']['match']
remove_pattern = config['format']['remove']

# -- definitions 
# -- do a check for which entries comform to a pattern 
match = functools.partial(re.match, match_pattern)
check = functools.partial(filter, match)

# -- remove messages containing specific text
checkin = lambda val, s: s not in val 
tests   = map(lambda s: functools.partial(filter, functools.partial(checkin, s=s)), remove_pattern)
remove  = compose(*tests)

# -- search for groups that we parse out
search_  = lambda s: re.search(pattern=config['parse']['regex'], string=s).groups()
search   = functools.partial(map, search_)

# -- rowParse to correct types
# TODO: parse rows into correct types needs implementing

parse = compose(search, remove, check)
