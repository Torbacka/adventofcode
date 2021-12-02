import re

parser = re.compile("-?\d+")
data = open("input/input.in").read()


def calc_score(player):
    sum = 0
    for i, number in enumerate(reversed(player)):
        sum += number * (i + 1)
    return sum

def calc_unq(player):
    sum = 0
    for i, number in enumerate((player)):
        sum += number * (i + 1)
    return sum


def game(player1, player2):
    rounds = set()
    while len(player1) > 0 and len(player2) > 0:
        stand = (calc_unq(player1), calc_unq(player2))
        if stand in rounds:
            return [34], []
        else:
            rounds.add(stand)
        card1 = player1.pop(0)
        card2 = player2.pop(0)
        if card1 <= len(player1) and card2 <= len(player2):
            subplayer1, subplayer2 = game(player1[:card1], player2[:card2])
            if len(subplayer1) > len(subplayer2):
                player1.append(card1)
                player1.append(card2)
            else:
                player2.append(card2)
                player2.append(card1)
        else:
            if card1 > card2:
                player1.append(card1)
                player1.append(card2)
            else:
                player2.append(card2)
                player2.append(card1)

    return player1, player2


player1 = [int(number) for number in data.split("\n\n")[0].split("\n")[1:]]
player2 = [int(number) for number in data.split("\n\n")[1].split("\n")[1:]]
player1, player2 = game(player1, player2)

print(calc_score(player1) if len(player1) > 0 else calc_score(player2))
