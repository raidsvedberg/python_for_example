from array import *
import random

nums_user = array('i', [])
nums = array('i', [])
for i in range(0, 3):
    value = int(input('enter a value: '))
    nums_user.append(value)
for v in range(0, 5):
    val = random.randint(0, 100)
    nums.append(val)
print(nums, nums_user)
nums_user.extend(nums)
nums_user = sorted(nums_user)
for i in nums_user:
    print(i)
