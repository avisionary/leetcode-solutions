
# Need to do memoization


class Solution:
    def fib(self, n: int, memo = {}) -> int:
        if (n in memo):
            return memo[n]
        if n==1 or n==2:
            return 1
        elif n==0:
            return 0
        else:
            memo[n] =  self.fib(n-1,memo) + self.fib(n-2,memo)
            return memo[n]



if __name__ == "__main__":
    n = 9
    sol = Solution()
    z = sol.fib(n)
    print(z)