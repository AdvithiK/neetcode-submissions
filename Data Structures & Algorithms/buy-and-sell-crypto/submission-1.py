class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        min_price = prices[0]

        for i in range(len(prices)):
            #find the min price
            min_price = min(min_price, prices[i])

            #calculate the profit
            profit = prices[i] - min_price

            #set new max profit
            max_profit = max(max_profit,profit)
        return max_profit
            
        