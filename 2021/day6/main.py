import re
from collections import defaultdict

data = [list(map(int, re.findall("-?\d+", line))) for line in open("input/input.in").readlines()]


def main():
    fishs = defaultdict(lambda: 0)
    for fish in data[0]:
        fishs[fish] += 1

    for i in range(0,256 ):
        temp_fishs = defaultdict(lambda: 0)
        for fish, number in fishs.items():
            fish -= 1
            if fish == -1:
                temp_fishs[8] += number
                fish = 6
                temp_fishs[fish] += number
            else:
                temp_fishs[fish] += number
        fishs = temp_fishs
    print(sum(fishs.values()))

if __name__ == '__main__':
    main()
