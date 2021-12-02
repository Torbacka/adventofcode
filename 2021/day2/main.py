data = [line for line in open("input/input.in").readlines()]


def main():
    horizontal_position = 0
    depth = 0
    aim = 0
    for row in data:
        direction, amount = row.split(" ")
        if direction == 'forward':
            horizontal_position += int(amount)
            depth += int(amount) * aim
        elif direction == 'down':
            aim += int(amount)
        elif direction == 'up':
            aim -= int(amount)

    print(horizontal_position * depth)


if __name__ == '__main__':
    main()
