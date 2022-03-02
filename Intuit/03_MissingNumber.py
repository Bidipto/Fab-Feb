def missingNumber(string):
    arr = [i for i in string]
    
    for i in range(1,7):
        prev = -1
        j = 0
        missing = []
        gap = i
        while j + gap <= len(string):
            temp = int("".join(arr[j: j+gap]))
            if prev != -1:
                #edge case for 98,998,9998
                if prev == int("".join(["9" for j in range(gap-1)] + ['8'])) and j+gap<len(arr) and temp*10 + int(arr[j+gap]) == int("".join( ["1"] + ["0" for j in range(gap)])):
                    missing.append(prev + 1)
                    gap += 1
                    temp = temp*10 + int(arr[j+gap-1])
                elif temp - 1 == prev:
                    pass
                elif temp - 2 == prev:
                    missing.append(temp-1)
                else:
                    break
                prev = temp
            else:
                prev = temp
            j = j+gap
            nine = int("".join(["9" for j in range(gap)]))
            
            if temp == nine:
                gap += 1
        
        if j == len(string) and len(missing) == 1:
            return missing[0]
    return -1

print(missingNumber("99899910001002"))
