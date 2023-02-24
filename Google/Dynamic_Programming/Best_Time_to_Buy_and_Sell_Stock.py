class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        maximum = 0
        for price in prices:
            if price - lowest > maximum:
                maximum = price - lowest
            if lowest > price:
                lowest = price
        
        return maximum