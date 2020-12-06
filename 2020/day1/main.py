data = [int(line) for line in open("input/input.in")]

length = len(data)

for i in range(length):
    for j in range(i+1, length):
        for k in range(j + 1, length):
            if (data[i] + data[j] + data[k]) == 2020:
                print(data[i] * data[j] * data[k])

