
from typing import List
class Solution:
    def maxProfit(self, prices:List[int])->int:
        l, r = 0,1 #Left is buy and right is sell
        maxP = 0
        while r < len(prices):
            if prices[l]<prices[r]:
                profit = prices[r] - prices[l]
                maxP= max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP
prices = [3,5,1,7,9,4]
solution = Solution()
ans =solution.maxProfit(prices)
print(ans)