data = [line.strip() for line in open("input.in").readlines()]

cycle = 0
register = 1
answer = 0
crt_row = ''
rows = []


def prog_cycle(answer, cycle):
    global crt_row
    cycle += 1
    if cycle % 40 == register or cycle % 40 == register + 1 or cycle % 40 == register + 2:
        crt_row += "#"
    else:
        crt_row += "."
    if cycle % 40 == 20:
        answer += register * cycle
    elif cycle % 40 == 0:
        rows.append(crt_row)
        crt_row = ''
    return answer, cycle


for line in data:
    command = line.split(" ")
    if command[0] != "noop":
        if command[0] == "addx":
            answer, cycle = prog_cycle(answer, cycle)
            answer, cycle = prog_cycle(answer, cycle)
            register += int(command[1])
            continue
    answer, cycle = prog_cycle(answer, cycle)
for line in rows:
    print(line)
