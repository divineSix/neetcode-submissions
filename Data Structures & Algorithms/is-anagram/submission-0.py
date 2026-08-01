class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = defaultdict(int)
        for c in s:
            hashmap[c] += 1
        
        for c in t:
            hashmap[c] -= 1
        
        valsum = any(hashmap.values())
        return True if valsum == 0 else False