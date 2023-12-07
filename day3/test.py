import regex as re


# Regular expression pattern
pattern = "(\d+)"

test_puzzle = \
'''\
...........441
...606........
....*......116
..902.........
..............
...318.......8
....*.........
.850....269...
..........&..4
..............
..............
.....=.....964
...966.152*...
..............
862*766......@
'''

# load test_puzzle into a grid
grid = []
for line in test_puzzle.splitlines():
    grid.append(line)

for line in grid:
    print(line)
