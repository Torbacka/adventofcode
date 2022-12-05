import re


def parse_crates():
    crates = None
    for line in open("input.in").readlines():
        if crates is None:
            crates = []
            counter = 1
            for char_pos in range(len(line)):
                if counter == 4:
                    crates.append([])
                    counter = 0
                counter += 1
        crate_str = ''
        for i, char in enumerate(line):
            if char == '[':
                crate_str += char
            elif char == ']':
                crate_str += char

                pos = 0
                tmp_i = i
                if 0 == i - 2:
                    pass
                else:
                    tmp_i -= 2
                    for n in range(20):
                        if 0 <= tmp_i - 4:
                            pos += 1
                        tmp_i -= 4
                crates[pos].append(crate_str)
                crate_str = ''
            elif len(crate_str) > 0:
                crate_str += char
    return crates


crates = parse_crates()
moves = [list(map(int, re.findall("-?\d+", line))) for line in open("input2.in").readlines()]
print(crates)
for line in moves:
    move = []
    for _ in range(line[0]):
        move.append(crates[line[1] - 1].pop(0))
    crates[line[2] - 1][:0] = move
    print(crates)

str = ''
for crate in crates:
    if len(crate) >0:
        str += crate[0]
print(str)