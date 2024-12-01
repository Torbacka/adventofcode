import re

parser = re.compile("-?\d+")
data = [int(x) for line in open("input/input.in").readlines() for x in parser.findall(line.strip())]

def main():
    print(pairs)


if __name__ == '__main__':
    main()
