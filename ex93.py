from array import *

nums = array('i', [])
for r in range(0, 5):
    num = int(input('enter a num: '))
    nums.append(num)
nums = sorted(nums)
for i in nums:
    print(i)
delete = int(input('enter a num to delete: '))
nums.remove(delete)
new_nums = array('i', [])
new_nums.append(delete)
new_nums = sorted(new_nums)
print(nums)
print(new_nums)
