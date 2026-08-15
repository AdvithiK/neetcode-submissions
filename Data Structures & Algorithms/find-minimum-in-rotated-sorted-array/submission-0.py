class Solution:
    def findMin(self, nums: List[int]) -> int:
        #binary search

        l, r = 0, len(nums)-1

        #set dummy minimum
        minimum = nums[l]

        #compare middle to l & r
        while l <= r:
        
            middle = (l+r)//2

            #check for if minimum is l pointer:
            if nums[l] < nums[r]:
                minimum = min(minimum, nums[l])
                break
            
            #set minimum to either curr minimum or middle
            minimum = min(minimum, nums[middle])
            #search the right half
            if nums[middle] >= nums[l]:
                l += 1

            #search the left half
            else:
                r -= 1
        return minimum



        