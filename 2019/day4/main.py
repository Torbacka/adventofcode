import re

parser = re.compile("\d+")
data = [int(x) for line in open("input/input.txt").readlines() for x in parser.findall(line.strip())]


def main():
    found = 0
    for i in range(data[0], data[1]):
        if finding_passwords(i):
            found += 1
            print(i)
    print(found)


def finding_passwords(i):
    numbers = list(str(i))
    double = False
    decreasing = True
    for n in range(len(numbers) - 1):
        if numbers[n] <= numbers[n + 1]:
            if numbers[n] == numbers[n + 1]:
                if n - 1 >= 0 and numbers[n - 1] == numbers[n]:
                    continue
                if n + 2 < len(numbers) and numbers[n + 2] == numbers[n]:
                    continue
                double = True
        else:
            decreasing = False

    if double and decreasing:
        return True
    return False


if __name__ == '__main__':
    main()
