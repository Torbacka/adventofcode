def main():
    bingo_cards_hor, bingo_cards_vert, bingo_numbers = get_bingo_cards()
    winner = set()
    for number in bingo_numbers:
        for i, bingo_cards in enumerate(bingo_cards_vert):
            # Remove numbers from vertical lines
            for bingo_line in bingo_cards_vert[i]:
                if number in bingo_line:
                    bingo_line.remove(number)
                    if len(bingo_line) == 0:
                        if i not in winner:
                            print(f"winner board {i} {sum_bingo(bingo_cards_vert[i]) * int(number)}")
                            winner.add(i)
            # Remove numbers from horizontal lines
            for bingo_line in bingo_cards_hor[i]:
                if number in bingo_line:
                    bingo_line.remove(number)
                    if len(bingo_line) == 0:
                        if i not in winner:
                            print(f"winner board {i} {sum_bingo(bingo_cards_vert[i]) * int(number)}")
                            winner.add(i)


def get_bingo_cards():
    bingo_numbers = []
    bingo_cards_vert = []
    bingo_cards_hor = []
    for i, line in enumerate(open("input/input.in").readlines()):
        if i == 0:
            bingo_numbers = line.split(",")
            continue
        if len(line) == 1:
            bingo_cards_vert.append([])
        else:
            bingo_cards_vert[-1].append([x.strip() for x in line.split(" ") if x != ''])
    for bingo_card in bingo_cards_vert:
        bingo_cards_hor.append([])
        for i in range(0, len(bingo_card)):
            bingo_cards_hor[-1].append([])
            for line in bingo_card:
                bingo_cards_hor[-1][i].append(line[i])
    return bingo_cards_hor, bingo_cards_vert, bingo_numbers


def sum_bingo(bingo_card):
    sum = 0
    for line in bingo_card:
        for number in line:
            sum += int(number)
    return sum


if __name__ == '__main__':
    main()
