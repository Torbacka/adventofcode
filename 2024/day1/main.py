from collections import Counter
data = [line.strip() for line in open("input/input.in").readlines()]
left =[]
right =[]
for line in data:
    s  = line.split("   ")
    left.append(int(s[0]))
    right.append(int(s[1]))

left.sort()
right.sort()
number_counter = Counter(right)
sum = 0
for i, value in enumerate(left):
    sum += abs(value * number_counter[value])

print(sum)

