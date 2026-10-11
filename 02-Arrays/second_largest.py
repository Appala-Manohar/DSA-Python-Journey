nums = [12, 35, 1, 10, 34, 35]
largest=nums[0]
second_largest=0
for i in range(1,len(nums)):
  if nums[i]>largest:
    second_largest=largest
    largest=nums[i]
  elif nums[i]>second_largest and nums[i]!=largest:
    second_largest=nums[i]
print("Second Largest Number =",second_largest)
    
