import re

parser = re.compile("-?\d+")
data = [line.strip().split(" | ") for line in open("input/input.in").readlines()]

unqiue = {
    2: 1,
    4: 4,
    3: 7,
    7: 8
}




def main():
    print(data)
    hashed_numbers = {
        str(sorted([1, 2, 7, 5, 4])): 2,
        str(sorted([1, 2, 7, 3, 4])): 3,
        str(sorted([1, 6, 7, 3, 4])): 5,
        str(sorted([1, 6, 7, 3, 4, 5])): 6,
        str(sorted([1, 2, 3, 4, 6, 7])): 9,
        str(sorted([1, 2, 3, 4, 5, 6])): 0
    }
    count = 0
    for first, second in data:
        display = generate_display(first)
        display = {v: k for k, v in display.items()}
        numbers = ''
        for number in second.split(" "):
            segments = []
            if len(number) in unqiue:
                numbers += str(unqiue[len(number)])
            else:
                for c in number:
                    segments.append(display[c])
                numbers += str(hashed_numbers[str(sorted(segments))])
        count += int(numbers)
    print(count)


def generate_display(first):
    display = {
        1: None,
        2: None,
        3: None,
        4: None,
        5: None,
        6: None,
        7: None,
    }
    pattern = first.split(" ")
    pattern = sorted(pattern, key=len)
    display[2] = pattern[0]
    display[3] = pattern[0]
    display[1] = set(pattern[1]).difference(set(pattern[0])).pop()
    all_len_six = list(filter(lambda x: len(x) == 6, pattern))
    display[7] = find_middle_rod(pattern[2], pattern[0], all_len_six)
    display[6] = set(pattern[2]).difference(set(pattern[0])).difference(set(display[7])).pop()
    display[6] = set(pattern[2]).difference(set(pattern[0])).difference(set(display[7])).pop()
    pos_five, pos_four = find_lower_corner(display, pattern[-1], all_len_six)
    display[5] = pos_five
    display[4] = pos_four
    display[2] = set(pattern[-1]).difference(filter_out_6(all_len_six, display[2])[0]).pop()
    display[3] = set(display[3]).difference(set(display[2])).pop()
    return display


def find_lower_corner(display, eight, all_number_six):
    found_number = set()
    for value in display.values():
        if value:
            found_number.update(set(value))
    nine_and_zero = filter_out_9_and_0(all_number_six, display[2])
    corner = set(eight).difference(found_number)
    for number in nine_and_zero:
        difference = corner.difference(number)
        if len(difference) == 1:
            pos_five = difference.pop()
            return pos_five, corner.difference(set(pos_five)).pop()
    return None


def find_middle_rod(four, one, all_numbers_six):
    number_set = filter_out_9_and_0(all_numbers_six, one)
    for n_set in number_set:
        diff = set(four).difference(n_set)
        if len(diff) == 1:
            return diff.pop()
    return None


def filter_out_9_and_0(all_numbers_six, one):
    number_set = []
    for number in all_numbers_six:
        difference = set(number).difference(set(one))
        if len(difference) == 4:
            number_set.append(difference.union(one))
    return number_set


def filter_out_6(all_numbers_six, one):
    number_set = []
    for i, number in enumerate(all_numbers_six):
        difference = set(number).difference(set(one))
        if len(difference) == 5:
            number_set.append(difference.union(number))
    return number_set


if __name__ == '__main__':
    main()
