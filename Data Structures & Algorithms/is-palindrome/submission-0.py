class Solution:
    def isPalindrome(self, s: str) -> bool:
        # a = s.replace(" ", "").lower()
        a = "".join([c for c in s if c.isalnum()]).lower()
        a1,a2 = 0,len(a)-1
        while a1 <= a2: 
            if a[a1] != a[a2]:
                return False
            else:
                a1 += 1
                a2 -= 1
        
        return True