import re

parser = re.compile(r"-?\d+")
data = [line.strip() for line in open("input/input.in").readlines()]

sum = 0

for line in data:
    position = 0
    window_size = len(line) - 11
    battery = ""
    for battery_i in range (12):
        window = list(map(int, line[battery_i+position:window_size + battery_i+position]))
        max_value = max(window)
        battery += str(max_value)
        max_pos = window.index(max_value)
        position += max_pos
        window_size -= max_pos
        # Find biggest in window
        biggest = 0

    print(battery)
    sum += int(battery)
print(sum)

