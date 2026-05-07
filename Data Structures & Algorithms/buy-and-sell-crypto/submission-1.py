class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # looking for biggest difference between two values

        max = 0
        minBuy = prices[0] # set cheapest to first day



# [10,1,5,6,7,1]
        for price in prices:
            profit = price - minBuy # current profit

            if (profit > max):
                max = profit # set max to current profit if it exceeds it

            if (price < minBuy):
                minBuy = price # set minBuy to current price if its cheapest

        # for i in range(len(prices)):
        #     for j in range(i, len(prices)):
        #         current = prices[j] - prices[i]

        #         if(current > max):
        #             max = current


            
        
        return max
