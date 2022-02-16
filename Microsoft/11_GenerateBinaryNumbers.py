def generate(N):
    res = []
    for i in range(1, N+1):
        s = ""
        temp = i
        while temp:
            if not temp%2:
                s = '0' + s
            else:
                s = '1' + s 
            temp = temp // 2
        res.append(s)
    return res