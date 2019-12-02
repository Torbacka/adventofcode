import re


def main():
    parser = re.compile("-?\d+")
    for noun in range(99):
        for verb in range(99):
            data = [int(x) for line in open("input/input.txt").readlines() for x in parser.findall(line.strip())]
            data[1] = noun
            data[2] = verb
            for i in range(0, len(data), 4):
                op_code = data[i]
                if op_code == 1:
                    output = data[data[i + 1]] + data[data[i + 2]]
                    if output == 19690720:
                        print(f"Addtion noun: {noun} verb: {verb}")
                        print(100 * noun + verb)
                    data[data[i + 3]] = output
                elif op_code == 2:
                    output = data[data[i + 1]] * data[data[i + 2]]
                    if output == 19690720:
                        print(f"Multiple noun: {noun} verb: {verb}")
                        print(100 * noun + verb)
                    data[data[i + 3]] = output
                elif op_code == 99:
                    break
                else:
                    print("Halt and catch fire!")


if __name__ == '__main__':
    main()
