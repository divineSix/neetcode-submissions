class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = prices[0]
        max_p = 0
        N = len(prices)
        for i in range(1, N):
            curr_p = prices[i] - min_so_far
            max_p = max(max_p, curr_p)
            min_so_far = min(min_so_far, prices[i])
        
        return max_p