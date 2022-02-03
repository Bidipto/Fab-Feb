class Solution:
    def printMinNumberForPattern(self,s):
        # for each sequence we have to track the number of the number of following Ds if a I is found
        # if we have a conseqitive Is the numeber of trailing Ds is zero except for the last D
        # there is a special case for the first element since there is only n-1 Is and Ds
        # therefore we have to print the first element 
        # we have to aslo keep track of the max element print until now and the last element 
        res = []
        i = 0
        #the last element visited
        last = 0
        #the max element printed
        maxi = 0   
        #ID
        #132
        while(i<len(s)):
            Dtrail = 0
            # when the next element is I
            if s[i] == 'I':
                j = i + 1

                while j<len(s) and s[j] == "D":
                    j += 1
                    Dtrail += 1

                if i == 0:
                    last = Dtrail + 2
                    maxi = last
                    #print(1, end="")
                    res.append(1)
                    #print(last, end="")
                    res.append(last)
                    i += 1
                else:
                    last = maxi + Dtrail + 1
                    maxi = last
                    # print(last, end="")
                    res.append(last)
                    i += 1 
                #since we know the number of trailing Ds we can print then
                for q in range(Dtrail):
                    last -= 1
                    # print(last, end = "")
                    res.append(last)
                    i += 1
            else:
                j = i + 1
                Dtrail = 1
                while j<len(s) and s[j] == "D":
                    Dtrail += 1
                    j += 1
                maxi = Dtrail + 1
                last = maxi
                # print(last, end="")
                res.append(last)
                for q in range(Dtrail):
                    last -= 1
                    # print(last, end="")
                    res.append(last)
                    i += 1
        return ''.join([str(i) for i in res])

            

S = "DDIDDIID"               
ob = Solution()
print(ob.printMinNumberForPattern(S))


# if __name__ == '__main__': 
#     t = int (input ())
#     for _ in range (t):
        
#         S=str(input())

#         ob = Solution()
#         print(ob.printMinNumberForPattern(S))
