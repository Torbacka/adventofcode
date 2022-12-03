def sum_elf(elf):
    return sum(int(num) for num in elf.split('\n'))


data = [sum_elf(elf) for elf in open("input/input.in").read().split('\n\n')]
data.sort(reverse=True)
print(data)
print(sum(data[:3]))
