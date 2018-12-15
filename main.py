# -- imports
# base
import functools
import regex as re

# third party 
import toml

from numpy import array

# project
from functions import compose, parse, clean

# -- parse
with open('data/text.txt', 'r') as f:
    lines = f.readlines()

config = toml.load('config.ini')

pipe = compose(array, list, clean, parse)
l = pipe(lines)

