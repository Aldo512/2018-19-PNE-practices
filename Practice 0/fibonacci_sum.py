import math

usr = int(input('Introduce the nth fibonacci number to be calculated: '))
v = []

for n in range(usr):

    h = int((1/math.sqrt(5))*(((1 + math.sqrt(5))/2)**n)+(1/2))
    v.append(h)
    print(h)

print('this is the total sum of all the fibonacci numbers requested: ', sum(v))