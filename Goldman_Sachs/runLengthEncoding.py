from tempfile import tempdir


def encode(arr):
    tempalp = []
    tempnum = []
    counter = 1
    temp = arr[0]
    for i in arr[1:]:
        if i == temp:
            counter += 1
        else:
            tempalp.append(temp)
            tempnum.append(counter)
            temp = i
            counter = 1
            
    tempalp.append(temp)
    tempnum.append(counter)

    res = []
    for i in range(len(tempalp)):
        res.append(str(tempalp[i]))
        res.append(str(tempnum[i]))

    return "".join(res)



#  Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        arr=input().strip()
        print (encode(arr))
# } Driver Code Ends