def IsPerfect(num):

    sum = 1

    for i in range(2, math.ceil(math.sqrt(num))): 
        if (num % i == 0):
            sum += i
            sum += num / i
    return sum == num

import math

for i in range(2, 500):
    if IsPerfect(i):
        print(i)
