data = {i: {"line": line.strip(), "copies": 1} for i, line in enumerate(open("input/input.in").readlines())}
part1 = 0
for i, line in data.items():
    lottery, winning_numbers = line["line"].split(":")[1].strip().split(" | ")
    winning_numbers = set(int(winning.strip()) for winning in winning_numbers.strip().split(" ") if winning != '')
    lottery = set(int(lot.strip()) for lot in lottery.strip().split(" ") if lot != '')
    wins = len(winning_numbers & lottery)
    if wins > 0:
        part1 += 2**(wins-1)
    for m in range(i+1, i+1+wins):
        data[m]['copies'] += 1*data[i]['copies']

print(part1)
print(sum([line['copies'] for _, line in data.items()]))
