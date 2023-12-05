import json

games = []

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

games.append(game_object)
for game_offset, game_data in enumerate(games):
    print(f"game offset: {game_offset}| game data: {game_data}")