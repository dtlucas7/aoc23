import regex as re
import json

with open('./puzzle-input-day2.txt') as file:
    puzzle_data = [line.strip() for line in file]

RED_MAX     = 12
GREEN_MAX   = 13
BLUE_MAX    = 14

# list of game objects
games = []

# list of IDs of games that are possible
possible_game_ids = []

def game_is_possible(game):
    print(f"total rolls in game {game['game_id']}: {len(game['rolls'])}")
    for roll in game['rolls']:
        print(roll)

def get_game_id(game):
    game_id = int(str(game.split(':')).split(' ')[1].strip('\','))
    return game_id

def get_game_rolls(game):
    # one "roll" will have all of the following fields
    roll_object = {
        'red':      int,
        'green':    int,
        'blue':     int
    }
    # rolls for a single game
    rolls = []

    # everything to the right of the colon represents a single game
    game_data = game.split(':')[1].strip()

    # splits the data to the right of the colon
    # each item is a roll
    rolls_original = game_data.split(';')

    # iterate through each "roll" string and put result in a proper dict
    # sample "roll" string: 6 blue, 7 red, 11 green
    for roll in rolls_original:

        red_search = re.search(r'(\d+) red', roll)
        green_search = re.search(r'(\d+) green', roll)
        blue_search = re.search(r'(\d+) blue', roll)

        if red_search:
            red_value = int(red_search.group(1))
        else:
            red_value = 0
        if green_search:
            green_value = int(green_search.group(1))
        else:
            green_value = 0
        if blue_search:
            blue_value = int(blue_search.group(1))
        else:
            blue_value = 0

        roll_object['blue']  = blue_value
        roll_object['green'] = green_value
        roll_object['red']   = red_value
        
        rolls.append(roll_object)

    return rolls

for input_game in puzzle_data:

    game_object = {
        'game_id':  get_game_id(input_game),    # int
        'rolls':    get_game_rolls(input_game)  # list of roll objects
    }

    games.append(game_object)

print(f"total games played: {len(games)}")

# just printing the last game while I debug the rolls all being the same
print(games[-1])

print(f"possible_game_ids: {possible_game_ids}")