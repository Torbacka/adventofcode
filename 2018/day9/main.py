import re
from collections import defaultdict, deque

parser = re.compile("-?\d+")
data = [int(x) for line in open("input/input.txt").readlines() for x in parser.findall(line.strip())]


def main():
    print(play_game(data[0], data[1]))


def play_game(max_players, last_marble):
    scores = defaultdict(int)
    circle = deque([0])

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % max_players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return max(scores.values()) if scores else 0


if __name__ == '__main__':
    main()
