class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs: 
            key = "".join(sorted(s)) # sorted string as key
            hashmap[key] = hashmap.get(key, []) + [s]
        
        return list(hashmap.values())
