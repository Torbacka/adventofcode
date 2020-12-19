import re
from itertools import product


def modifyBit(n, p, b):
    mask = 1 << p
    return (n & ~mask) | ((b << p) & mask)


def permutations(list):
    return product(*[[0, 1]] * len(list))


print(list(permutations([0, 5, 8, 12])))
parser = re.compile("-?\d+")
lines = [line.strip() for line in open("input/input.in").readlines()]
mask_perm = 0
address = {}
for line in lines:
    if "mask = " in line:
        mask_perm = []
        string_mask = line.split('=')[1].strip()
        for i, c in enumerate(reversed(string_mask)):
            if c == 'X':
                mask_perm.append(i)
        mask = int(string_mask.replace("X", "0"), 2)
    else:
        memory, value = parser.findall(line)
        value = int(value)
        memory = int(memory)
        memory |= mask
        for perm in permutations(mask_perm):
            memory_perm = memory
            for i, v in enumerate(perm):
                memory_perm = modifyBit(memory_perm, mask_perm[i], v)
            address[memory_perm] = value

print(sum(address.values()))
