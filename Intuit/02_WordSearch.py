class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M = len(board)
        N = len(board[0])
        
        path = set()
        
        def magic(m , n, i):
            #base case if the word is found
            if i == len(word):
                # print(m,n)
                return True
            
            #outofbounds check
            if m>=M or n>=N or m<0 or n<0:
                # print(m,n,1)
                return False
            
            #if we go into a previously visited element
            if (m, n) in path:
                # print(m,n,2)
                return False
            
            #if the word does not match the curent letter in word
            if board[m][n] != word[i]:
                # print(m,n,3)
                return False
            #adding the current position in path
            path.add((m, n))
            
            #next seach in four direction
            res = magic(m + 1, n, i + 1) or magic(m - 1, n, i + 1) or magic(m, n + 1, i + 1) or magic(m, n - 1, i + 1) 
            # print(path)
            #removing the visited position for visited set
            path.remove((m, n))
            
            return res
        
        # return magic(1, 3, 0)
        for i in range(M):
            for j in range(N):
                if magic(i,j,0):
                    return True
        return False
            