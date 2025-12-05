import re

parser = re.compile(r"-?\d+")
data = open("input/input.in").read().split("\n\n")
rules = [line.strip().split("-") for line in data[0].split("\n")]
ingredients = [line.strip() for line in data[1].split("\n")]

sum = 0
for ingredient in ingredients:
    for low, high in rules:
        if int(low) <= int(ingredient) <= int(high):
            sum += 1
            break

print(sum)