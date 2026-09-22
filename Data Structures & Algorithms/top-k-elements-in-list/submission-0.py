class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for i in nums:
            if i in hmap:
                hmap[i]+=1
            else:
                hmap[i]=1
        
        sorted_hmap = [item[0] for item in sorted(hmap.items(),key=lambda item: item[1])]
        print(sorted_hmap)
        return sorted_hmap[-k:]