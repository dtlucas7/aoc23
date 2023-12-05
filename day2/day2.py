import regex as re
import json

with open('./puzzle-input-day2.txt') as file:
    puzzle_data = [line.strip() for line in file]

RED_MAX     = 12
GREEN_MAX   = 13
BLUE_MAX    = 14

# list of game objects
games = []

# list of IDs of games that are impossible
impossible_game_ids = []

for game_id, game in enumerate(puzzle_data, start=1):
    
    game_object = {
        'game_id': game_id,
        'rolls': []
    }
    
    # list of rolls for the current game
    current_game_rolls = game.split(':')[1].strip().split(';')

    for roll in current_game_rolls:
        
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
        
        game_object['rolls'].append({
            'red': red_value,
            'green': green_value,
            'blue': blue_value
        })

        games.append(game_object)

for game in games:
    for roll in game['rolls']:
        if roll['red'] <= RED_MAX and roll['green'] <= GREEN_MAX and roll['blue'] <= BLUE_MAX:
            continue
        else:
            impossible_game_ids.append(game['game_id'])

possible_game_ids = list(set([game['game_id'] for game in games if game['game_id'] not in impossible_game_ids]))
solution = sum(possible_game_ids)
# uniq the possible game IDs
#possible_game_ids = list(set(possible_game_ids))
print(f"possible game IDs: {possible_game_ids}")
print(f"sum of possible game IDs: {solution}")