class Solution:
    def maxProfit(self, prices) -> int:
        l = 0
        r = 1
        d = deque(prices)
        maxP = 0
        while r<len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else: 
                l = r
            r = r+1
        return maxP
        