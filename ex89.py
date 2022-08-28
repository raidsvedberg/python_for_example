from array import *
import random

nums = array('i', [])
for r in range(0, 5):
    value = random.randint(0, 100)
    nums.append(value)
for v in nums:
    print(v)
