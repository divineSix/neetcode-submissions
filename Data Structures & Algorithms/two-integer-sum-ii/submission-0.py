class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        N = len(numbers)
        l,h = 0,N-1
        while l < h:
            diff = target - (numbers[l] + numbers[h])
            if diff == 0:
                return [l+1, h+1] # return is 1-indexed
            elif diff > 0: 
                l += 1
            else:
                h -= 1