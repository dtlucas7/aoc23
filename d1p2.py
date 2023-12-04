import regex

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

# takes a line from the puzzle input as an argument
# returns the number for that line corresponding to (first_number + last_number)
def get_line_number(line):
    # result_number is the first and last number of the line
    # combined to make a single number
    # list of ints after converting the string version of the numbers
    numbers_in_line = []
    # regex to find either digits or spelled out numbers
    numbers_regex = regex.compile('(zero|one|two|three|four|five|six|seven|eight|nine|\d)')
    # list of all numbers in the line
    #matches_in_line = numbers_regex.findall(line, overlapped=True)
    matches_in_line = numbers_regex.findall(line, overlapped=False)
    for number in matches_in_line:
        if number.isdigit():
            numbers_in_line.append(int(number))
        else:
            numbers_in_line.append(int(numbers[number]))
    result_number = str(numbers_in_line[0]) + str(numbers_in_line[-1])
    #print(f"{line}:{result_number}")
    return int(result_number)

# list that each of the line results will be added to, then summed
results_list = []

for line in calibration_data:
    # get list of numbers in the line
    current_line_number = get_line_number(line)
    results_list.append(current_line_number)

print(sum(results_list))
