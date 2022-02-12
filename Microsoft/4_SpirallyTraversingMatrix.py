#idea is to maintain the last row and column index that are not visited
#for top bottom left and right and then incerement them as we visit the rows and columns
#also maintain the direction to know which direction we are going to visit like 1 for left to right ie top row 
# and 2 for top to bottom ie left column 
 

def spirallyTraverse(self,matrix, r, c): 
        top = 0
        bottom = r-1
        left = 0
        right = c-1
        
        direction = 1
        res = []
        while bottom >= top and right >= left:
            if direction == 1:
                for i in range(left, right + 1):
                    res.append(matrix[top][i])
                top += 1
                direction = 2
            elif direction ==2:
                for i in range(top, bottom + 1):
                    res.append(matrix[i][right])
                right -= 1
                direction = 3
            elif direction == 3:
                for i in range(right, left -1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1
                direction = 4
            else:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
                direction = 1
        return res