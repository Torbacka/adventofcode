import re

parser = re.compile(" (.) .+ (.) ")
pairs = [parser.search(line.strip()) for line in open("input/day_07.txt").readlines()]


def main():
    print(pairs)


if __name__ == '__main__':
    main()
