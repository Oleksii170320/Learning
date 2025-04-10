nums = [20,100,10,12,5,13]
res = False

min_num = min(nums)
i_min = nums.index(min_num)
c = 0
a = nums[0]

for i in range(len(nums) - 2):
    if len(nums) < 3:
        break
    else:
        if nums[i] < nums[i+1]:
            a = nums[i+1]
            c += 1
        elif nums[i] > nums[i+1]:
            a = nums[i+1]
            c = 0



print(res)
print(i_min)
