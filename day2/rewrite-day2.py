import regex as re
import json

with open('puzzle-input-day2.txt') as file:
    puzzle_data = [line.strip() for line in file]

games = [
    {
        'game_id': int,
        'rolls': 
            {
                'roll_id':  int,
                'red':      int,
                'green':    int,
                'blue':     int
            }
    }
]

for game in puzzle_data:
    game_fields = game.split(':')
    game_id = int(str(game_fields).split(' ')[1].strip('\','))
    game_data = game_fields[1].strip()
    print(f"game id: {game_id}\ngame data: {game_data}")
    