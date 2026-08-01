class Solution:

    def encode(self, strs: List[str]) -> str:
        delim = "§"
        ans = ""
        for s in strs: 
            ans += f"{len(s)}{delim}{s}"
        print(ans)
        return ans

    def decode(self, s: str) -> List[str]:
        delim = "§" # non-ascii delimiter
        N = len(s)
        i = 0
        ans = []
        num = "" # init
        while i < N: 
            # check if char is digit, add to num_str only if next one is also digit. If any non-digit chars come, break that. and move on. 
            # delim 
            # convert to int, read the string directly, skip to the next char. 
            
            if s[i].isdigit():
                num += s[i]
                i += 1
            elif s[i] == delim:
                length = int(num)
                ans.append(s[i+1:i+1+length])
                i += 1+length
                num = ""
            else:
                num = ""
                i += 1

        return ans