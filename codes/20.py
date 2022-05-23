from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s)%2 == 1:
            return False


        s = list(s)
        bracks = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack= deque()

        for x in s:
            print(x)
            if x not in bracks:
                print(x)
                stack.append(x)
            else:
                if len(stack) == 0:
                    return False
                if stack.pop() != bracks[x]:
                    return False


        if len(stack) > 0:
            return False
        
        return True