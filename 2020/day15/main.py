import re

numbers = [int(number) for number in open("input/input.in").read().split(",")]
spoken = {}
previous = numbers[-1]
for i in range(len(numbers) - 1):
    spoken[numbers[i]] = [i + 1]

for i in range(len(numbers) + 1, 30000001):
    if previous in spoken:
        if len(spoken[previous]) == 1:
            spoken[previous].append(i - 1)
        elif len(spoken[previous]) == 2:
            prev = spoken[previous]
            prev[0] = prev[1]
            prev[1] = i - 1
        previous = i - 1 - spoken[previous][0]
    else:
        spoken[previous] = [i - 1]
        previous = 0
print(previous)
