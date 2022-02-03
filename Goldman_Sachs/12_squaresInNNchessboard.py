N = 7
#accumulates the total number of size 1 square to size n-1 square
res = 0
for i in range(N,0,-1):
    res += pow(i,2)
print(res)