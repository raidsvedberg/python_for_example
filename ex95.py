from array import *
import random

nums = array('f', [])
for r in range(0, 5):
    value = round(random.uniform(10, 100), 2)
    nums.append(value)
for i in nums:
    print(round(i, 2))
number = int(input('enter a number between 2 and 5: '))

const = 1
while const == 1:
    if 5 < number < 2:
        number = int(input('that is out of range. enter another number: '))
    else:
        const = 0
for v in range(0, 5):
    value = nums[v] / number
    print(round(value, 2))
