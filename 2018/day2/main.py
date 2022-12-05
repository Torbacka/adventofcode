data = [[int(number.strip()) for number in line.split(" ")] for line in open('input.in').readlines()]

sum = 0
for line in data:
    sum += max(line) - min(line)
print(f"part 1: {sum}")


sum = 0
for line in data:
    found = False
    for i, number in enumerate(line):
        for n in range(0, len(line)):
            if i != n and number % line[n] == 0:
                sum += int((number / line[n]))
                found = True
                break
        if found:
            break
print(f"part 2: {sum}")
