from collections import deque
from unicodedata import digit


class Solution:
    def plusOne(self, digits):

        number = 0
        mul = 1
        digits = deque(digits)

        while digits:
            x = digits.pop()
            number = number + x*mul
            mul = mul*10

        number = int(number+1)
        ans = [int(a) for a in str(number)]
        return ans






if __name__ == "__main__":
    digits = [6,1,4,5,3,9,0,1,9,5,1,8,6,7,0,5,5,4,3]
    sol = Solution()
    x = sol.plusOne(digits)
    print(x)