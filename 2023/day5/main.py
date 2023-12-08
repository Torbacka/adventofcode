import re
import sys

parser = re.compile("-?\d+")
data = [group for group in open("input/input.in").read().split("\n\n")]
seeds = [int(seed) for seed in data[0].strip().split()[1:]]

paths = [[(range(int(m.split()[1]), int(m.split()[1]) + int(m.split()[2])),
           int(m.split()[0]) - int(m.split()[1])) for n in line.strip().split(":")[1:] for m
          in n.strip().split("\n")] for line in data[1:]]
smallest = sys.maxsize
for seed in seeds:
    print(seed)
    for i, path in enumerate(paths):
        temp_seed = seed
        smallest_seed = seed
        for value in path:
            if temp_seed in value[0]:
                if temp_seed <= smallest_seed:
                    smallest_seed += value[1]
                    print(f"{i}, {seed} ", "")
        seed = smallest_seed
    print(seed)
    if seed < smallest:
        smallest = seed

print(smallest)