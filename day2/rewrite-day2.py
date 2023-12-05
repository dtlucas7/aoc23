import re
import json

with open('./puzzle-input-day2.txt') as file:
    puzzle_data = [line.strip() for line in file]

games = [
    {
        'game_id': int,
        'rolls': 
            [
                {
                    'roll_id':  int,
                    'red':      int,
                    'green':    int,
                    'blue':     int
                }
            ]
    }
]

# list of IDs of games that are possible
possible_game_ids = []

def is_game_possible(game_object):
    # this is where the values of each cube are checked
    # to make sure they are less than the max value for each color
    pass

# parsed game object
game_object = {
    'game_id': int,
    'rolls': 
        [
            {
                'roll_id':  int,
                'red':      int,
                'green':    int,
                'blue':     int
            }
        ]
}

for game in puzzle_data:

    # 2 fields -> game ID and game data
    game_fields = game.split(':')

    # the field before the colon
    game_id = int(str(game_fields).split(' ')[1].strip('\','))

    # the field after the colon
    # game_data will be split by the semi-colon into rolls
    game_data = game_fields[1].strip()

    # each roll will be split by the comma into colors
    rolls = game_data.split(';')

    #debug
    print(f"Game ID: {game_id}")

    for roll_id,roll in enumerate(rolls):
        roll_object = {
            'roll_id':  int,
            'red':      int,
            'green':    int,
            'blue':     int
        }
        # strip whitespace
        roll = roll.strip()
        # each roll will be split by the comma into colors
        colors = roll.split(',')

        red_search = re.search(r'(\d+) red', roll)
        
        if red_search:
            #print(red_search.group(1))
            red_value = int(red_search.group(1))
        else:
            red_value = 0
        
        green_search = re.search(r'(\d+) green', roll)
        
        if green_search:
            #print(green_search.group(1))
            green_value = int(green_search.group(1))
        else:
            green_value = 0
        
        blue_search = re.search(r'(\d+) blue', roll)
        
        if blue_search:
            #print(blue_search.group(1))
            blue_value = int(blue_search.group(1))
        else:
            blue_value = 0
        
        roll_object['roll_id'] = roll_id
        roll_object['red'] = red_value
        roll_object['green'] = green_value
        roll_object['blue'] = blue_value
        game_object['rolls'].append(roll_object)
    
    games.append(game_object)

for game in games:
    print(game)
    print('\n')