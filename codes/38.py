class Solution:
    def countAndSay(self, n: int) -> str:

        if n == 1:
            return "1"

        def count_say(n,s):
            if n == 0:
                return s


            
            y = self.countAndSay(n-1)





if __name__ == "__main__":
    n= 4
    sol = Solution()
    y = sol.countAndSay(n)
    print(y)