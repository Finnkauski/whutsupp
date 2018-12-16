# -- imports
# base
import functools
import re

# third party 
import toml

from numpy import array

# project
from functions import compose, parse, clean
from woffle.woffle.embed.numeric.spacy.embed import embed

# -- parse
with open('data/text.txt', 'r') as f:
    lines = f.readlines()

config = toml.load('config.ini')

pipe = compose(array, list, clean, parse)
l = pipe(lines)
