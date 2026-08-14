class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #two pointers, binary search, find the pivot then target

        l,r = 0, len(nums)-1

        
        while l <= r:
            #calculate the middle
            middle = (l+r)//2

            if nums[middle] == target:
                return middle

            if nums[l] <= nums[middle]:
                if target > nums[middle] or target < nums[l]:
                    l = middle + 1
                else:
                    r = middle - 1
                    
            else:
                if target < nums[middle] or target > nums[r]:
                    r = middle - 1
                else:
                    l = middle + 1




        return -1

        