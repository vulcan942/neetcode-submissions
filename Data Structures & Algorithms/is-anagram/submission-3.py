class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s = sorted(list(s))
        t = sorted(list(t))

        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True

