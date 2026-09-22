class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_len = 0
        char_set = set()
        for end in range(len(s)):
            while s[end] in char_set:
                char_set.remove(s[start])
                start+=1
            char_set.add(s[end])
            max_len = max(max_len,end-start+1)
        
        return max_len
            

