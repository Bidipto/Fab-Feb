N = "3553"
def nextPalin(N):
    N = list(N)
    if len(N) == 1 or len(N) == 2 or len(N) == 3:
        return 0
    
    floor = len(N)//2 -1
    
    #arr is the arr we work with 
    arr = N[:floor+1]
    
    for i in range(len(arr) - 1, 0, -1):
        #searching for a peak and storing the element before peak in swap
        if arr[i-1]<arr[i]:
            swap = arr[i-1]
            pos = i - 1
            break
    # there exists no element before peak ie the element is already maximix=zed
    else:
        return -1
    
    for i in range(len(arr) - 1, pos, -1):
        if int(swap)<int(arr[i]):
            arr[pos],arr[i] = arr[i],arr[pos]
            break
    arr[pos+1:] = sorted(arr[pos+1:])
    
    #building the palindrome
    #even
    if len(N)%2 == 1:
        res = arr + [N[floor + 1]] + arr[::-1]
    else:
        res = arr + arr[::-1]
        
    return "".join(res)

print(nextPalin(N))