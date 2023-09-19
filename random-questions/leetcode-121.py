# Best Time to Buy and Sell a stock
# Start 10:20 pm - 10:46 pm - ran into issues
class Solution:
    def maxProfit(self,prices):
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit

sol = Solution()
print(sol.maxProfit([2,1,2,1,0,1,2]))