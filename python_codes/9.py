class Solution:
    def isPalindrome(self, x: int) -> bool:
        s_x = str(x)        
        q = deque(s_x)
        while len(q)>1:
            if q.popleft() == q.pop():
                pass
            else:
                return False
        return True