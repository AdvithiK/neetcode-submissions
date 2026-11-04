class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #DP solution

        #initialize a memo
        memo = {}

        #dfs function
        def dfs(i,j):
            #check if i or j at the end
            if i == len(text1) or j == len(text2):
                return 0
            #if the pair exists in memo return
            if (i,j) in memo:
                return memo[(i,j)]
            
            #if they match add to their memo
            if text1[i] == text2[j]:
                memo[(i,j)] = 1 + dfs(i+1, j+1)  
            else:
                memo[(i,j)] = max(dfs(i+1, j),dfs(i, j+1))      
            
            return memo[(i,j)]
        return dfs(0,0)   
            