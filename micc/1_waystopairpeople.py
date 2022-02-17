limit = 5

#basic recursive approach 
def magic(n):
    # base case for 1 element 
    if n == limit:
        return 1 
    #base case for out of bountds
    if n == limit + 1:
        return 0

    single =  magic(n + 1)
    #i can form pairs with all the elements that are left  
    double = magic(n + 2) * (limit-n-1)
    
    #print(single, double, n)
    return single + double

# print(magic(0))

#recursive approach with memoization
dp = [-1] * limit
def magicdp(n, dp):
    # base case for 1 element 
    if n == limit:
        return 1 
    #base case for out of bountds
    if n == limit + 1:
        return 0

    if dp[n] != -1:
        return dp[n]

    single =  magicdp(n + 1, dp)
    #i can form pairs with all the elements that are on its right  
    double = magicdp(n + 2, dp) * (limit-n-1)
    
    dp[n] = single + double
    print(single, double, n)
    return dp[n]

print(magicdp(0, dp))

#tabulization with space optimization 
prev=1 #singles
now=1 #doubles

for i in range(limit-2, -1, -1):
    print(i, now, prev)
    temp = now + (prev * (limit - i -1))
    prev = now
    now = temp

print(now) 
    
