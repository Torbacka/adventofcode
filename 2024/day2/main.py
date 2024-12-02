data = [line.strip() for line in open("input/input.in").readlines()]
sum = 0


def check_safe(levels):
    dec = False
    global sum
    for i in range(0, len(levels) - 1):
        if i == 0:
            dec = levels[i] > levels[i + 1]
        if dec != (levels[i] > levels[i + 1]):
            break
        if 0 == abs(levels[i] - levels[i + 1]) or abs(levels[i] - levels[i + 1]) > 3:
            break
        if i == len(levels) - 2:
            return True
    return False


for line in data:
    levels = [int(i) for i in line.split()]
    safe = check_safe(levels)
    i = 0
    while not safe and i < len(levels):
        copy_l = levels.copy()
        copy_l.pop(i)
        safe = check_safe(copy_l)
        if safe:
            break
        i += 1
    if safe:
        sum += 1
print(sum)
