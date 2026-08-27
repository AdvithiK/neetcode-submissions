class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #have a hashmap num : count
        #if hashmap[num] has one count already, return false
        #else return true
        hmap = {}

        for num in nums:
            if num in hmap:
                return True
            else:
                hmap[num] = 1
        return False