class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def func(i, c, t):
            if t == target:
                res.append(c[:])
                return
            
            if t > target or i >= len(nums):
                return 
            # add the candidate to the current
            c.append(nums[i])
            func(i, c, t + nums[i])
            
            # skip the candidate
            c.pop()
            func(i+1, c, t)
            return res

        return func(0, [], 0)