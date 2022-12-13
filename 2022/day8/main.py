data = [(line.strip().split(" ")[0], int(line.strip().split(" ")[1])) for line in open("input.in").readlines()]

h = [0, 0]
t = [0, 0]



def print_grid(t, h):
    for y in range(-10, 10):
        for x in range(-6, 10):
            if [x, y] == h:
                print("H", end="")
            elif [x, y] == t:
                print("T", end="")
            elif (x, y) in visited:
                print("#", end="")
            else:
                print(".", end="")
        print()


for dir, moves in data:
    print(f"== {dir} {moves} ==")
    for move in range(moves):
        if dir == 'R':
            h[0] += 1
            if t[1] == h[1] and t[0] + 1 != h[0] and t[0] != h[0]:
                t[0] += 1
            elif t[0] != h[0] and t[0] + 1 != h[0]:
                t[0] += 1
                t[1] = h[1]
        if dir == 'L':
            h[0] -= 1
            if t[1] == h[1] and t[0] - 1 != h[0] and t[0] != h[0]:
                t[0] -= 1
            elif t[0] != h[0] and t[0] - 1 != h[0]:
                t[0] -= 1
                t[1] = h[1]
        if dir == 'D':
            h[1] += 1
            if t[0] == h[0] and t[1] + 1 != h[1] and t[1] != h[1]:
                t[1] += 1
            elif t[1] != h[1] and t[1] + 1 != h[1]:
                t[1] += 1
                t[0] = h[0]
        if dir == 'U':
            h[1] -= 1
            if t[0] == h[0] and t[1] - 1 != h[1] and t[1] != h[1]:
                t[1] -= 1
            elif t[1] != h[1] and t[1] - 1 != h[1]:
                t[1] -= 1
                t[0] = h[0]
        visited[1] = ((t[0], t[1]))
        print_grid(t, h)
        print()

print(len(visited))
