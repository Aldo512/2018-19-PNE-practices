import math
v = []
for n in range(51):

    h = int((1/math.sqrt(5))*(((1 + math.sqrt(5))/2)**n)+(1/2))
    v.append(h)

print(sum(v))