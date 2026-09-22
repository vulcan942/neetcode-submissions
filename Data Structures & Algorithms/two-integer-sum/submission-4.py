class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            idx = target-nums[i]
            if idx in hm:
                return [hm[idx],i]
            else:
                hm[nums[i]]=i
