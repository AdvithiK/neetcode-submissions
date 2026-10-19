class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}

        #populate the hmap to be element : count
        for num in nums:
            #append the count if it exists in hmap
            if num in hmap:
                hmap[num] = 1 + hmap.get(num,0)
            #else create it in the hmap
            else:
                hmap[num] = 1
        
        #sort the hmap descending order
        sorted_map = sorted(hmap.items(), key = lambda x:x[1], reverse=True)

        #return the k first values
        return[item[0] for item in sorted_map[:k]]
        