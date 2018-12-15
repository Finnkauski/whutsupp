# -- imports
# base
import functools
import regex as re

# third party 
import toml

# project
from functions.compose import compose
from functions.parse   import parse 


# -- parse
with open('data/text.txt', 'r') as f:
    lines = f.readlines()

    config = toml.load('config.ini')
    
l = list(parse(lines))


