class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm={}
        for i in nums:
            if i in hm:
                return True
            else:
                hm[i]=1
        return False
        
