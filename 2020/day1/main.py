import re

data = [int(line) for line in open("input/input.in").readlines()]

def main():
    b = False

    for input1 in data:
        for input2 in data:
            for input3 in data:
                if (input1 + input2 + input3) == 2020:
                    print(input1*input2)
                    b = True
                    break
            if b:
                break
        if b:
            break


if __name__ == '__main__':
    main()
