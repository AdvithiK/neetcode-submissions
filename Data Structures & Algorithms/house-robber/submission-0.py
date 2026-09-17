class Solution:
    def rob(self, nums: List[int]) -> int:
        #greedy algo + alternate
        #only start at two alternates i or i+1
        #recursively -> redundant, use DP !!
        
        #use memoization to keep log of computed paths
        memo = [-1] * len(nums)
        

        def dfs(i):
            if i > len(nums) - 1:
                return 0
            if memo[i] != -1:
                return memo[i]
            #find the path of starting at i
            skip = dfs(i+1)
            #find the path of starting at i+1
            rob = nums[i] + dfs(i+2)

            #store the max between both paths in memo[i]
            memo[i] = max(skip,rob)
            return memo[i]
        return dfs(0)

        