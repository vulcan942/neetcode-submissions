class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        max_len = 1
        for i in range(len(nums)):
            temp = nums[i]
            temp_len=1
            while temp+1 in nums:
                temp_len+=1
                max_len=max(temp_len,max_len)
                temp+=1
        return max_len