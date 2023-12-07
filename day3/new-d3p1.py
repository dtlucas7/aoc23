#!/usr/bin/env python3

import regex as re

with open('puzzle-input.txt') as file:
    puzzle_input = [line.strip() for line in file]

# find the numbers on each line
for line_number, line in enumerate(puzzle_input, start=1):

    numbers_found = re.findall(r'\d+', line)
    special_characters = re.findall(r'[^A-Za-z0-9 \s \. \n]', line)
    
    print(f"numbers on line {line_number}: {numbers_found}")