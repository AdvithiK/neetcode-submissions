class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #hashmap to get a count of all numbers
        hmap = {}
        #loop through nums to populate hashmap & check dupes
        for i in nums:
            #if there exists an occurance, there is a dupe
            if i in hmap and hmap[i] >=1:
                return True
            hmap[i] = hmap.get(i,0)+1
        return False
        

        