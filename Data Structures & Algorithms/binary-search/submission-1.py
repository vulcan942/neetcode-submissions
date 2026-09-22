class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,u = 0,len(nums)-1
        while l <= u:
            mid = l+(u-l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l=mid+1
            else:
                u=mid-1
        return -1