#!/usr/bin/env python
# -- imports
# base
import functools

from datetime import datetime as dt

# third party
import spacy

# project
from functions.compose import compose

# -- definitions
def convert_(d):
    d['datetime'] = dt.strptime(f'{d["date"]} {d["time"]}', '%d/%m/%Y %H:%M')
    return d 
convert = functools.partial(map, convert_)
