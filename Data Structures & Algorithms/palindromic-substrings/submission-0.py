class Solution:    
    def countSubstrings(self, s: str) -> int:
        count = 0
        def expand(s,i,j):
            nonlocal count
            while i>=0 and j<len(s) and s[i]==s[j]:
                count+=1
                i-=1
                j+=1

        n = len(s)
        for i in range(n):
            odd = expand(s,i,i)
            even = expand(s,i,i+1)
        
        return count
    