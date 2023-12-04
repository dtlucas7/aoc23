import re

'''
# day 1 part 2

two1nine:29
eightwothree:83
abcone2threexyz:13
xtwone3four:24
4nineeightseven2:42
zoneight234:14
7pqrstsixteen:76
'''
numbers = {
    'zero':0,
    'one':1,
    'two':2,
    'three':3,
    'four':4,
    'five':5,
    'six':6,
    'seven':7,
    'eight':8,
    'nine':9
    }


with open('puzzle-input.txt') as file:
    calibration_data = [line.strip() for line in file]

main_numbers_list = []

def get_numbers(line):
    # regex to find either digits or spelled out numbers
    numbers_regex = re.compile('(zero|one|two|three|four|five|six|seven|eight|nine|\d)')
    # list of all numbers in the line
    numbers_in_line = numbers_regex.findall(line)
    for number in numbers_in_line:
        if number.isdigit():
            continue
        else:
            #does this edit the list in place?
            # or do i need to create new variable?
            number = numbers[number]
    return numbers_list

for line in calibration_data:
    # get list of numbers in the line
    numbers_on_current_line = get_numbers(line)
    x = str(numbers_on_current_line[0])
    y = str(numbers_on_current_line[-1])
    # this concatenates the first and last number in the line
    line_number = x + y
    # cast the concatenated number to an int and add it to the main list
    main_numbers_list.append(int(line_number))

# sum all the numbers in the list
total = sum(main_numbers_list)
print(total)
