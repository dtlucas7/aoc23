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

with open('puzzle-input.txt') as file:
    calibration_data = [line.strip() for line in file]

main_numbers_list = []

def get_numbers(line):
    # regex to find either digits or spelled out numbers
    numbers_regex = re.compile('(zero|one|two|three|four|five|six|seven|eight|nine|\d)')
    # list of all numbers in the line
    numbers_list = numbers_regex.findall(line)
    for number in numbers_list:
        if number == 'zero':
            numbers_list[numbers_list.index(number)] = 0
        elif number == 'one':
            numbers_list[numbers_list.index(number)] = 1
        elif number == 'two':
            numbers_list[numbers_list.index(number)] = 2
        elif number == 'three':
            numbers_list[numbers_list.index(number)] = 3
        elif number == 'four':
            numbers_list[numbers_list.index(number)] = 4
        elif number == 'five':
            numbers_list[numbers_list.index(number)] = 5
        elif number == 'six':
            numbers_list[numbers_list.index(number)] = 6
        elif number == 'seven':
            numbers_list[numbers_list.index(number)] = 7
        elif number == 'eight':
            numbers_list[numbers_list.index(number)] = 8
        elif number == 'nine':
            numbers_list[numbers_list.index(number)] = 9
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
