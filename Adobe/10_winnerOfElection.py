def winner(self,arr,n):
        # return the name of the winning candidate and the votes he recieved
        dic = Counter(arr)
        temp = -1
        res = []
        for i in dic:
            if dic[i]>temp:
                res = [i,dic[i]]
                temp = dic[i]
            elif dic[i] == temp and i<res[0]:
                res = [i,dic[i]]
        return res