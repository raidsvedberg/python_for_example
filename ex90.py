from array import *

nums = array('i', [])
while len(nums) < 5:
    value = int(input('enter a value: '))
    if 10 <= value <= 20:
        nums.append(value)
    else:
        print('outside the range')
print('thank you')
for v in nums:
    print(v)
