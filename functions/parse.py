# -- imports
# base
import re
import functools

# third party
import toml 

# project
from functions.compose import compose

# -- config
# TODO: Remove reliance on named values. seems silly
config         = toml.load('config.ini')
match_pattern  = config['format']['match']
remove_pattern = config['format']['remove']
groups         = config['parse']['regex']
cols           = config['parse']['cols'] 

# -- definitions 
# -- do a check for which entries comform to a pattern 
match = functools.partial(re.match, match_pattern)
check = functools.partial(filter, match)

# -- remove messages containing specific text
checkin = lambda val, s: s not in val 
tests   = map(lambda s: functools.partial(filter, functools.partial(checkin, s=s)), remove_pattern)
remove  = compose(*tests)

# -- search for groups that we parse out
search_  = lambda s: re.search(pattern=groups, string=s).groups()
search   = functools.partial(map, search_)

# -- dictize
dictize_ = lambda row: dict(zip(cols,row)) 
dictize  = functools.partial(map, dictize_)

# -- rowParse to correct types
# TODO: parse rows into correct types needs implementing

parse = compose(dictize, search, remove, check)
