
#Exercise 3
nums= list(range(1,5))
for i in nums:
    if i == 3:
        del nums[i:]
print(nums)
