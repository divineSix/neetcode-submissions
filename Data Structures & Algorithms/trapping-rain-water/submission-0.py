class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        prefix_max, suffix_max = [0]*N, [0]*N

        pre_max, suf_max = 0, 0
        for idx in range(N): 
            prefix_max[idx] = pre_max
            suffix_max[N-1-idx] = suf_max
            pre_max = max(height[idx], pre_max) # for next iteration
            suf_max = max(height[N-1-idx], suf_max) # for next iteration
        
        # Compute water trapped at element[i]
        # print(f"[DEBUG] Prefix: {prefix_max}")
        # print(f"[DEBUG] Suffix: {suffix_max}")
        # print(f"[DEBUG] Height: {height}")
        total_water = 0
        for idx in range(N):
            min_height = min(prefix_max[idx], suffix_max[idx])
            total_water += max(min_height - height[idx], 0)
        
        return total_water