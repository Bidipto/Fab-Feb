#User function Template for python3

class Solution:
    def Anagrams(self, words, n):
        dic = dict()
        for i in words:
            word = "".join(sorted(i))
            if word in dic.keys():
                dic[word].append(i)
            else:
                dic[word] = [i]
        res = []
        for i in dic.keys():
            res.append(dic[i])
        return res

    def new_method(self, i):
        word = ''.join(sorted(i))
        return word
                
#  Driver Code Starts
#Initial Template for Python 3
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        words=input().split()
        
        ob = Solution()
        ans = ob.Anagrams(words,n)
        
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()

# } Driver Code Ends