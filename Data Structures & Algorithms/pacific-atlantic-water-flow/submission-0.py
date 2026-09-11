class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #set rows & cols
        ROWS, COLS = len(heights), len(heights[0])

        #have two hash sets (pacific & atlantic)
        pacific, atlantic = set(), set()

        #dfs function
        def dfs(r,c,visit, prevHeight):
            #EDGE CASE: check if coord is visited already & norm edge cases
            if((r,c) in visit or 
            r < 0 or c < 0 or r == ROWS or c == COLS or 
            heights[r][c] < prevHeight):
                return
            visit.add((r,c))
            #go through LRUD for each coord
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
            


        #go through each col in the first row
        for c in range(COLS):
            #run dfs on every col in the first row
            dfs(0,c,pacific, heights[0][c])
            #run dfs on every col in the last row
            dfs(ROWS-1, c, atlantic, heights[ROWS-1][c])
        for r in range(ROWS):
            #run dfs on every row in the first row
            dfs(r,0,pacific, heights[r][0])
            #run dfs on every row in the last row
            dfs(r, COLS-1, atlantic, heights[r][COLS-1])

        #go through every pos in grid & return all coords in both hashsets 
        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        
        return res
        