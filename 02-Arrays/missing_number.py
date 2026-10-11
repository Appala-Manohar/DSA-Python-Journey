class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        expected_num=n*(n+1)//2
        original_sum=sum(nums)
        return expected_num - original_sum
nums=[3,0,1]
sol=Solution()
missing_number=sol.missingNumber(nums)
print(missing_number)
