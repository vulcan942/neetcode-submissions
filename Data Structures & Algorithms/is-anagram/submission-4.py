class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False
        hm = {}
        for i in s:
            hm[i] = hm.get(i,0)+1
        
        for i in t:
            if i not in hm:
                return False
            hm[i] -= 1
            if hm[i] < 0:
                return False
        return True
