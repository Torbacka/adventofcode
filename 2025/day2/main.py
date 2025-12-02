import re

parser = re.compile(r"-?\d+")
data =  open("input/input.in").read()
invalid_numbers = 0
for d in data.split(","):
    range_start = int(d.split("-")[0])
    range_stop = int(d.split("-")[1])
    for n in range(range_start,range_stop +1):
        string_number = str(n)
        if len(string_number) % 2 != 0:
            continue

        if string_number[:len(string_number)//2 + len(string_number)%2] ==  string_number[len(string_number)//2 + len(string_number)%2:]:

            invalid_numbers += n
            print(f"{d} has invalid ID")



print(invalid_numbers)
