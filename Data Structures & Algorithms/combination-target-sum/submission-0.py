class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #backtracking
        res = []

        #recursive dfs helper function
        def dfs(i, currlist, total):
            #return case & edge case
            if total == target:
                res.append(currlist.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            #choice 1: include nums[i]
            currlist.append(nums[i])
            dfs(i, currlist, total+nums[i])
            currlist.pop()
            #choice 2: skip nums[i]
            dfs(i+1, currlist,total)
        #call dfs
        dfs(0,[],0)
        return res
            

                


        