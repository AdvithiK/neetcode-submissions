class Solution:
    def rob(self, nums: List[int]) -> int:
        #edge case: if only one house
        if len(nums) == 1:
            return nums[0]
        
        def helper(nums):
            rob1,rob2 = 0,0

            for num in nums:
                newrob = max(rob1+num, rob2)
                rob1 = rob2
                rob2 = newrob
            return rob2
        #return the max of everything but the first value or everything but the last value
        return max(helper(nums[1:]), helper(nums[:-1]))
        