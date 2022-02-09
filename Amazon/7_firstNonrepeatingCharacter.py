S = "hrqcvsvszpsjammdrw"
from collections import deque 
def FirstNonRepeating(S):
    que = deque()
    srr = set()
    srr.add(S[0])
    temp = S[0]
    res = S[0]
    #two cases if temp == "" or temp is some non repeating letter
    for i in S[1:]:
        if temp:
            if temp == i:
                # the last temp has to be change with the next earliest non-repeating letter, 
                # which is stored in the deque
                if que:
                    temp = que.popleft()
                    res += temp
                else:
                    res += "#"
                    temp = ""
            # when i not temp,therefore temp will not change 
            else:
                res += temp
                if i not in srr:
                    srr.add(i)
                    que.append(i)
                elif i in que:
                    que.remove(i)
        else:
            #when a new non-repeating letter is found
            if i not in srr:
                res += i
                temp = i
                srr.add(i)
            else:
                res += "#"
    return res

print(FirstNonRepeating(S))