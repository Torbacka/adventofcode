data = [(line.strip().split(" ")[0], int(line.strip().split(" ")[1])) for line in open("input.in").readlines()]

snake = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]

visited = set()


def print_grid(snake):
    for y in range(-10, 10):
        for x in range(-6, 10):
            found = None
            for i, part in enumerate(snake):
                if part == (x, y):
                    found = i
                    break
            if found is None:
                if (x, y) in visited:
                    print("#", end="")
                else:
                    print(".", end="")
            elif found == 0:
                print("H", end="")
            elif found == len(snake) - 1:
                print("T", end="")
            else:
                print(f"{found}", end="")

        print()


def move_tail(head, tail):
    # check if head is one away from tail
    for y in range(-1, 2):
        for x in range(-1, 2):
            if (tail[0] + x, tail[1] + y) == head:
                return tail
    if head[0] > tail[0]:
        tail = (tail[0] + 1, tail[1])
    elif head[0] < tail[0]:
        tail = (tail[0] - 1, tail[1])
    if head[1] > tail[1]:
        tail = (tail[0], tail[1] + 1)
    elif head[1] < tail[1]:
        tail = (tail[0], tail[1] - 1)
    return tail


for dir, moves in data:
    print(f"== {dir} {moves} ==")
    for move in range(moves):
        if dir == 'R':
            snake[0] = (snake[0][0] + 1, snake[0][1])
        if dir == 'L':
            snake[0] = (snake[0][0] - 1, snake[0][1])
        if dir == 'D':
            snake[0] = (snake[0][0], snake[0][1] + 1)
        if dir == 'U':
            snake[0] = (snake[0][0], snake[0][1] - 1)
        for i in range(0, len(snake)-1):
            head = snake[i]
            tail = snake[i + 1]
            snake[i + 1] = move_tail(head, tail)
        print_grid(snake)
        visited.add(snake[-1])
        print()

print(len(visited))
