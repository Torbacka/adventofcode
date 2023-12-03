import re

parser = re.compile(r"-?\d+")
data = [line.strip() for line in open("input/input.in").readlines()]


sum = 0
for line in data:
    bags = {
        "red": 1,
        "green": 1,
        "blue": 1
    }
    game = line.split(":")
    id = int(parser.findall(game[0])[0])
    for set in game[1].strip().split(";"):
        for color in set.strip().split(","):
            value, color = color.strip().split(" ")
            if bags[color] < int(value):
                bags[color] = int(value)
    sum += bags["red"]*bags["green"]*bags["blue"]

print(sum)