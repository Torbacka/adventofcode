numbers = [int(i) for i in open("input.in").read()]

sum = 0
for i, number in enumerate(numbers):
    look_up = int((len(numbers) / 2 + i)) % len(numbers)
    if number == numbers[look_up]:
        sum += number
print(sum)
