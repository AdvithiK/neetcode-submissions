class Solution:
    def rob(self, nums: List[int]) -> int:
        #return the max of either the first value, everything but the first value or everything but the last value
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self,nums):
        rob1,rob2 = 0,0

        for num in nums:
            newrob = max(rob1+num, rob2)
            rob1 = rob2
            rob2 = newrob
        return rob2
        