class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i =0
        max_s = 0
        d1 = deque()
        while i < len(s):
            while (s[i] in d1):
                d1.popleft()
            d1.append(s[i])
            max_s = max(max_s,len(d1))
            i = i+1
        return max_s