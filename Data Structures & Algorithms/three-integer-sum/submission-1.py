class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #two pointer with 1 num fixed and the other two have pointers

        #list to store resulting triplets
        res = []

        #sort the array
        nums.sort()

        for i in range(len(nums)):
            #fixed number a (num 1)
            a = nums[i]
            #edge case: if all positive numbers, no way to 0
            if a > 0:
                break
            #edge case: skip dupes
            if i>0 and a == nums[i-1]:
                continue
            #(num 2 & 3) set l & r pointers to the ends
            l = i+1
            r = len(nums)-1

            #two pointer method 
            while l < r:
                total = a + nums[l] + nums[r]

                #if total > 0, decrease r & total < 0, increase l
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    #0 is found
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    #skip dupes we saw already
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res











        