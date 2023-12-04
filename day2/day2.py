import json
import regex as re

with open('puzzle-input-day2.txt') as file:
    puzzle_data = [line.strip() for line in file]

# get all games that are possible with this configuration
red_max     = 12
green_max   = 13
blue_max    = 14

for game in puzzle_data:
    game_dict = {
        'game_id': int,
        'number_of_draws': int,
        'draws': [
                {
                    'draw_id':int,
                    'red': int,
                    'blue': int,
                    'green': int, 
                    }
            ]
    }
    
    game_number = re.search(r'Game (?P<game_id>\d+):', game)
    game_id = game_number.group('game_id')
    game_data = game.split(':')[1].strip()
    draw_list = game_data.split(';') # list of draws for a single game
    game_dict['game_id'] = int(game_id)
    game_dict['number_of_draws'] = len(draw_list)
    
    print(f"working on current game/line:\n{game}")

    for i,draw in enumerate(draw_list, start=1):
        draw = draw.strip()
        colors_in_current_draw = draw.split(',')
        for color in colors_in_current_draw:
            color = color.strip()
        print(colors_in_current_draw)
        
