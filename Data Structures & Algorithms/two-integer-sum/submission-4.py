class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #it is not sorted ! return the indicies
        #make a hashmap of value:index
        hashmap = {}

        #i -> index, num is value
        for i, num in enumerate(nums):
            #find the complement
            diff = target - num
            if diff in hashmap:
                #return the index at the complement and curr index
                return [hashmap[diff], i]
            else:
                hashmap[num] = i
        return []

        