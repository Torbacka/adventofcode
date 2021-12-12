import re
from statistics import mean, median

parser = re.compile("-?\d+")
data = [line.strip() for line in open("input/input.in").readlines()]

points = {
    '(': 3,
    '[': 57,
    '{': 1197,
    '<': 25137,
    '}': 3,
    ')': 1,
    ']': 2,
    '>': 4

}
mapping = {
    '}': '{',
    ')': '(',
    ']': '[',
    '>': '<',
    '{': '}',
    '(': ')',
    '[': ']',
    '<': '>'
}


def main():
    error = {
        '{': 0,
        '(': 0,
        '[': 0,
        '<': 0
    }
    left = []

    for line in data:
        para = []
        corrupt = False
        for char in line:
            if char == '{' or char == '(' or char == '[' or char == '<':
                para.append(char)
            if char == '}' or char == ')' or char == ']' or char == '>':
                close = para.pop()
                if mapping[char] != close:
                    error[mapping[char]] += 1
                    corrupt = True
        if not corrupt:
            left.append([mapping[char] for char in reversed(para)])

    fun = 0
    for char, count in error.items():
        fun += points[char] * count
    print(fun)
    tot = []
    for line in left:
        fun = 0
        for char in line:
            fun *= 5
            fun += points[char]
        tot.append(fun)
    print(median(tot))


if __name__ == '__main__':
    main()
