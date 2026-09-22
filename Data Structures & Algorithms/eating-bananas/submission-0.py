class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,u = 1 , max(piles)
        res = u

        while l<=u:
            k = (l+u)//2
            totalTime = 0

            for p in piles:
                totalTime += math.ceil(float(p) / k)

            if totalTime <= h:
                res=k
                u = k - 1
            else:
                l=k+1
        return res

