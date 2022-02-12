arr = [[1, 0, 0, 0],
         [1, 1, 0, 1], 
         [1, 1, 1, 0],
         [0, 1, 1, 1]]
N = len(arr)

#initial intuition, looks like a DP problem

#simple backtrack without using DP
#for a dp solution we can make a 2d matrix and then for each well we can keep the path upto that point in the cell
#therefore if we have two paths form a cell we can use the stored value instead of calculating it again
def findPath(arr, N):
    res = []
    def magic(m , n, arr, curr):
        if m == N - 1 and n == N - 1:
            res.append(curr)
            return
        #if we are rat is not allowed to enter the maze
        if arr[0][0] != 1:
            return []
        #up
        if m != 0:
            if arr[m - 1][n] == 1:
                #this is to prevent from coming back
                arr[m][n] = 0
                magic(m - 1, n, arr, curr + 'U')
                arr[m][n] = 1
        #down
        if m != N - 1:
            if arr[m + 1][n] == 1:
                arr[m][n] = 0
                magic(m + 1, n, arr, curr + 'D')
                arr[m][n] = 1
        #left
        if n != 0:
            if arr[m][n - 1] == 1:
                arr[m][n] = 0
                magic(m, n - 1, arr, curr + 'L')
                arr[m][n] = 1
        #right
        if n != N - 1:
            if arr[m][n + 1] == 1:
                arr[m][n] = 0
                magic(m, n + 1, arr, curr + 'R')
                arr[m][n] = 1
    magic(0, 0, arr, '')
    return res

print(findPath(arr, N))

