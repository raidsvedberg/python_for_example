from array import *

nums = array('i', [123, 45, 879, 55, 68])
for r in nums:
    print(r)
number = int(input('choose a number: '))
while number not in nums:
    number = int(input('choose correct number: '))
    if number in nums:
        print(nums.index(number))
    continue
