from collections import deque
from math import prod

from matplotlib.pyplot import ylabel
class Solution:
    def productExceptSelf(self, nums):
        output = []
        for i in range(len(nums)):
            x = nums
            print("List ------>", x)
            y = x.pop(i)
            print("Popped ------>", y)
            output.append(prod(x))
        return output

if __name__ == "__main__":
    x = Solution()
    y = [1,2,3,4]
    print(x.productExceptSelf(y))