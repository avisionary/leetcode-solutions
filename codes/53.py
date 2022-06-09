class Solution:
    def maxSubArray(self, nums) -> int:
        max_sum = nums[0]
        prev = max_sum

        for i in range(1,len(nums)):
            res = max(nums[i]+prev,nums[i])
            max_sum = max(res,max_sum)
            prev = res

        return max_sum




if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    sol = Solution()
    z = sol.maxSubArray(nums)
    print(z)