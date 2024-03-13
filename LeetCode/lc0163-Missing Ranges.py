nums = [0, 1, 3, 50, 75] 
lower = 0
upper = 99

missing = []



if len(nums) == 0:
    missing.append([lower, upper])

if nums[0] > lower:
    missing.append([lower, nums[0]-1])

for i in range(len(nums)-1):
    if nums[i+1] - nums[i] > 1:
        missing.append([nums[i]+1, nums[i+1]-1 ])

if nums[-1] < upper:
    missing.append([nums[-1]+1, upper])

print(missing)
