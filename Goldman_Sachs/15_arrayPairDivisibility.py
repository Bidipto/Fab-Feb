k = 8
nums = [13, 13]

def canPair(nums, k):
    lst = [i%k for i in nums]
    check = dict()
    while lst:
        temp = lst.pop()
        if temp in check.keys():
            check[temp] += 1
        elif k-temp in check.keys():
            check[k-temp] -= 1
        else:
            check[k-temp] = -1
    
    for i in check.keys():
        if i == k and check[i]%2 != 0:
            return False
        else:
            continue
        if check[i] != 0:
            return False
    return True

print(canPair(nums, k))




