from collections import deque
from math import prod
import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        z = re.compile(p)
        x = z.search(s)
        if x:
            return True
        else:
            return False

if __name__ == "__main__":
    x = Solution()

    s = "aa"
    z = "a*"

    print(x.isMatch(s,z))