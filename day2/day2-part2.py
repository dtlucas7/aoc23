import regex as re

with open('./puzzle-input-day2.txt') as file:
    puzzle_data = [line.strip() for line in file]

RED_MAX     = 12
GREEN_MAX   = 13
BLUE_MAX    = 14

# list of game objects
games = []

# list of IDs of games that are impossible
impossible_game_ids = []

for game in puzzle_data:
    
    game_object = {
        'game_id': int(game.split(':')[0].split(' ')[1]),
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

# the list(set()) is to uniq the list
possible_game_ids = list(set([game['game_id'] for game in games if game['game_id'] not in impossible_game_ids]))

possible_power_list = []
all_power_list = [] 

# get the power values for each game in the
# possible game list
for id in possible_game_ids:
    current_game = [game for game in games if game['game_id'] == id][0]

    # get the minimum number of red, green, and blue dice
    min_red     = max([roll['red'] for roll in current_game['rolls']])
    min_green   = max([roll['green'] for roll in current_game['rolls']])
    min_blue    = max([roll['blue'] for roll in current_game['rolls']])

    power_value = min_red * min_green * min_blue
    
    possible_power_list.append(power_value)

    print(f"Game {current_game['game_id']} requires at least {min_red} red, {min_green} green, and {min_blue} blue dice")
    print(f"Power value: {power_value}")

for game in games:
    # get the minimum number of red, green, and blue dice
    min_red     = max([roll['red'] for roll in game['rolls']])
    min_green   = max([roll['green'] for roll in game['rolls']])
    min_blue    = max([roll['blue'] for roll in game['rolls']])

    power_value = min_red * min_green * min_blue
    
    all_power_list.append(power_value)

    print(f"Game {game['game_id']} requires at least {min_red} red, {min_green} green, and {min_blue} blue dice")
    print(f"Power value: {power_value}")

part_2_solution_full = sum(all_power_list)

part_2_solution = sum(possible_power_list)
print(possible_power_list)
print(f"Part 2 solution: {part_2_solution_full}")