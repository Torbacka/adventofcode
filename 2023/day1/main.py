import re

parser = re.compile(r"-?\d+")
data = [line.strip() for line in open("input/input.in").readlines()]
sum = 0
numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

for line in data:
    for i, number in enumerate(numbers, 1):
        line = line.replace(number, number[0] + str(i) + number[-1])
    found_numbers = parser.findall(line)
    sum += int(found_numbers[0][0] + found_numbers[-1][-1])

print(sum)
