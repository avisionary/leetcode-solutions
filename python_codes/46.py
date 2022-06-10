from collections import deque
import itertools

nums = [1,2,3]

# perm = itertools.permutations(nums)

# s=[]
# for i in list(perm):
#     s.append(i)
# print(s)


class Solution:
    def permute(self, nums):
        result = []

        # base case
        if len(nums) == 1:
            return [nums.copy()]

        for i in range(len(nums)):
            x = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(x)
            result.extend(perms)
            nums.append(x)
        return result