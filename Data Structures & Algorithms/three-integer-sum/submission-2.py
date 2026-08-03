class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O(n^2) solution. Two-pointer approach. 
        nums.sort()
        N = len(nums)
        ans = set()
        for idx, num in enumerate(nums): 
            # if idx > 0 and num == nums[idx-1]: # duplicate check. 
            #     continue # we've already completed all possible triplets with this number. 

            l, h = idx+1, N-1
            while l < h: 
                val = num + nums[l] + nums[h]
                if val > 0: # target is 0, so reduce nums[l]+nums[h]
                    h -= 1
                elif val < 0: # target is 0, nums[l]+nums[h] must increase
                    l += 1
                else:
                    a = (num, nums[l], nums[h]) # Why tuple? Immutability, and therefore, hashable.  
                    if a in ans: 
                        pass     
                    else: 
                        ans.add(a)
                    
                    # move it simultaneously, because we will get duplicates otherwise. 
                    l += 1
                    h -= 1

        return [list(a) for a in ans]
            