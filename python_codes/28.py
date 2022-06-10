class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        
        if len(needle) > len(haystack):
            return -1

        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1




if __name__ == "__main__":
    haystack = "hello"
    needle = "ll"
    sol = Solution()
    y = sol.strStr(haystack,needle)
    print(y)
