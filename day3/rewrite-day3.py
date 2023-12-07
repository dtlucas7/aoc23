#!/usr/bin/env python3

import json

# Day 3: Gear Ratios

with open('./puzzle-input.txt') as file:
    puzzle_data = [line.strip() for line in file]

# the symbols that we are looking for in the file
symbols = ['+', '@', '-', '%', '/', '*', '&', '$', '#', '=']

# create a list of dicts that contain the character and the coordinates
special_characters = []

for line_number, line_data in enumerate(puzzle_data, start=1):
    for character_number, character_data in enumerate(line_data, start=1):
        #print(f"line-{line_number}:char-{character_number} = {character_data}")
        if character_data in symbols:
            special_characters.append(
                {
                    'character': character_data,
                    'coordinates': (line_number, character_number),
                }
            )

print(json.dumps(special_characters[1], indent=2))
