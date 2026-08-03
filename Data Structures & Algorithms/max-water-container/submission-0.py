class Solution:
    def maxArea(self, heights: List[int]) -> int:
        N = len(heights)
        l, h = 0, N-1
        max_vol = -1000
        while l < h:
            a = (h-l)*min(heights[l], heights[h])
            max_vol = max(a, max_vol)
            
            if heights[l] < heights[h]:
                l += 1
            else:
                h -= 1
        
        return max_vol