def find3number(self,A, n):
    small = [0] * n
    big = [0] * n
    temp = math.inf
    for i in range(n):
        temp = min(A[i], temp)
        small[i] = temp
    temp = - math.inf
    for i in range(n-1, -1, -1):
        temp = max(A[i], temp)
        big[i] = temp
    
    for i in range(1, n-1):
        if small[i-1]<A[i]<big[i+1]:
            return [small[i-1], A[i], big[i+1]]
            break
    else:
        return []