class Solution:
    def firstMissingPositive(self, nums) -> int:
        nums = set(nums)
        x = max(nums)
        if x<0:
            return 1
        if x == len(set(nums))  and min(nums)>0:
            return x+1
        
        
        for i in range(1,x):
            if i not in nums:
                return i
        return x+1