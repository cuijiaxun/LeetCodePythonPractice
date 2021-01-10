class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 
        if len(prices)==0:return 0
        right, right_high = len(prices)-1, prices[-1]
        while right>-1:
            right_high = max(prices[right], right_high)
            max_profit = max(max_profit, right_high-prices[right])
            right -= 1
        return max_profit
