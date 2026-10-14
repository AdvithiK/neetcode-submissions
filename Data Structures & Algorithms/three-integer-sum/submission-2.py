class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        #two pointer solution
        #first sort the array
        #go through the array
        #for each i, L = i+1 and R = len(nums)-1
        #move L & R inward until solution is found, else next i
      
        #have res list store result
        res = []

        nums.sort()
        for i in range(len(nums)):
            #edge case: if all positive numbers, no 0
            if nums[i] > 0:
                break
            #edge case: skip duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            #set l and r to the indexes
            l,r = i+1, len(nums)-1
            while l < r:
                truth = nums[i] + nums[l] + nums[r]
                if truth == 0:
                    #addthe combo to res
                    res.append([nums[i], nums[l],nums[r]])
                    #reset l & r
                    l += 1
                    r -= 1
                    #skip the dupes we already saw
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

                elif truth < 0:
                    l += 1
                else:
                    r -= 1
        
        return res
    



        