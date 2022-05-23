class Solution:
    def twoSum(self, nums, target: int):
        
        check = defaultdict()
        
        for idx, value in enumerate(nums):
            if (target - value) in check:
                return [idx , check[target-value]]
            else:
                check[value] = idx
                