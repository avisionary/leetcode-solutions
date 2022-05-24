class Solution:
    def threeSum(self, nums):
        
        output = []
        while nums:
            x = nums.pop()
            target = -x
            check = defaultdict()
            for idx, value in enumerate(nums):
                if target - value in check:
                    y = sorted([x,value,target-value])
                    if y not in output:
                        output.append(y)
                else:
                    check[value] = idx
        return output