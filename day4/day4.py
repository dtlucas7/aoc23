#!/usr/bin/env python3

import regex as re

# day 3 - part 1
'''                                                          1,  2,  4,  8  -> score: 8
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53 -> winners: 48, 83, 86, 17 -> score: 8 (current line winners)

                                                             1,  2          -> score: 2
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19 -> winners: 32, 61         -> score: 2

                                                             1, 2           -> score: 2
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1 -> winners: 1, 21,         -> score: 2

                                                             1              -> score: 1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83 -> winners: 84,            -> score: 1

Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36 -> winners: x              -> score: 0

Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11 -> winners: x              -> score: 0

winning_
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

with open('puzzle-input.txt', 'r') as f:
    puzzle_data = [line.strip() for line in f.readlines()]

# strip the whitespace from the sample data (since it's a string instead of a file input) -> strip()
# then put it into a list -> splitlines()
# puzzle_data = sample_input.strip().splitlines()

def calculate_score(num_winners):
    # to prevent calculate_score(0) returning .5
    if num_winners >= 1:
        score = 1 * (2 ** (num_winners - 1))
    else:
        score = 0
    return score

# loop through every line of the input,
# then append the score for that line 
game_scores = []

for line in puzzle_data:
    # for every line, create a list of numbers that were winners
    # this means that the number was present in the 'winning_numbers' AND the 'numbers_i_have' lists
    current_line_winners = []

    game_number = line.split(':')[0].split(' ')[1]
    # splits the game/line at the ':' to strip off the game number information
    full_game_data = line.split(':')[1]

    winning_numbers = full_game_data.split('|')[0].strip()
    winning_number_list = re.findall(r'(\d+)', winning_numbers)
    
    numbers_i_have = full_game_data.split('|')[1].strip()
    numbers_i_have_list = re.findall(r'(\d+)', numbers_i_have)
    
    for number in winning_number_list:
    
        if number in numbers_i_have_list:
            current_line_winners.append(int(number))
            #print(f"winner found in line {game_number}: {number}")
    
    print(current_line_winners)

    current_line_score = calculate_score(len(current_line_winners))
    
    print(f"score for line {game_number}: {current_line_score}")
    
    game_scores.append(current_line_score)

print(f"total score: {sum(game_scores)}")