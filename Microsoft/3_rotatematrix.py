matrix = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

def rotate(matrix): 
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]
    print(matrix)
    for i in range(len(matrix)):
        for j in range(i,len(matrix)):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    return matrix

#leetcode question
def rotateclockwise(self, matrix: List[List[int]]) -> None:
    for i in range(len(matrix)):
        for j in range(i,len(matrix)):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]
    return matrix


print(rotate(matrix))