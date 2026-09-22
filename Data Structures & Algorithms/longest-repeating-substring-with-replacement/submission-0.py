class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_set = {}
        start = 0
        max_frequency = 0

        for end in range(len(s)):
            char_set[s[end]] = 1 + char_set.get(s[end],0)
            max_frequency = max(max_frequency,char_set[s[end]])

            if (end-start+1)- max_frequency > k:
                char_set[s[start]]-=1
                start+=1
            
        return end-start+1