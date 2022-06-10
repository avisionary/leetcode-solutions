class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        res = ""
        res_len = 0

        def is_palin(s,left,right,res_len,res):
            while left >= 0 and right <len(s) and s[left] == s[right]:
                if right-left +1 > res_len:
                    res = s[left:right+1]
                    res_len = right-left+1
                left = left -1
                right = right + 1
            return res,res_len
            
        for i in range(len(s)):
            # odd
            left = i
            right = i
            res,res_len = is_palin(s,left,right,res_len,res)
            # even
            left = i
            right = i+1
            res,res_len = is_palin(s,left,right,res_len,res)
            
        return res
        








if __name__ == "__main__":
    s = "aacabdkacaa"
    sol = Solution()
    y = sol.longestPalindrome(s)
    print(y)