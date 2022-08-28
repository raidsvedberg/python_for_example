from array import *

nums = array('i', [])
for r in range(0, 5):
    newnum = int(input('enter a value: '))
    nums.append(newnum)

nums = sorted(nums)
nums.reverse()
print(nums)
