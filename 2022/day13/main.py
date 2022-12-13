import ast
from functools import cmp_to_key

import numpy

data = [[ast.literal_eval(x) for x in line.strip().split("\n")]
        for line in open("input.in").read().strip().split("\n\n")]


def compare(list1, list2):
    cmp = 0
    for i in range(max(len(list1), len(list2))):
        if i == len(list1):
            return -1
        if i == len(list2):
            return 1
        item = list1[i]
        item2 = list2[i]
        if isinstance(item, list) and isinstance(item2, list):
            cmp = compare(item, item2)
        elif isinstance(item, list) and not isinstance(item2, list):
            cmp = compare(item, [item2])
        elif not isinstance(item, list) and isinstance(item2, list):
            cmp = compare([item], item2)
        elif item == item2:
            continue
        else:
            return -1 if item < item2 else 1
        if cmp != 0:
            break
    return cmp


print(sum([i + 1 for i, line in enumerate(data)
           if compare(line[0], line[1]) == -1 and line[0] != [[2]]]))
data = [item for line in data for item in line]
print(numpy.prod([i + 1 for i, line in enumerate(sorted(data, key=cmp_to_key(compare)))
                  if line == [[2]] or line == [[6]]]))
