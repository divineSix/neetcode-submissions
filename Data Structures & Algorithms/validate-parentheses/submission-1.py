class Solution:
    def isValid(self, s: str) -> bool:
        _OPEN = set(["(", "{", "["])
        _CLOSE = set([")", "}", "]"])
        pairs = {")": "(", "}": "{", "]": "["}
        stack = []
        for c in s:
            if c in _OPEN: 
                stack.append(c)
            else: # c in _CLOSE
                if len(stack) == 0: # stack was empty when close bracket came, so false. 
                    return False
                elif stack[-1] == pairs[c]:
                    stack.pop()
                else: # mis-matched bracket, pattern fails. 
                    return False
        
        if len(stack) > 0:
            return False
        else:
            return True