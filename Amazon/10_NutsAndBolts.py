nuts = ['@', '%', '$', '#', '^']
bolts = ['%', '@', '#', '$', '^']
ref = ['!', '#', '$', '%', '&', '*', '@', '^', '~']

def matchPairs(nuts, bolts, n):
    k = 0
    p = 0
    for i in range(9):
        for j in range(k,n):
            if ref[i] == nuts[j]:
                nuts[j],nuts[k] = nuts[k],nuts[j]
                k += 1
                break
        for q in range(p,n):
            if ref[i] == bolts[q]:
                bolts[q],bolts[p] = bolts[p],bolts[q]
                p += 1
                break
    return nuts,bolts

print(matchPairs(nuts, bolts, len(nuts)))