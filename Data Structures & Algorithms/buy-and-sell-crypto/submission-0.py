class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #sliding window problem

        min_price = prices[0]
        max_price = 0

        for i in range(len(prices)):
            #find the minimum 
            min_price = min(min_price, prices[i])

            #calculate the current profit
            profit = prices[i] - min_price

            #find the maximum profit
            max_price = max(max_price, profit)
        return max_price



        