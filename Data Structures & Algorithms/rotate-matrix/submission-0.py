class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #store one temp at a time
        #create calls for each direction move

        #set boundaries
        l,r = 0, len(matrix)-1

        #while left doesn't cross past r, rotate
        while l < r:
            for i in range(r-l):
                top,bottom = l, r

                #save the top left
                topLeft = matrix[top][l+i]

                #move bottom left to top left
                matrix[top][l+i] = matrix[bottom-i][l]

                #move bottom right to bottom left
                matrix[bottom-i][l] = matrix[bottom][r-i]

                #move top right to bottom right
                matrix[bottom][r-i] = matrix[top+i][r]

                #move top left to top right
                matrix[top+i][r] = topLeft

            r -= 1
            l += 1

    
        
        