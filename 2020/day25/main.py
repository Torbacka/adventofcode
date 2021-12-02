import re

parser = re.compile("-?\d+")
data = [int(x) for line in open("input/input.in").readlines() for x in parser.findall(line.strip())]

door_pubkey = 8421034
card_pubkey = 15993936


subject_number = 7
value = 1
step = 1
door_found = False
card_found = False
loop_size = 0
while not door_found or not card_found:
    value *= subject_number
    value = value % 20201227
    if value == door_pubkey:
        door_found = True
        loop_size = step
        break
    if value == card_pubkey:
        card_found = True
        loop_size = step
        break
    step +=1

subject_number = card_pubkey if door_found else door_pubkey
value = 1
for i in range(loop_size):
    value *= subject_number
    value = value % 20201227
print(value)