import re

parser = re.compile("\d+")


def solve(a1,a2,b1,b2,c1,c2):
    # Cramer's rule
    i, j, k = a1*b2-a2*b1, c1*b2-c2*b1, a1*c2-a2*c1
    return 0 if j%i or k%i else  3*j//i + k//i


sum = 0
sum2 = 0
for machine in open('input/input.in').read().split('\n\n'):
    a1,a2,b1,b2,c1,c2 = map(int, re.findall(r'\d+', machine))
    sum += solve(a1,a2,b1,b2,c1,c2 )
    sum2 += solve(a1,a2,b1,b2,c1+10000000000000,c2+10000000000000 )


print(sum)
print(sum2)
