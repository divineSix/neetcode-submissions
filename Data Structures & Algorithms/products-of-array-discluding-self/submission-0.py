class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        left, right, ans = [0]*N, [0]*N, [0]*N
        # l,r = 0, N-1
        lprod, rprod = 1, 1
        for idx in range(N):
            right[N-1-idx] = rprod
            left[idx] = lprod
            rprod *= nums[N-1-idx]
            lprod *= nums[idx]

        for i in range(N):
            ans[i] = left[i] * right[i]
            
        return ans
    

