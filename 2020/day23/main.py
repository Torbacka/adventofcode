# Part 2
input = [int(x) for x in "925176834"]
for x in range(max(input), 1000000):
    input.append(x + 1)

current = input[0]
ring = dict()
for i in range(len(input)):
    if i == len(input) - 1:
        ring[input[i]] = input[0]
    else:
        ring[input[i]] = input[i + 1]
max_value = max(ring.keys())


def move(current, ring):
    picked_up = [ring[current], ring[ring[current]], ring[ring[ring[current]]]]
    next = ring[ring[ring[ring[current]]]]
    ring[current] = next
    destination = current - 1
    if destination == 0:
        destination = max_value
    while destination in picked_up:
        destination -= 1
        if destination == 0:
            destination = max_value
    temp = ring[destination]
    ring[destination] = picked_up[0]
    ring[picked_up[-1]] = temp
    return next, ring


for x in range(10000000):
    current, ring = move(current, ring)

print(ring[1] * ring[ring[1]])
