class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = s.lower()
        s_x = re.sub(r"[^0-9a-zA-Z]","",x)
        q = deque(s_x)
        while len(q)>1:
            if q.popleft() == q.pop():
                pass
            else:
                return False
        return True