from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        d1 = defaultdict(int)

        for i in range(len(s)):
            d1[s[i]] += 1
            d1[t[i]] -= 1
        
        for char in d1:
            if d1[char] != 0:
                return False
        
        return True