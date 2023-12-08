import re
from collections import Counter
from functools import cmp_to_key


def sort(hand1, hand2):
    grouped1 = Counter(replace2(hand1[0]))
    grouped2 = Counter(replace2(hand2[0]))
    hand_score1 = calculate_hand(grouped1)
    hand_score2 = calculate_hand(grouped2)
    if hand_score1 == hand_score2:
        for i, c in enumerate(hand1[0]):
            if c != hand2[0][i]:
                return -(ord(hand2[0][i]) - ord(c))
    return hand_score1 - hand_score2


def calculate_hand(grouped_hand):
    values = grouped_hand.values()
    if 5 in values:
        return 6
    elif 4 in values:
        return 5
    elif 3 in values and 2 in values:
        return 4
    elif 3 in values:
        return 3
    elif 2 in Counter(values).values():
        return 2
    elif 2 in values:
        return 1
    return 0


def replace2(hand):
    if '*' in hand:
        common = Counter(hand).most_common()
        most_common_non_joker = 0
        if common[0][0] == '*':
            most_common_non_joker = 1
        if common[0][1] == 5:
            return 'AAAAA'
        return hand.replace('*', common[most_common_non_joker][0])
    return hand


parser = re.compile("-?\d+")
data = [(line.strip().split()[0]
         .replace('A', 'E')
         .replace('T', 'A')
         .replace('J', '*')
         .replace('Q', 'C')
         .replace('K','D'),
         int(line.strip().split()[1])) for line in open("input/input.in").readlines()]
sum = 0
l = sorted(data, key=cmp_to_key(sort))
for i, data in enumerate(l, 1):
    sum += i * data[1]
print(sum)
