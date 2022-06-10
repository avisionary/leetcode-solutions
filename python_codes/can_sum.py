class Solution:
    def canSum(self,target,nums,memo = {}):
        if target in memo:
            return memo[target]
        if target == 0:
            return True
        elif target < 0:
            return False
        
        for num in nums:
            rem = target - num
            if self.canSum(rem,nums) == True:
                memo[target] = True
                return True

        memo[target] = False
        return False

        


if __name__ == "__main__":
    target = 300
    nums = [2,3,5,7]
    sol = Solution()
    z = sol.canSum(target,nums)
    print(z)