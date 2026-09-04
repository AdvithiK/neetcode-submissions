class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #make a list of directions to refer to for checking
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        #grab the rows & columns for 2d array/graph questions
        rows, cols = len(grid), len(grid[0])

        #global count for islands found
        islands = 0
        
        #bfs looking for 1s
        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r,c))
            
            while q:
                row, col = q.popleft()

                #loop checking thru horizontal & vertical directions
                for dr,dc in directions:
                    nr,nc = row + dr, col + dc
                    if (nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == "0"):
                        continue
                    #append the new island 1 found to queue & visited
                    q.append((nr, nc))
                    grid[nr][nc] = "0"
        
        #go through each row and column
        for i in range(rows):
            for j in range(cols):
                #if we visit a 1, traverse it with bfs, increment islands
                if grid[i][j] == "1":
                    bfs(i,j)
                    islands += 1
                    

        return islands












