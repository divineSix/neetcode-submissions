class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O(n^2) solution. Two-pointer approach. 
        nums.sort()
        N = len(nums)
        ans = set()
        for idx, num in enumerate(nums): 
            # early termination. if current number is > 0, then terminate immediately. 
            if num > 0:
                break

            l, h = idx+1, N-1
            while l < h:
                val = num + nums[l] + nums[h]
                if val > 0: # target is 0, so reduce nums[l]+nums[h]
                    h -= 1
                elif val < 0: # target is 0, nums[l]+nums[h] must increase
                    l += 1
                else:
                    ans.add((num, nums[l], nums[h])) # add the triplet as a tuple so that it is hashable. 
                    # move it simultaneously, because we will get duplicates otherwise. 
                    l += 1
                    h -= 1

        return list(ans)
            