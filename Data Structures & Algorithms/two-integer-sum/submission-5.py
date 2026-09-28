class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #hashmap with num:index
        hmap = {}

        for i,num in enumerate(nums):
            #compute the diff
            diff = target - num

            if diff in hmap:
                return [hmap[diff],i]
            else:
                hmap[num] = i
        return []
         
        