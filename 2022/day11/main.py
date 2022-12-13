import math
import re
from collections import defaultdict

import numpy

data = [monkey for monkey in open("input.in").read().strip().split("\n\n")]
parser = re.compile("-?\d+")
monkeys = defaultdict(dict)
for monkey in data:
    lines = monkey.split("\n")
    monkeys[int(parser.findall(lines[0].strip())[0])] = {
        "items": [int(x) for x in parser.findall(lines[1].strip())],
        "multi": lines[2].strip().split("old", 1)[1].strip().split(" "),
        "test": int(parser.findall(lines[3].strip())[0]),
        "true": int(parser.findall(lines[4].strip())[0]),
        "false": int(parser.findall(lines[5].strip())[0]),
        "inspections": 0
    }
least_common_multiple = numpy.prod([monkey['test'] for monkey in monkeys.values()])
for i in range(10000):
    if i % 1000 == 0:
        print(f"Round: {i}")
        for i, monkey in monkeys.items():
            print(f"Monkey {i}: {monkey['inspections']}")
        print()
    for monkey in monkeys.values():
        for _ in range(len(monkey["items"])):
            item = monkey["items"].pop()
            operator = monkey['multi'][0]
            value = int(monkey['multi'][1]) if monkey['multi'][1].isnumeric() else item
            if operator == '*':
                item *= value
            elif operator == '/':
                item = int(item / value)
            elif operator == '+':
                item += value
            elif operator == '-':
                item -= value
            # Test
            item = item % least_common_multiple
            if item % monkey['test'] == 0:
                monkeys[monkey['true']]['items'].append(item)
            else:
                monkeys[monkey['false']]['items'].append(item)
            monkey['inspections'] += 1

inspection = []
for monkey in monkeys.values():
    inspection.append(monkey['inspections'])
inspection.sort(reverse=True)
print(inspection[0] * inspection[1])
