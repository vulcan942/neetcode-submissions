class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = defaultdict(int)
        for i in nums:
            counts[i]+=1
            if counts[i] > 1:
                return True
        return False