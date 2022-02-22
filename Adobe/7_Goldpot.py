arr = [8, 15, 3, 7]
n = len(arr)

def maxCoins(arr, n):
    dp = {} 
    def magic(left, right, player): 
        if left > right: 
            return 0 
        if (left, right, player) in dp: 
            return dp[(left, right, player)] 
        if player: 
            #we are maximizing for player 1
            result = max(magic(left + 1, right, not player) + pots[left], 
                            magic(left, right - 1, not player) + pots[right]) 
        else: 
            #we are maximizing for player 2, ie minimizing for player 1
            result = min(magic(left + 1, right, not player), 
                            magic(left, right - 1, not player)) 
        dp[(left, right, player)] = result 
        return result 

        return magic(0, len(pots)-1, True)

print(maxCoins(arr, n))
        