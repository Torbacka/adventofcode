data = open("input.in").read()


def solve(start):
    for i in range(0, len(data)):
        marker = set()
        marker.update(data[i:i + start])
        if len(marker) == start:
            return i + start


print(f"part 1: {solve(4)}")
print(f"part 2: {solve(14)}")
