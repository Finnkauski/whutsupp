# WhutsUpp 
A simple set of tools for WhatsApp text analysis with complex ambitions.
Its a work in progress. Not documented, tested or CI'd

## Usage

``` python
# -- imports
# base

# third party 
import toml

# project
from functions.parse   import parse 


# -- parse
with open('data/text.txt', 'r') as f:
    lines = f.readlines()

    config = toml.load('config.ini')
    
l = parse(lines)
```
