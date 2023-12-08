#!/usr/bin/env python3

import regex as re
import json

# day 4 - part 1
'''                                                          1,  2,  4,  8  -> score: 8
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53 -> winners: 48, 83, 86, 17 -> score: 8 (current line winners)
                                                                            -> og_matches: 4

                                                             1,  2          -> score: 2
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19 -> winners: 32, 61         -> score: 2
                                                                            -> og_matches: 2
                                                                            

                                                             1, 2           -> score: 2
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1 -> winners: 1, 21,         -> score: 2
                                                                            -> og_matches: 2

                                                             1              -> score: 1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83 -> winners: 84,            -> score: 1
                                                                            -> og_matches: 1


Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36 -> winners: x              -> score: 0
                                                                            -> og_matches: 0


Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11 -> winners: x              -> score: 0
                                                                            -> og_matches: 0
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
print(sample_input)

# for processing full solution! use test data until ready for this part
##with open('puzzle-input.txt', 'r') as f:
##    puzzle_data = [line.strip() for line in f.readlines()]

def calculate_score(num_winners):
    # to prevent calculate_score(0) returning .5
    if num_winners >= 1:
        score = 1 * (2 ** (num_winners - 1))
    else:
        score = 0
    return score

def add_copies(start, num_winners):
    # example for card 1
    # length of winners list: 4
    # where to start: 1 (game number)
    # how many games to add copies to: 4 (length of winners list)
    # start=1, num_winners=4

    pass

# list of game objects
games = []

# loop through every line of the input,
# then append the score for that line
game_scores = []

for line in puzzle_data:
    # for every line, create a list of numbers that were winners
    # this means that the number was present in the 'winning_numbers' AND the 'numbers_i_have' lists
    current_line_winners = []
    
    game_number = line.split(':')[0]
    game_number = int(re.search(r'\d+', game_number).group(0))
    
    # create a copy number tracker for each game/line in the puzzle input
    
    # splits the game/line at the ':' to strip off the game number information
    full_game_data = line.split(':')[1]

    winning_numbers = full_game_data.split('|')[0].strip()
    winning_number_list = re.findall(r'(\d+)', winning_numbers)
    
    numbers_i_have = full_game_data.split('|')[1].strip()
    numbers_i_have_list = re.findall(r'(\d+)', numbers_i_have)
    
    for number in winning_number_list:
    
        if number in numbers_i_have_list:
            #print(f"winner found in line {game_number}: {number}")
            current_line_winners.append(int(number))
    
    current_line_score = calculate_score(len(current_line_winners))

    # print(f"Winners for line {game_number}: {current_line_winners}")
    # print(f"\tog_matches on line {game_number}: {len(current_line_winners)}")
    # print(f"\tscore for line {game_number}: {current_line_score}")
    
    game_scores.append(current_line_score)
    games.append({
        'id': game_number,
        'score': current_line_score,
        'matches': len(current_line_winners),
        'copies': 1
    })

#print(f"final list of game scores: {game_scores}")
#print(f"Part 1: total score: {sum(game_scores)}")

################ part 2 ################

# since the puzzle is asking us for how MANY cards,
copies = []

print("original card list:")
for game_offset, game in enumerate(games):
    print(game_number, ':', game)
    
    copies.append(game) # this should execute every time on the first iteration
    

    for x in range(game['matches']):
        # LEFT OFF HERE
        pass

# this is the list of all copies
# the length will end up being the solution to the puzzle
print("Final copies list:")
print(f"total copies: {len(copies)}")
for copy in copies:
    print(copy)