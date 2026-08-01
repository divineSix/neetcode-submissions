class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums: 
            hashmap[num] = hashmap.get(num, 0) + 1
        
        count_list = sorted([[key,cnt] for key,cnt in hashmap.items()], key=lambda x: x[1], reverse=True) # sort by count. 
        print(count_list)
        return [item[0] for item in count_list[:k]]