# -- imports
# base
import functools
import itertools
import re

# third party 
import toml
import spacy

from pandas import DataFrame

# project
from functions import compose, parse, clean, convert, embed

# -- parse
with open('data/text.txt', 'r') as f:
    lines = f.readlines()

config = toml.load('config.ini')

pipe = compose(DataFrame, list, embed, convert, clean, parse)
l = pipe(lines)



