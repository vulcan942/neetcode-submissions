class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hm = {}
        for i in s:
            hm[i] = hm.get(i,0)+1
        
        for j in t:
            if j in hm:
                hm[j]-=1
                if hm[j]==-1:
                    return False
            else:
                return False
        return True
