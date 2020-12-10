import math

data = [int(line) for line in open("input/input.in")]

adapters = sorted(data)
diff_3 = 0
diff_5 = 0
sets = []
n = 0
for i in range(len(adapters)):
    n -= 1
    if n > 0:
        continue
    for n in range(3):
        if i == 0:
            if adapters[i + n] > 3:
                n -= 1
                break
            diff = (adapters[i + n])
        else:
            if (i + n) > len(adapters) - 1:
                n -= 1
                break
            if adapters[i + n] - adapters[i - 1] > 3:
                n -= 1
                break
            diff = adapters[i + n] - adapters[i + n - 1]

        if diff == 1:
            diff_3 += 1
        elif diff == 3:
            diff_5 += 1

    if n == 2 and (i + n + 1) <= len(adapters) - 1 and adapters[i + n + 1] - adapters[i + n] == 1:
        n += 1
        sets.append(7)
    if n == 2:
        sets.append(4)
    elif n == 1:
        sets.append(2)

print(diff_5 * diff_3)
print(math.prod(sets))

