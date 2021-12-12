

def main():
    data = [[int(x) for x in line.strip()] for line in open("input/input.in").readlines()]
    print(data)
    count = 0
    step = 1
    for i in range(0, 500):
        data = [[number + 1 for number in line] for line in data]
        ready_for_flash = [(x, y) for y, line in enumerate(data) for x, number in enumerate(line) if number > 9]
        flashed = flash(ready_for_flash, set(), data)
        if len(flashed) == 100:
            print(step)
        step +=1
        if len(flashed) < 100:
            count += len(flashed)
    print(count)

def flash(ready_flash, flashed, data):
    i = 0
    for x, y in ready_flash:
        flashed.add((x, y))
        i += 1


        if x > 0:
            if y > 0:
                data[y - 1][x - 1] += 1
                if data[y - 1][x - 1] > 9 and (x - 1, y - 1) not in ready_flash:
                    ready_flash.append((x - 1, y - 1))
            if y < len(data) - 1:
                data[y + 1][x - 1] += 1
                if data[y + 1][x - 1] > 9 and (x - 1, y + 1) not in ready_flash:
                    ready_flash.append((x - 1, y + 1))
            data[y][x - 1] += 1
            if data[y][x - 1] > 9 and (x - 1, y) not in ready_flash:
                ready_flash.append((x - 1, y))
        if x < len(data[0]) - 1:
            if y > 0:
                data[y - 1][x + 1] += 1
                if data[y - 1][x + 1] > 9 and (x + 1, y - 1) not in ready_flash:
                    ready_flash.append((x + 1, y - 1))
            if y < len(data) - 1:
                data[y + 1][x + 1] += 1
                if data[y + 1][x + 1] > 9 and (x + 1, y + 1) not in ready_flash:
                    ready_flash.append((x + 1, y + 1))
            data[y][x + 1] += 1
            if data[y][x + 1] > 9 and (x + 1, y) not in ready_flash:
                ready_flash.append((x + 1, y))
        if y > 0:
            data[y - 1][x] += 1
            if data[y - 1][x] > 9 and (x, y - 1) not in ready_flash:
                ready_flash.append((x, y - 1))
        if y < len(data) - 1:
            data[y + 1][x] += 1
            if data[y + 1][x] > 9 and (x, y + 1) not in ready_flash:
                ready_flash.append((x, y + 1))

    for x, y in flashed:
        data[y][x] = 0
    return flashed

def print_grid(data):
    for y, line in enumerate(data):
        for x, number in enumerate(line):
            if number < 10:
                print(f"{data[y][x]}", end='')
            else:
                print(f"{data[y][x]}", end='')
        print()
    print()


if __name__ == '__main__':
    main()
