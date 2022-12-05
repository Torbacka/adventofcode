from math import sqrt

data = 325489



sum = 0
squares = []

for i in range(1, int(sqrt(data))):
    squares.append(int(pow(i, 2))+1)
print(squares)