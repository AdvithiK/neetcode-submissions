class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        #initialize the prefix
        prefix = 1
        #loop through nums
        for i in range(len(nums)):
            #store prev accumulated prefix in respective index 
            output[i] = prefix
            prefix *= nums[i]
        #initialize postfix 
        postfix = 1
        #loop from back to front
        for i in range(len(nums)-1, -1, -1):
            #multiple everything after the index and store in respective index
            output[i] *= postfix
            postfix *= nums[i]
        return output


        
        