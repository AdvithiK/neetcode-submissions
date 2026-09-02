class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #use recursive dfs & backtracking

        #vars to refer too
        ROWS, COLS = len(board), len(board[0])
        #a set to store coords we already explored (store the path)
        path = set()

        #nested dfs function
        def dfs(row, col, letter):
            #return case: if letter is last letter
            if letter == len(word):
                return True
            #edge case: if row or col is out of bounds
            if (row < 0 or col < 0 or row >= ROWS or col >= COLS):
                return False
            
            #edge case: if word[i] is not in the board or (row,col) is in the path
            if (word[letter] != board[row][col] or (row, col) in path):
                return False
            
            #append the (row, col) to path
            path.add((row, col))

            #dfs for L R U D check
            res = (dfs(row+1,col,letter+1) or 
                   dfs(row-1,col,letter+1) or 
                   dfs(row,col+1,letter+1) or
                   dfs(row, col-1,letter+1))
            
            #remove the position we just added because we aren't visiting it again
            path.remove((row, col))
            return res
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        return False




