class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # looking for biggest difference between two values

        max = 0

        for i in range(len(prices)):
            for j in range(i, len(prices)):
                current = prices[j] - prices[i]

                if(current > max):
                    max = current
            
        
        return max
