class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #two pointer solution

        #set l & r pointers to opposite ends
        l,r = 0, len(heights)-1

        #set a res to store final result
        res = 0

        while l < r:
            #compute the area
            area = (r-l)* min(heights[r],heights[l])
            
            res = max(res,area)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res


        