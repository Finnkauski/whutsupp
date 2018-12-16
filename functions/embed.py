# -- imports
# base
import functools

# third party
import toml 
import spacy

# project
from functions.compose import compose

# -- config
config   = toml.load('config.ini')
model    = spacy.load(config['embed-spacy']['model'])

# -- definitions
def embed_(d):
    d['vector'] = model(d['clean']).vector
    
    return d
embed    = functools.partial(map, embed_) 
