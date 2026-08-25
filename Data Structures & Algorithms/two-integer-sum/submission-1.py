class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #make a hashmap of nums -> val : index
        hashmap = {}

        for i, num in enumerate(nums):
            #if value does exist
            diff = target - num
            if diff in hashmap:
                #return the index of complement & curr
                return [hashmap[diff], i]
            else:
                #otherwise store the complement in there
                hashmap[num] = i
        return []
