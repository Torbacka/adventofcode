import re
from collections import defaultdict

parser = re.compile("-?\d+")
data = [line.strip() for line in open("input/input.in").read().strip().split(",")]

sums = 0


def hash_code(s):
    hash = 0
    for c in s:
        hash += ord(c)
        hash *= 17
        hash %= 256
    return hash


hashmap = defaultdict(lambda: defaultdict(int))

for line in data:
    if line[-1] == '-':
        label = line[:-1]
        hash = hash_code(label)
        if hash in hashmap and label in hashmap[hash]:
            hashmap[hash].pop(label)
    else:
        label = line[:-2]
        focal_length = int(line[-1])
        hash = hash_code(label)
        hashmap[hash][label] = focal_length
sums = 0

for key, box in hashmap.items():
    for i, entry in enumerate(box.items()):
        sums += (key + 1) * (i + 1) * entry[1]
print(sums)