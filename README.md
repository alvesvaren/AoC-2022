# AoC 2022

This is my solutions for AoC 2022

## Initialize:

When cd:ed into this repo, run;

```bash
$ python -m aoc
```

This will ask you for your session cookie (which can be found in the application tab in most browsers devtools when on adventofcode.com).

## Usage: 

In `1a.py`:
```python
from aoc import get_input

data = get_input(1).splitlines()

for line in data:
    print(line)

```

