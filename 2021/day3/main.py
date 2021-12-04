import re

parser = re.compile("-?\d+")
loop = [int(x) for line in open("input/input.in").readlines() for x in parser.findall(line.strip())]
data = [line.strip() for line in open("input/input.in").readlines()]


def main():
    zero = []
    one = []
    oxi = data.copy()
    co2 = data.copy()
    for line in data:
        if len(zero) == 0:
            for i in range(0, len(line)):
                zero.append(0)
                one.append(0)
        for i, cha in enumerate(line):
            if cha == '0':
                zero[i] += 1
            if cha == '1':
                one[i] += 1
    rate1 = ""
    rate2 = ""
    for i in range(0, len(zero)):
        if zero[i] > one[i]:
            rate1 += '0'
            rate2 += '1'
            if len(oxi) > 1:
                oxi = [line for line in oxi if line[i] == '0']
            if len(co2) > 1:
                co2 = [line for line in co2 if line[i] == '1']

        else:
            rate1 += '1'
            rate2 += '0'
            if len(oxi) > 1:
                oxi = [line for line in oxi if line[i] == '1']
            if len(co2) > 1:
                co2 = [line for line in co2 if line[i] == '0']
    print(int(rate1, 2) * int(rate2, 2))
    print(int(oxi[0], 2) * int(co2[0], 2))
    print(rate2)


def main2():
    oxi = data.copy()
    co2 = data.copy()
    for i in range(0, len(oxi[0])):
        oxi_one, oxi_zero = calculate_common(oxi)
        co2_one, co2_zero = calculate_common(co2)

        if oxi_zero[i] > oxi_one[i]:
            if len(oxi) > 1:
                oxi = [line for line in oxi if line[i] == '0']
        else:
            if len(oxi) > 1:
                oxi = [line for line in oxi if line[i] == '1']

        if co2_zero[i] > co2_one[i]:
            if len(co2) > 1:
                co2 = [line for line in co2 if line[i] == '1']
        else:
            if len(co2) > 1:
                co2 = [line for line in co2 if line[i] == '0']
    print(int(oxi[0], 2) * int(co2[0], 2))

def calculate_common(data):
    zero = []
    one = []

    for line in data:
        if len(zero) == 0:
            for i in range(0, len(line)):
                zero.append(0)
                one.append(0)
        for i, cha in enumerate(line):
            if cha == '0':
                zero[i] += 1
            if cha == '1':
                one[i] += 1
    return one, zero


if __name__ == '__main__':
    main2()
