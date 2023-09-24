class Solution:
    def maxProfit(self, prices):
        l,r = 0,0
        n=len(prices)
        curProfit, maxProfit = 0, 0
        while l<n and r<n:
            curProfit = prices[r] - prices[l]
            if curProfit < 0:
                curProfit -= prices[l]
                l+=1
            else:
                r += 1
            maxProfit = max(curProfit, maxProfit)
        return maxProfit



print(Solution().maxProfit([7,1,5,3,6,4]))