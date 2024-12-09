import sys
import numpy

if len(sys.argv) != 2:
    print('Usage: python compute.py nums')
    sys.exit()
    
nums = sys.argv[1].split(', ')

for i in range(len(nums)):
    try:
        nums[i] = float(nums[i])
    except:
        nums[i] = 0 - (float(nums[i][1:]))

mean = sum(nums)/len(nums)
nums_dev_list = []
for i in range(len(nums)):
    nums_dev_list.append((nums[i] - mean) ** 2)

variance = sum(nums_dev_list) / len(nums_dev_list)

print(nums)
print(f'Mean = {mean} and standard deviation = {numpy.sqrt(variance)}')
print(len(nums))
