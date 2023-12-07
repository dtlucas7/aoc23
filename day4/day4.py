#!/usr/bin/env python3

import re

# day 3 - part 1
'''                                                          1,  2,  4,  8  -> score: 8
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53 -> winners: 48, 83, 86, 17 -> score: 8

                                                             1,  2          -> score: 2
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19 -> winners: 32, 61         -> score: 2

                                                             1, 2           -> score: 2
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1 -> winners: 1, 21,         -> score: 2

                                                             1              -> score: 1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83 -> winners: 84,            -> score: 1

Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36 -> winners: x              -> score: 0

Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11 -> winners: x              -> score: 0
'''


sample_input = \
'''
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
'''

# strip the whitespace from the sample data (since it's a string instead of a file input) -> strip()
# then put it into a list -> splitlines()
puzzle_data = sample_input.strip().splitlines()

def calculate_score(winning_cards):
    num_winners = len(winning_cards)
    score = 1 * (2 ** (num_winners - 1))
    return score

winning_cards = []

for line in puzzle_data:
    
    game_number = line.split(':')[0].split(' ')[1]
    full_game_data = line.split(':')[1]
    winning_numbers = full_game_data.split('|')[0].strip()
    winning_number_list = re.findall(r'(\d+)', winning_numbers)
    numbers_i_have = full_game_data.split('|')[1].strip()
    current_line_score = calculate_score(winning_number_list)

    print(f"current line score: {current_line_score}")


