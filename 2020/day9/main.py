import re

data = [int(line.strip()) for line in open("input/input.in")]
sums = set()
pebel_size = 25
for i in range(0, len(data)):
    pebels = data[i:i + pebel_size]
    for x in range(len(pebels)):
        for y in range(x + 1, len(pebels)):
            sums.add((int(pebels[x]) + int(pebels[y])))
    if data[i+pebel_size] not in sums:
        part_1 = data[i+pebel_size]
        break
    sums = set()

for i in range(0, len(data)):
    continues_sum = data[i]
    for n in range(i+1, len(data)):
        continues_sum +=data[n]
        if continues_sum == part_1:
            lists = sorted(data[i:n +1])
            print(lists[0] + lists[-1])
            exit(0)
        elif continues_sum > part_1:
            break
