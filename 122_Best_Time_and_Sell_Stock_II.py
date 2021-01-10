class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0,0
        if len(prices) == 0: return 0
        max_profit = 0
        while right<=len(prices)-1:
            while left<len(prices)-1 and prices[left]>=prices[left+1]:
                left+=1
            right = left
            while right<len(prices)-1 and prices[right+1]>=prices[right]:
                right+=1
            max_profit += prices[right]-prices[left]
            left=right
            right=left+1
        
        return max(max_profit,0)
