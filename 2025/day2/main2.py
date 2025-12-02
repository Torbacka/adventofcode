import re

parser = re.compile(r"-?\d+")
data =  open("input/input.in").read()
invalid_numbers = set()
for d in data.split(","):
    range_start = int(d.split("-")[0])
    range_stop = int(d.split("-")[1])
    for n in range(range_start,range_stop +1):
        string_number = str(n)
        for m in range(1, len(string_number)//2 +1):
            if len(string_number)%m != 0:
                continue
            found_matches = 0
            for o in range(0, len(string_number)//m - 1):
                if string_number[o*m:m + o*m] ==  string_number[m + o*m:m*2 + o*m]:
                    found_matches += 1
            if found_matches == len(string_number)//m -1:
                invalid_numbers.add(n)
                print(f"{d} has invalid ID, {n}")



print(sum(invalid_numbers))
