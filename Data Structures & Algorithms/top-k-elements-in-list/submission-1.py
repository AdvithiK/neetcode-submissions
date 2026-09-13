class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hash table storing num : count
        hmap = {}

        #iterate through nums and populate hash
        for i in nums:
            if i not in hmap:
                hmap[i] = 1
            else:
                hmap[i] = hmap.get(i,0) + 1
        #sort to return the k most frequent elements
        sorted_hmap = sorted(hmap.items(), key = lambda x: x[1], reverse = True)
        return[item[0] for item in sorted_hmap[:k]]


        