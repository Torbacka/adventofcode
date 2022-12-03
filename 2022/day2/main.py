
data = [line.strip().split(" ") for line in open("input/input.in").readlines()]

winners = {
    'X': 'Z',
    'Y': 'X',
    'Z': 'Y'
}
losers = {
    'X': 'Y',
    'Y': 'Z',
    'Z': 'X'
}


def convert(o, m):
    if m == 'X':
        return winners[o]
    elif m == 'Y':
        return o
    elif m == 'Z':
        return losers[o]


score = 0
for line in data:
    first = chr(bytes(line[0], 'utf-8')[0] + 23)
    second = convert(first, line[1])

    if second == first:
        score += 3
    elif winners[second] == first:
        score += 6
    score += bytes(second, 'utf-8')[0] - 23 - 64
    print(score)
