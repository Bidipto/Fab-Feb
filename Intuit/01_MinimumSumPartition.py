arr = [1, 6, 5, 11]
def minDifference(arr, n):
    summ = sum(arr)
    target = summ // 2
    dp = set()
    dp.add(0)
    res = 0
    
    for i in range(len(arr) -1, -1, -1):
        nextdp = set()
        for j in dp:
            if j + arr[i] <= target:
                print(res)
                res = max(res, j + arr[i])
            nextdp.add(j + arr[i])
            nextdp.add(j)
        
        dp = nextdp
    ans = (summ - res) - res
    return ans

# print(minDifference(arr, len(arr)))
print(int("".join(["9" for i in range(2)])))