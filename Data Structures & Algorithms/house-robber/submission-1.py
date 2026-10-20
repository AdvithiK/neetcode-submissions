class Solution:
    def rob(self, nums: List[int]) -> int:
        #creating empty memo board to track robberies
        memo = [-1] * len(nums)

        #dfs function to find possible ways to rob
        def dfs(i):
            #edge case: if i is out of bounds
            if i > len(nums) - 1:
                return 0

            #edge case: if i in memo board
            if memo[i] != -1:
                return memo[i]
            
            #skip
            skip = dfs(i+1)
            #rob 
            rob = nums[i] + dfs(i+2)

            memo[i] = max(skip,rob)
            return memo[i]
        return dfs(0)

        