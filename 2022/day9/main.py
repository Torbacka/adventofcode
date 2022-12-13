data = [line.strip() for line in open("input.in").readlines()]

cycle = 0
register = 1
answer = 0
crt_row = ''
rows = []
for line in data:
    command = line.split(" ")
    if command[0] != "noop":
        if command[0] == "addx":
            cycle += 1
            if cycle%40 == register or cycle%40 == register + 1 or cycle%40 == register + 2:
                crt_row += "#"
            else:
                crt_row += "."
            if cycle % 40 == 20:
                answer += register * cycle
            elif cycle % 40 == 0:
                rows.append(crt_row)
                crt_row = ''
            cycle += 1
            if cycle%40 == register or cycle%40 == register + 1 or cycle%40 == register + 2:
                crt_row += "#"
            else:
                crt_row += "."
            if cycle % 40 == 20:
                answer += register * cycle
            elif cycle % 40 == 0:
                rows.append(crt_row)
                crt_row = ''
            register += int(command[1])
            continue
    cycle += 1
    if cycle%40 == register or cycle%40 == register + 1 or cycle%40 == register + 2:
        crt_row += "#"
    else:
        crt_row += "."
    if cycle % 40 == 20:
        answer += register * cycle
    elif cycle % 40 == 0:
        rows.append(crt_row)
        crt_row = ''
for line in rows:
    print(line)
