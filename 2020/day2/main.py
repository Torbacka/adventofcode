import re

parser = re.compile("-?\d+")
data = [line for line in open("input/input.in")]
valid_passwords = 0
for d in data:
    input = d.split(" ")
    numbers = input[0].split("-")
    letter = input[1].split(":")[0]
    password = input[2]
    count = 0
    found = False
    if password[int(numbers[0]) -1 ] == letter:
        found = not found
    if password[int(numbers[1]) - 1] == letter:
        found = not found
    if found:
        valid_passwords += 1



print(valid_passwords)