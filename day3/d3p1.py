#!/usr/bin/env python3

# Day 3: Gear Ratios

with open('./puzzle-input.txt') as file:
    puzzle_data = [line.strip() for line in file]

#TODO: check to make sure that we aren't on the border of the grid
# -> otherwise we will get an index out of range error

    # theoretical solution:
    # if x == 0: # we are on the left border
    # if x == num_columns: # we are on the right border
    # if y == 0: # we are on the top border
    # if y == num_rows: # we are on the bottom border


num_columns = len(puzzle_data[0])  # X # COLUMNS # length of first row since they are all the same
num_rows = len(puzzle_data)        # Y # ROWS    # number of rows

# create a (num_columns X num_rows) grid of 0s
grid = [[0 for i in range(num_columns)] for j in range(num_rows)]

def get_adjacent(coordinates):
    x = coordinates[0]
    y = coordinates[1]
    adjacent_items = {
            'original'   : {'item': grid[x][y] , 'coordinates': (x, y)},
            'up'         : {'item': grid[x-1][y] , 'coordinates': (x-1, y)},
            'down'       : {'item': grid[x+1][y] , 'coordinates': (x+1, y)},
            'left'       : {'item': grid[x][y-1] , 'coordinates': (x, y-1)},
            'right'      : {'item': grid[x][y+1] , 'coordinates': (x, y+1)},
            'up_left'    : {'item': grid[x-1][y-1] , 'coordinates': (x-1, y-1)},
            'up_right'   : {'item': grid[x-1][y+1] , 'coordinates': (x-1, y+1)},
            'down_left'  : {'item': grid[x+1][y-1] , 'coordinates': (x+1, y-1)},
            'down_right' : {'item': grid[x+1][y+1] , 'coordinates': (x+1, y+1)},
        }
    return adjacent_items

# return false if we are not on the border of the grid
def border_check(coordinates):
    x = coordinates[0]
    y = coordinates[1]
    if x == 0: # we are on the left border
        print(f"{coordinates}:left border")
        return True
    elif x == num_columns: # we are on the right border
        print(f"{coordinates}:right border")
        return True
    elif y == 0: # we are on the top border
        print(f"{coordinates}:top border")
        return True
    elif y == num_rows: # we are on the bottom border
        print(f"{coordinates}:bottom border")
        return True

def get_adjacent_numbers(adjacent_items_object):
    adjacent_numbers = []
    # takes in a dict of adjacent items and returns a list of adjacent numbers
    # to any numbers found in the passed dict
    adjacent_items = adjacent_items_object
    for direction in adjacent_items:
        if border_check(adjacent_items[direction]['coordinates']) == False: # if we are not on the border of the grid
            if adjacent_items[direction]['item'].isdigit(): # if the item is a number
                # pull cells to the left and right in case there are numbers there too
                adjacent_number = adjacent_items[direction]['item'] # the first number we found
                adjacent_number_coordinates = adjacent_items[direction]['coordinates'] # the coordinates of the first number we found
                adjacent_number_adjacent_cells = get_adjacent(adjacent_number_coordinates) 

                for direction in adjacent_number_adjacent_cells:
                    if adjacent_number_adjacent_cells[direction]['item'].isdigit():
                        adjacent_number = adjacent_number + adjacent_number_adjacent_cells[direction]['item']
                        adjacent_numbers.append(adjacent_number)
                        return adjacent_numbers
                    #TODO: i'm not sure if this is working correctly

# fill grid with puzzle data
for y in range(num_rows):
    for x in range(num_columns):
        grid[y][x] = puzzle_data[y][x]

symbols = ['+', '@', '-', '%', '/', '*', '&', '$', '#', '=']

for y in range(num_rows):
    for x in range(num_columns):
        # if the current cell is a special character
        if grid[x][y] in symbols:
            gear_item = grid[x][y]
            item_coordinates = (x, y)
            readable_coordinates = (x+1, y+1) # for humans & accessing the data in the IDE not the program
            adjacent_cells = get_adjacent(item_coordinates)
            adjacent_numbers = get_adjacent_numbers(adjacent_cells)
            print(f"item_coordinates:{readable_coordinates}\ngear_item:{gear_item}\nadjacent_numbers:{adjacent_numbers}")
            




# grid[ up/down ][ left/right ]
# print(f"grid[0][11]:{grid[0][11]}, grid[0][12]:{grid[0][12]}, grid[0][13]:{grid[0][13]}")