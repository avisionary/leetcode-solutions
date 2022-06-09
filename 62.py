class Solution:
    def uniquePaths(self, m: int, n: int,memo = {}) -> int:
        key = (m,n)
        if key in memo:
            return memo[key]
        if m == 1 or n == 1:
            return 1
        elif m == 0 or n == 0:
            return 0
        memo[key] = self.uniquePaths(m-1,n) + self.uniquePaths(m,n-1)
        memo[(n,m)] = memo[key]
        return memo[key]


if __name__ == "__main__":
    m = 3
    n = 7
    sol = Solution()
    z = sol.uniquePaths(m,n)
    print(z)