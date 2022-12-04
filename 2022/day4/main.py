def range_subset(range1, range2):
    if range1.start <= range2.start <= range1.stop:
        return True
    return False


data = [[int(elf) for elfs in line.split(",") for elf in elfs.split("-")]
        for line in open("input/input.in").readlines()]

sum = 0
for line in data:
    first = range(line[0], line[1])
    second = range(line[2], line[3])

    if range_subset(first, second) or range_subset(second, first):
        sum += 1
print(sum)
