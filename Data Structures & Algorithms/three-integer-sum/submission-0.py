class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #pick a num a, then do two sum using L & R pointers

        #list to store the result
        res = []
        #sort the original array
        nums.sort()

        for i, a in enumerate(nums):
            #don't reuse the same value consecutively 
            if i > 0 and a == nums[i-1]:
                continue
            
            #set the L pointer to be after a, and R pointer at the end
            l,r = i + 1, len(nums)-1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                #if total is greater than 0, decrease (move r down)
                if threeSum > 0:
                    r -= 1
                #if total is less than 0, increase (move l up)
                elif threeSum < 0:
                    l += 1
                #if we find 3 nums that equal 0, append to res
                else:
                    res.append([a, nums[l], nums[r]])
                #move the left pointer continously until it's not a dupe
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res


        