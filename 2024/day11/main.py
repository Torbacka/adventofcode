stones = [int(line) for line in open("input/input.in").read().split(" ")]

for blink in range(25):
    new_stones = []
    for stone in stones:

        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            middle_index = len(str(stone)) // 2
            new_stones.append(int(str(stone)[:middle_index]))
            new_stones.append(int(str(stone)[middle_index:]))
        else:
            new_stones.append(stone * 2024)
    stones = new_stones

print(len(stones))
