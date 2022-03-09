def recoverArray(self, n: int, sums: List[int]) -> List[int]:
    #for every number we need the calculate the including and the exculding sums
    #the number can be calucualted by the diff between the max element and the second max element
    # therefore for every element in including the must exist a sum the doesnt include the number
    sums.sort()
    res = []
    while len(sums) > 1:
        diff = sums[-1] - sums[-2]
        including = []
        excluding = []
        counter = Counter(sums)
        
        for i in sums:
            if counter[i]>0:
                excluding.append(i)
                including.append(i + diff)
                counter[i] -= 1
                counter[i+diff] -=1
        if 0 in excluding:
            sums = excluding
            res.append(diff)
        else:
            sums = including
            res.append(-1*diff)
            
    return res