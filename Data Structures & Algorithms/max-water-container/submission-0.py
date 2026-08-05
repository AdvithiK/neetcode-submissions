class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #two pointers L & R set to opposite ends

        res = 0 
        l,r = 0, len(heights)-1
        while l < r:
            #calculate the area
            area = (r-l)*min(heights[l],heights[r])
            #result is the max area we've calculated
            res = max(res,area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res
            



        