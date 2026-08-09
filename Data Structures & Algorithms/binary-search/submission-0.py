class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #split the array in half checking < or > target
        l,r = 0, len(nums) -1

        #while l does not cross r
        while l <= r:
            #calc the midpoint using L & R
            midpoint = (l+r)//2
            if nums[midpoint] < target:
                #move the l pointer up
                l = midpoint + 1
            elif nums[midpoint] > target:
                #move the r pointer down
                r = midpoint - 1
            else:
                #target found
                return midpoint  
        return -1