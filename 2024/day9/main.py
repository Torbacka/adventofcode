import re
from collections import defaultdict

parser = re.compile(r"-?\d+")

data = [int(c) for c in open("input/input.in").read()]
result= 0
file = True
file_id = 0
memory = []
for i, value in enumerate(data):
    if i % 2 == 0:
        for n in range(value):
            memory.append(file_id)
        file_id += 1
    else:
        for n in range(value):
            memory.append(None)

empty_pointer = 0
for n in range(empty_pointer, len(memory)):
    if memory[n] is None:
        empty_pointer = n
        break
for i in range(len(memory)-1, 0, -1):
    if memory[i] is not None and empty_pointer < i:
        memory[empty_pointer] = memory[i]
        memory[i] = None
        for n in range(empty_pointer, len(memory)):
            if memory[n] is None:
                empty_pointer = n
                break

check = 0
for i, file_id in enumerate(memory):
    if file_id is None:
        break
    check += file_id*i

print(check)
