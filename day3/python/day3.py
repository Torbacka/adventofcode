from collections import defaultdict
import re
import json

data = open('input.txt')
claims = map(lambda s: map(int, re.findall(r'-?\d+', s)), data)
for (claim_id, x, y, width, height) in claims:
    print("%s, %s, %s, %s, %s" % (claim_id, x,y ,width, height) )
