class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s)-1
        
        def recfunc(s,left,right):
            if left <= right:
                s[left],s[right] = s[right],s[left]
                recfunc(s,left+1,right-1)

        recfunc(s,left,right)
        return s


if __name__ == "__main__":
    s = ["h","e","l","l","o"]
    sol = Solution()
    y = sol.reverseString(s)
    print(y)
        