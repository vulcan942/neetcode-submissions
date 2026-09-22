from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts =  defaultdict(int)
        for i in nums:
            counts[i]+=1
        counts = {k: v for k, v in sorted(counts.items(), key=lambda item: item[1],reverse=True)}

        return list(counts.keys())[:k]
