class Solution:
    def maxProfit(self, prices):
        maxP = 0
        l, r = 0, 1
         
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r +=1
        return maxP

